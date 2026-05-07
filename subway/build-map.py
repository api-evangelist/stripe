#!/usr/bin/env python3
"""Build a subway-style map of the Stripe API.

Each Stripe OpenAPI file is a station; APIs are grouped onto colored lines that
mirror Stripe's product taxonomy (Payments, Billing, Connect, etc.).

Outputs an HTML file with embedded SVG (for browser viewing + printing) at
8.5x11 in landscape orientation.
"""

import html
import os
from pathlib import Path

# ---------------------------------------------------------------------------
# Map data — lines (color-coded subway lines) and their stations
# ---------------------------------------------------------------------------

# Display abbreviations for stations whose canonical name is too long for the
# rotated subway label. Anything not listed here renders as-is.
ABBREV = {
    "Payment Method Configurations": "PM Configurations",
    "Application Secrets": "App Secrets",
    "Application Fees": "App Fees",
}


LINES = [
    {
        "name": "Checkout & Links",
        "short": "Checkout",
        "color": "#7B3FE4",
        "stations": [
            "Crypto Onramp",
            "Link",
            "Customer Portal",
            "Payment Links",
            "Checkout",
        ],
    },
    {
        "name": "Payments",
        "short": "Payments",
        "color": "#E0245E",
        "stations": [
            "Customers",          # interchange with Billing
            "Tokens",
            "Sources",
            "Apple Pay",
            "Payment Methods",
            "Payment Method Configurations",
            "Setup",
            "Payment Intents",
            "Charges",
            "Refunds",            # interchange with Risk
        ],
    },
    {
        "name": "Billing — Core",
        "short": "Billing Core",
        "color": "#0E9D6E",
        "stations": [
            "Customers",          # interchange with Payments
            "Invoice",
            "Subscription",
            "Plans",
            "Prices",
            "Products",
            "Billing",
            "Billing Meters",
        ],
    },
    {
        "name": "Billing — Catalog & Tax",
        "short": "Billing Tax",
        "color": "#0B7956",
        "stations": [
            "Coupons",
            "Promotion Codes",
            "Credit Notes",
            "Quotes",
            "Shipping Rates",
            "Tax",
            "Entitlements",
            "Revenue Recognition",
        ],
    },
    {
        "name": "Connect",
        "short": "Connect",
        "color": "#E68B1F",
        "stations": [
            "Accounts",           # interchange with Issuing/Treasury
            "Connect",
            "Application Fees",
            "Application Secrets",
            "Transfers",
            "Payouts",
            "Topups",
            "Balance",
        ],
    },
    {
        "name": "Issuing & Treasury",
        "short": "Issuing/Treasury",
        "color": "#1E5BD0",
        "stations": [
            "Accounts",            # interchange with Connect (must be first to align vertically)
            "Issuing",
            "Treasury",
            "Financial Connections",
        ],
    },
    {
        "name": "Risk & Disputes",
        "short": "Risk",
        "color": "#C5318B",
        "stations": [
            "Identity",
            "Radar",
            "Reviews",
            "Disputes",
            "Refunds",             # interchange with Payments
        ],
    },
    {
        "name": "Reporting & Data",
        "short": "Reporting",
        "color": "#5A6275",
        "stations": [
            "Sigma",
            "Reporting",
            "Events",
            "Webhook",
            "Files",
            "Exchange Rates",
            "Country",
            "Ephemeral Keys",
        ],
    },
    {
        "name": "Sustainability & Edge",
        "short": "Edge",
        "color": "#B89719",
        "stations": [
            "Climate",
            "Forwarding",
            "Terminal",
            "Test Helpers",
        ],
    },
]

# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------

# 8.5 x 11 landscape at 100dpi-ish viewBox => 1100 x 850
W, H = 1100, 850

TITLE_BOTTOM = 70
KEY_TOP = 815                       # small key bar at the bottom
MAP_TOP = TITLE_BOTTOM + 25         # 95
MAP_BOTTOM = KEY_TOP - 5            # 810
MAP_HEIGHT = MAP_BOTTOM - MAP_TOP   # 715

# Horizontal margins for the map area
LINE_LABEL_W = 140                  # space reserved for the line name on the left
MAP_LEFT = 30 + LINE_LABEL_W        # 170
MAP_RIGHT = W - 60
MAP_WIDTH = MAP_RIGHT - MAP_LEFT


def line_y(idx, n):
    """Vertical y for line `idx` of `n` lines, evenly spaced inside the map area."""
    # leave breathing room top and bottom
    pad = 30
    available = MAP_HEIGHT - 2 * pad
    return MAP_TOP + pad + (idx + 0.5) * available / n


def station_x(idx, n):
    """Horizontal x for station `idx` of `n` stations on a line."""
    pad = 40
    available = MAP_WIDTH - 2 * pad
    return MAP_LEFT + pad + idx * available / max(1, n - 1)


