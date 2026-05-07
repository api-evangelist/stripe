#!/usr/bin/env python3
"""Build a tube-style map of the Stripe API.

Each Stripe OpenAPI file is a station; APIs are grouped onto colored lines that
mirror Stripe's product taxonomy (Payments, Billing, Connect, etc.).

Lines are rendered as smooth cubic Bezier curves through hand-placed waypoints
so the map has the bends, arcs, and crossings of a real underground map rather
than parallel straight lines.

Outputs an HTML file with embedded SVG (for browser viewing + printing) at
8.5x11 in landscape orientation, plus a standalone SVG.
"""

import html
from pathlib import Path

# ---------------------------------------------------------------------------
# Display abbreviations for stations whose name is too long for the rotated label.
# ---------------------------------------------------------------------------
ABBREV = {
    "Payment Method Configurations": "PM Configurations",
    "Application Secrets": "App Secrets",
    "Application Fees": "App Fees",
}

# ---------------------------------------------------------------------------
# Layout (1100 x 850 viewBox = 8.5x11 in landscape)
# ---------------------------------------------------------------------------
W, H = 1100, 850

# Three interchange hubs anchor the map. Their (x,y) is shared across every
# line they belong to so transfer lines are clean and zero-length.
HUB = {
    "Customers": (240, 330),   # Payments + Billing-Core
    "Accounts":  (240, 600),   # Connect + Issuing & Treasury
    "Refunds":   (940, 330),   # Payments + Risk & Disputes
}

# ---------------------------------------------------------------------------
# Lines: each station has an explicit (x, y) so we can craft real subway shapes.
# Where a station name appears on multiple lines, it must use the same (x,y)
# to keep interchange transfer connectors collapsed to a single point.
# ---------------------------------------------------------------------------

LINES = [
    {
        "name": "Checkout & Links",
        "color": "#7B3FE4",
        # Gentle arc across the top
        "stations": [
            ("Crypto Onramp",  (300, 140)),
            ("Link",           (440, 110)),
            ("Customer Portal",(580, 100)),
            ("Payment Links",  (720, 110)),
            ("Checkout",       (860, 140)),
        ],
    },
    {
        "name": "Payments",
        "color": "#E0245E",
        # Horizontal main artery — the "Central Line".
        "stations": [
            ("Customers",                        HUB["Customers"]),
            ("Tokens",                           (320, 330)),
            ("Sources",                          (390, 330)),
            ("Apple Pay",                        (470, 330)),
            ("Payment Methods",                  (550, 330)),
            ("Payment Method Configurations",    (640, 330)),
            ("Setup",                            (720, 330)),
            ("Payment Intents",                  (800, 330)),
            ("Charges",                          (870, 330)),
            ("Refunds",                          HUB["Refunds"]),
        ],
    },
    {
        "name": "Billing — Core",
        "color": "#0E9D6E",
        # L-shape — goes vertically down from Customers, then bends 45° right.
        # Bend stations carry the geometry; visible stations appear at named points.
        "stations": [
            ("Customers",        HUB["Customers"]),
            ("Invoice",          (240, 400)),
            ("Subscription",     (240, 460)),
            ("Plans",            (300, 510)),    # post-bend
            ("Prices",           (370, 510)),
            ("Products",         (440, 510)),
            ("Billing",          (510, 510)),
            ("Billing Meters",   (580, 510)),
        ],
    },
    {
        "name": "Billing — Catalog & Tax",
        "color": "#0B7956",
        # Arc rising up the right side, rotates labels along the outer edge.
        "label_strategy": "above_rotated",
        "stations": [
            ("Coupons",            (650, 510)),
            ("Promotion Codes",    (720, 510)),
            ("Credit Notes",       (790, 510)),
            ("Quotes",             (855, 490)),
            ("Shipping Rates",     (905, 455)),
            ("Tax",                (945, 415)),
            ("Entitlements",       (970, 370)),
            ("Revenue Recognition",(990, 320)),
        ],
    },
    {
        "name": "Connect",
        "color": "#E68B1F",
        # Horizontal mid-bottom, anchored at the Accounts hub.
        "stations": [
            ("Accounts",        HUB["Accounts"]),
            ("Connect",         (320, 600)),
            ("Application Fees",(400, 600)),
            ("Application Secrets", (490, 600)),
            ("Transfers",       (570, 600)),
            ("Payouts",         (650, 600)),
            ("Topups",          (730, 600)),
            ("Balance",         (810, 600)),
        ],
    },
    {
        "name": "Issuing & Treasury",
        "color": "#1E5BD0",
        # Short vertical branch dropping below Accounts.
        "stations": [
            ("Accounts",              HUB["Accounts"]),
            ("Issuing",               (240, 660)),
            ("Treasury",              (240, 720)),
            ("Financial Connections", (240, 780)),
        ],
    },
    {
        "name": "Risk & Disputes",
        "color": "#C5318B",
        # Curve sweeping from lower-center up to Refunds.
        "stations": [
            ("Identity",  (470, 730)),
            ("Radar",     (610, 720)),
            ("Reviews",   (740, 680)),
            ("Disputes",  (860, 600)),
            ("Refunds",   HUB["Refunds"]),
        ],
    },
    {
        "name": "Reporting & Data",
        "color": "#5A6275",
        # Bottom-horizontal with a slight wave, well clear of other lines.
        "stations": [
            ("Sigma",          (340, 800)),
            ("Reporting",      (415, 805)),
            ("Events",         (490, 800)),
            ("Webhook",        (565, 805)),
            ("Files",          (640, 800)),
            ("Exchange Rates", (715, 805)),
            ("Country",        (790, 800)),
            ("Ephemeral Keys", (865, 805)),
        ],
    },
    {
        "name": "Sustainability & Edge",
        "color": "#B89719",
        # Small island arc on the right edge.
        "stations": [
            ("Climate",      (1015, 590)),
            ("Forwarding",   (1045, 650)),
            ("Terminal",     (1045, 720)),
            ("Test Helpers", (1010, 780)),
        ],
    },
]