def main():
    n_lines = len(LINES)

    # Compute station positions: dict { (line_index, station_index) -> (x, y, name) }
    positions = {}
    # Also collect, per station name, a list of (x, y, line_index) for interchange detection.
    by_name = {}
    for li, ln in enumerate(LINES):
        y = line_y(li, n_lines)
        for si, st in enumerate(ln["stations"]):
            x = station_x(si, len(ln["stations"]))
            positions[(li, si)] = (x, y, st)
            by_name.setdefault(st, []).append((x, y, li))

    interchange_names = {n for n, ps in by_name.items() if len(ps) > 1}

    # ------------------------------------------------------------------
    # Build SVG
    # ------------------------------------------------------------------
    parts = []
    parts.append(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
                 f'preserveAspectRatio="xMidYMid meet" '
                 f'font-family="-apple-system, BlinkMacSystemFont, Helvetica Neue, Arial, sans-serif">')

    # Background
    parts.append(f'<rect width="{W}" height="{H}" fill="#FAFAF7"/>')

    # Title
    parts.append(
        f'<text x="{W/2}" y="36" text-anchor="middle" font-size="26" font-weight="700" '
        f'fill="#1A1F2C" letter-spacing="0.5">The Stripe API · Subway Map</text>'
    )
    parts.append(
        f'<text x="{W/2}" y="58" text-anchor="middle" font-size="11" fill="#5A6275" '
        f'letter-spacing="1.5" font-weight="500">'
        f'57 APIs · {len(LINES)} functional lines · interchange stations link related domains'
        f'</text>'
    )

    # Subtle horizontal grid
    parts.append('<g opacity="0.05" stroke="#000" stroke-width="0.5">')
    for x in range(MAP_LEFT, MAP_RIGHT, 40):
        parts.append(f'<line x1="{x}" y1="{MAP_TOP}" x2="{x}" y2="{MAP_BOTTOM}"/>')
    parts.append('</g>')

    # ------------------------------------------------------------------
    # Draw each line as a single horizontal subway track + stations
    # ------------------------------------------------------------------
    LINE_W = 9
    STATION_R = 7
    INTERCHANGE_R = 11

    # Pre-compute interchange transfer connectors (vertical lines linking same-named stations)
    transfer_groups = []
    for name in sorted(interchange_names):
        ys = [(y, li) for (x, y, li) in by_name[name]]
        ys.sort()
        # vertical line from min y to max y at the average x
        xs = [x for (x, y, li) in by_name[name]]
        avg_x = sum(xs) / len(xs)
        transfer_groups.append({
            "name": name,
            "x_avg": avg_x,
            "y_min": min(y for y, li in ys),
            "y_max": max(y for y, li in ys),
            "points": by_name[name],
        })

    # Draw transfer connectors first (so lines + stations sit on top).
    # Interchange stations now share an x — connectors are clean vertical lines.
    parts.append('<g>')
    for tg in transfer_groups:
        pts = sorted(tg["points"], key=lambda p: p[1])
        for i in range(len(pts) - 1):
            x1, y1, _ = pts[i]
            x2, y2, _ = pts[i+1]
            parts.append(
                f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
                f'stroke="#1A1F2C" stroke-width="2.5" stroke-linecap="round" opacity="0.55" />'
            )
    parts.append('</g>')

    # Draw lines (single horizontal stroke per subway line) + left-side line label
    for li, ln in enumerate(LINES):
        y = line_y(li, n_lines)
        x_first, _, _ = positions[(li, 0)]
        x_last, _, _ = positions[(li, len(ln["stations"]) - 1)]
        parts.append(
            f'<line x1="{x_first}" y1="{y}" x2="{x_last}" y2="{y}" '
            f'stroke="{ln["color"]}" stroke-width="{LINE_W}" stroke-linecap="round" />'
        )
        # Line name as colored bar + label on the left
        label_x = 36
        # colored chip
        parts.append(
            f'<rect x="{label_x}" y="{y-9}" width="6" height="18" rx="3" '
            f'fill="{ln["color"]}"/>'
        )
        parts.append(
            f'<text x="{label_x + 14}" y="{y - 2}" font-size="11" '
            f'font-weight="700" fill="#1A1F2C">{html.escape(ln["name"])}</text>'
        )
        parts.append(
            f'<text x="{label_x + 14}" y="{y + 12}" font-size="9" '
            f'fill="#5A6275">{len(ln["stations"])} APIs</text>'
        )

    # Draw stations.
    # Strategy: alternate labels above/below the line (even index above, odd below)
    # which halves label density and removes overlap on dense lines.
    for li, ln in enumerate(LINES):
        y = line_y(li, n_lines)
        for si, st in enumerate(ln["stations"]):
            x, _, _ = positions[(li, si)]
            is_inter = st in interchange_names
            r = INTERCHANGE_R if is_inter else STATION_R
            ring = "#1A1F2C" if is_inter else ln["color"]
            ring_w = 3.5 if is_inter else 2.5
            tooltip = f"{st} — {ln['name']} line"
            if is_inter:
                others = [LINES[other_li]["name"] for (_, _, other_li) in by_name[st]]
                tooltip = f"{st} — interchange across: {', '.join(others)}"
            parts.append(
                f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFFFFF" '
                f'stroke="{ring}" stroke-width="{ring_w}">'
                f'<title>{html.escape(tooltip)}</title>'
                f'</circle>'
            )

            # Show interchange labels only once (on the first line they appear).
            first_line_for_name = by_name[st][0][2]
            if is_inter and li != first_line_for_name:
                continue

            label = ABBREV.get(st, st)
            # Vertical: alternate above/below by station index.
            # Horizontal: labels in the LEFT half of the line extend RIGHT;
            # labels in the RIGHT half extend LEFT. This keeps every label
            # comfortably inside the canvas.
            above = (si % 2 == 0)
            n_stations = len(ln["stations"])
            extend_left = (si > (n_stations - 1) / 2)
            offset = r + 8
            weight = "700" if is_inter else "600"

            if above:
                tx, ty = x, y - offset
                if extend_left:
                    anchor, angle = "end", -35
                else:
                    anchor, angle = "start", 35
            else:
                tx, ty = x, y + offset + 4
                if extend_left:
                    anchor, angle = "end", 35
                else:
                    anchor, angle = "start", -35

            parts.append(
                f'<text x="{tx}" y="{ty}" font-size="10" fill="#1A1F2C" '
                f'text-anchor="{anchor}" font-weight="{weight}" '
                f'transform="rotate({angle} {tx} {ty})">{html.escape(label)}</text>'
            )

    # ------------------------------------------------------------------
    # Compact key bar (just the interchange marker explanation;
    # line names are already labeled on the left of each line)
    # ------------------------------------------------------------------
    parts.append(f'<g transform="translate(0 {KEY_TOP})">')
    kx = 36
    parts.append(
        f'<circle cx="{kx + 8}" cy="8" r="6" fill="#FFFFFF" '
        f'stroke="{LINES[0]["color"]}" stroke-width="2.5" />'
    )
    parts.append(
        f'<text x="{kx + 22}" y="12" font-size="10" fill="#1A1F2C">Station — single API endpoint group</text>'
    )
    kx2 = 320
    parts.append(
        f'<circle cx="{kx2 + 10}" cy="8" r="9" fill="#FFFFFF" '
        f'stroke="#1A1F2C" stroke-width="3" />'
    )
    parts.append(
        f'<text x="{kx2 + 26}" y="12" font-size="10" fill="#1A1F2C" font-weight="600">'
        f'Interchange — API serves multiple lines (transfer connector shown)</text>'
    )
    parts.append('</g>')

    # Footer / source
    parts.append(
        f'<text x="{W-30}" y="{H-12}" text-anchor="end" font-size="8.5" fill="#8A92A6">'
        f'Source: stripe/openapi/*-openapi.yml · github.com/api-evangelist/stripe</text>'
    )

    parts.append('</svg>')
    svg = "\n".join(parts)

    # ------------------------------------------------------------------
    # HTML wrapper with print stylesheet for landscape letter
    # ------------------------------------------------------------------
    html_doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>The Stripe API · Subway Map</title>
<style>
  @page {{ size: 11in 8.5in; margin: 0; }}
  html, body {{ margin: 0; padding: 0; background: #FAFAF7; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif; }}
  .sheet {{
    width: 11in; height: 8.5in;
    margin: 0 auto;
    box-shadow: 0 2px 16px rgba(0,0,0,0.08);
    background: #FAFAF7;
    display: block;
  }}
  .sheet svg {{ width: 100%; height: 100%; display: block; }}
  @media print {{
    .sheet {{ box-shadow: none; }}
    body {{ background: #FFFFFF; }}
  }}
</style>
</head>
<body>
<div class="sheet">
{svg}
</div>
</body>
</html>
"""

    out_dir = Path("/Users/kinlane/GitHub/all/stripe/subway")
    out_dir.mkdir(exist_ok=True)
    (out_dir / "stripe-subway-map.svg").write_text(svg)
    (out_dir / "stripe-subway-map.html").write_text(html_doc)
    print(f"wrote {out_dir/'stripe-subway-map.svg'}")
    print(f"wrote {out_dir/'stripe-subway-map.html'}")


if __name__ == "__main__":
    main()