# ---------------------------------------------------------------------------
# Geometry helpers
# ---------------------------------------------------------------------------

def catmull_rom_path(points, tension=0.5):
    """Return an SVG path string drawing a smooth cubic Bezier through points.

    Uses Catmull-Rom-to-Bezier conversion. tension in [0,1] (0.5 is canonical).
    """
    if len(points) == 1:
        x, y = points[0]
        return f"M{x},{y}"
    if len(points) == 2:
        (x1, y1), (x2, y2) = points
        return f"M{x1},{y1} L{x2},{y2}"

    d = [f"M{points[0][0]},{points[0][1]}"]
    n = len(points)
    for i in range(n - 1):
        p0 = points[i - 1] if i > 0 else points[i]
        p1 = points[i]
        p2 = points[i + 1]
        p3 = points[i + 2] if i + 2 < n else p2
        cp1x = p1[0] + (p2[0] - p0[0]) * tension / 3
        cp1y = p1[1] + (p2[1] - p0[1]) * tension / 3
        cp2x = p2[0] - (p3[0] - p1[0]) * tension / 3
        cp2y = p2[1] - (p3[1] - p1[1]) * tension / 3
        d.append(f"C{cp1x:.1f},{cp1y:.1f} {cp2x:.1f},{cp2y:.1f} {p2[0]},{p2[1]}")
    return " ".join(d)


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def main():
    # Build station positions and detect interchanges (same name on multiple lines)
    by_name = {}  # name -> list of (line_index, station_index, x, y)
    for li, ln in enumerate(LINES):
        for si, (st, (x, y)) in enumerate(ln["stations"]):
            by_name.setdefault(st, []).append((li, si, x, y))
    interchange_names = {n for n, ps in by_name.items() if len(ps) > 1}

    parts = []
    parts.append(
        f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
        f'preserveAspectRatio="xMidYMid meet" '
        f'font-family="-apple-system, BlinkMacSystemFont, Helvetica Neue, Arial, sans-serif">'
    )

    # Background + title
    parts.append(f'<rect width="{W}" height="{H}" fill="#FAFAF7"/>')
    parts.append(
        f'<text x="{W/2}" y="36" text-anchor="middle" font-size="26" font-weight="700" '
        f'fill="#1A1F2C" letter-spacing="0.5">The Stripe API · Underground Map</text>'
    )
    parts.append(
        f'<text x="{W/2}" y="58" text-anchor="middle" font-size="11" fill="#5A6275" '
        f'letter-spacing="1.5" font-weight="500">'
        f'57 APIs · {len(LINES)} functional lines · Customers, Accounts &amp; Refunds are interchange hubs'
        f'</text>'
    )

    # Lines (drawn first so stations sit on top)
    LINE_W = 9
    parts.append('<g fill="none" stroke-linecap="round" stroke-linejoin="round">')
    for ln in LINES:
        pts = [pos for (_, pos) in ln["stations"]]
        path = catmull_rom_path(pts, tension=0.6)
        parts.append(
            f'<path d="{path}" stroke="{ln["color"]}" stroke-width="{LINE_W}" />'
        )
    parts.append('</g>')

    # Stations (regular = small ringed circle in line color; interchange = bigger ringed black)
    STATION_R = 6.5
    INTERCHANGE_R = 11
    STATION_RING_W = 2.5
    INTERCHANGE_RING_W = 3.5

    # Track which stations we've already labeled (so interchange labels appear once)
    labeled = set()

    for li, ln in enumerate(LINES):
        for si, (st, (x, y)) in enumerate(ln["stations"]):
            is_inter = st in interchange_names
            r = INTERCHANGE_R if is_inter else STATION_R
            ring = "#1A1F2C" if is_inter else ln["color"]
            ring_w = INTERCHANGE_RING_W if is_inter else STATION_RING_W

            # Skip duplicate interchange circles (they'd render on top of each other)
            station_key = (st, x, y)
            if is_inter and station_key in labeled:
                # Still need the marker once — we'll draw it the first time we see it
                continue

            tooltip = f"{st} — {ln['name']} line"
            if is_inter:
                others = [LINES[other_li]["name"] for (other_li, _, _, _) in by_name[st]]
                tooltip = f"{st} — interchange across: {', '.join(others)}"

            parts.append(
                f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFFFFF" '
                f'stroke="{ring}" stroke-width="{ring_w}">'
                f'<title>{html.escape(tooltip)}</title>'
                f'</circle>'
            )

            # Label: pick a side based on the line's direction at this station,
            # plus alternate above/below to reduce overlap.
            label = ABBREV.get(st, st)
            weight = "700" if is_inter else "600"
            font_size = "10.5" if is_inter else "10"

            # Choose label placement angle by inspecting where neighbors sit.
            # For mostly-horizontal segments: alternate above/below at -32°.
            # For mostly-vertical segments (Issuing & Treasury): label to the right.
            # For arcs (Catalog & Tax, Sustainability): label outward.
            stations_in_line = ln["stations"]
            prev_pos = stations_in_line[si - 1][1] if si > 0 else None
            next_pos = stations_in_line[si + 1][1] if si + 1 < len(stations_in_line) else None
            ref = next_pos or prev_pos or (x, y)
            dx = ref[0] - x
            dy = ref[1] - y

            strategy = ln.get("label_strategy")
            if strategy == "above_rotated":
                # Always place rotated above-label, fan up-left (away from arc interior)
                offset = r + 8
                tx, ty = x, y - offset
                parts.append(
                    f'<text x="{tx}" y="{ty}" font-size="{font_size}" fill="#1A1F2C" '
                    f'text-anchor="end" font-weight="{weight}" '
                    f'transform="rotate(-32 {tx} {ty})">{html.escape(label)}</text>'
                )
                labeled.add(station_key)
                continue

            # If line moves mostly vertically here, place label to right (or left if near right edge)
            if abs(dy) > 1.6 * abs(dx):
                # Vertical segment — label to the right by default, but to the left
                # if the station is near the right canvas edge.
                if x > W - 140:
                    tx, ty = x - r - 8, y + 4
                    parts.append(
                        f'<text x="{tx}" y="{ty}" font-size="{font_size}" fill="#1A1F2C" '
                        f'text-anchor="end" font-weight="{weight}">{html.escape(label)}</text>'
                    )
                else:
                    tx, ty = x + r + 8, y + 4
                    parts.append(
                        f'<text x="{tx}" y="{ty}" font-size="{font_size}" fill="#1A1F2C" '
                        f'text-anchor="start" font-weight="{weight}">{html.escape(label)}</text>'
                    )
            else:
                # Horizontal-ish segment — alternate above/below
                above = (si % 2 == 0)
                offset = r + 8
                if above:
                    tx, ty = x, y - offset
                    parts.append(
                        f'<text x="{tx}" y="{ty}" font-size="{font_size}" fill="#1A1F2C" '
                        f'text-anchor="end" font-weight="{weight}" '
                        f'transform="rotate(-32 {tx} {ty})">{html.escape(label)}</text>'
                    )
                else:
                    tx, ty = x, y + offset + 4
                    parts.append(
                        f'<text x="{tx}" y="{ty}" font-size="{font_size}" fill="#1A1F2C" '
                        f'text-anchor="start" font-weight="{weight}" '
                        f'transform="rotate(-32 {tx} {ty})">{html.escape(label)}</text>'
                    )

            labeled.add(station_key)

    # ----- Legend: stacked at top-left in the empty corner -----
    parts.append('<g>')
    lx0 = 30
    ly0 = 95
    parts.append(
        f'<text x="{lx0}" y="{ly0}" font-size="10" font-weight="700" fill="#1A1F2C" '
        f'letter-spacing="1.5">LINES</text>'
    )
    for i, ln in enumerate(LINES):
        cy = ly0 + 18 + i * 16
        parts.append(
            f'<line x1="{lx0}" y1="{cy - 3}" x2="{lx0 + 18}" y2="{cy - 3}" '
            f'stroke="{ln["color"]}" stroke-width="5" stroke-linecap="round" />'
        )
        parts.append(
            f'<text x="{lx0 + 26}" y="{cy}" font-size="9.5" fill="#1A1F2C" '
            f'font-weight="600">{html.escape(ln["name"])}</text>'
        )
        parts.append(
            f'<text x="{lx0 + 26}" y="{cy + 10}" font-size="8.5" fill="#8A92A6">'
            f'{len(ln["stations"])} APIs</text>'
        )

    # ----- Key: bottom-left corner under the legend column -----
    kx = 30
    ky = ly0 + 18 + len(LINES) * 16 + 18
    parts.append(
        f'<text x="{kx}" y="{ky}" font-size="10" font-weight="700" fill="#1A1F2C" '
        f'letter-spacing="1.5">KEY</text>'
    )
    parts.append(
        f'<circle cx="{kx + 8}" cy="{ky + 14}" r="6" fill="#FFFFFF" '
        f'stroke="#5A6275" stroke-width="2.5" />'
    )
    parts.append(
        f'<text x="{kx + 22}" y="{ky + 18}" font-size="9.5" fill="#1A1F2C">'
        f'Station</text>'
    )
    parts.append(
        f'<circle cx="{kx + 8}" cy="{ky + 34}" r="9" fill="#FFFFFF" '
        f'stroke="#1A1F2C" stroke-width="3" />'
    )
    parts.append(
        f'<text x="{kx + 22}" y="{ky + 38}" font-size="9.5" fill="#1A1F2C" font-weight="600">'
        f'Interchange</text>'
    )
    parts.append(
        f'<text x="{kx}" y="{ky + 56}" font-size="8.5" fill="#5A6275" font-style="italic">'
        f'Hubs: Customers · Accounts · Refunds</text>'
    )
    parts.append('</g>')

    parts.append(
        f'<text x="{W-30}" y="{H-12}" text-anchor="end" font-size="8.5" fill="#8A92A6">'
        f'Source: stripe/openapi/*-openapi.yml · github.com/api-evangelist/stripe</text>'
    )

    parts.append('</svg>')
    svg = "\n".join(parts)

    html_doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>The Stripe API · Underground Map</title>
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

    out_dir = Path(__file__).resolve().parent
    (out_dir / "stripe-subway-map.svg").write_text(svg)
    (out_dir / "stripe-subway-map.html").write_text(html_doc)
    print(f"wrote {out_dir/'stripe-subway-map.svg'}")
    print(f"wrote {out_dir/'stripe-subway-map.html'}")


if __name__ == "__main__":
    main()
