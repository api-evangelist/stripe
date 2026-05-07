#!/usr/bin/env python3
"""Build a tube-style map of the Stripe API.

Each Stripe OpenAPI file is a station; APIs are grouped onto colored lines that
mirror Stripe's product taxonomy (Payments, Billing, Connect, etc.).

Lines are rendered as smooth cubic Bezier curves through hand-placed waypoints
so the map has the bends, arcs, and crossings of a real underground map.
Labels use collision-aware placement: for every station we try several candidate
positions (above-rotated, below-rotated, left-horizontal, right-horizontal) and
pick the one with the most surrounding whitespace.

Outputs an HTML file with embedded SVG (for browser viewing + printing) at
8.5x11 in landscape orientation, plus a standalone SVG.
"""

import html
import math
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
# Collision-aware label placement
# ---------------------------------------------------------------------------

def text_extent(label, font_size):
    """Approximate width/height of a rendered label."""
    return len(label) * font_size * 0.55, font_size * 1.1


def _rotate(corners, cx, cy, deg):
    rad = math.radians(deg)
    c, s = math.cos(rad), math.sin(rad)
    return [(cx + (px - cx) * c - (py - cy) * s,
             cy + (px - cx) * s + (py - cy) * c) for (px, py) in corners]


def make_candidate(x, y, label, font_size, station_radius,
                   side, distance, angle):
    """Generate a candidate label placement.

    side: 'above', 'below', 'left', 'right'
    distance: pixels from station edge
    angle: rotation in degrees (0 = horizontal, -32 = tilted up to the right)
    Returns (anchor_x, anchor_y, anchor, rotation, polygon).
    """
    w, h = text_extent(label, font_size)
    pad = station_radius + distance

    if side == "above":
        # text-anchor=end -> text fans up-LEFT
        ax, ay = x, y - pad
        c0 = [(ax - w, ay - h / 2), (ax, ay - h / 2),
              (ax, ay + h / 2), (ax - w, ay + h / 2)]
        anchor = "end"
        return ax, ay, anchor, angle, _rotate(c0, ax, ay, angle)
    if side == "above_right":
        # text-anchor=start -> text fans up-RIGHT
        ax, ay = x, y - pad
        c0 = [(ax, ay - h / 2), (ax + w, ay - h / 2),
              (ax + w, ay + h / 2), (ax, ay + h / 2)]
        return ax, ay, "start", angle, _rotate(c0, ax, ay, angle)
    if side == "below":
        ax, ay = x, y + pad + h * 0.4
        c0 = [(ax, ay - h / 2), (ax + w, ay - h / 2),
              (ax + w, ay + h / 2), (ax, ay + h / 2)]
        return ax, ay, "start", angle, _rotate(c0, ax, ay, angle)
    if side == "below_left":
        ax, ay = x, y + pad + h * 0.4
        c0 = [(ax - w, ay - h / 2), (ax, ay - h / 2),
              (ax, ay + h / 2), (ax - w, ay + h / 2)]
        return ax, ay, "end", angle, _rotate(c0, ax, ay, angle)
    if side == "right":
        ax, ay = x + pad, y + 4
        c0 = [(ax, ay - h / 2), (ax + w, ay - h / 2),
              (ax + w, ay + h / 2), (ax, ay + h / 2)]
        return ax, ay, "start", 0, c0
    if side == "left":
        ax, ay = x - pad, y + 4
        c0 = [(ax - w, ay - h / 2), (ax, ay - h / 2),
              (ax, ay + h / 2), (ax - w, ay + h / 2)]
        return ax, ay, "end", 0, c0
    if side == "above_h":
        # horizontal above (centered)
        ax, ay = x, y - pad
        c0 = [(ax - w / 2, ay - h / 2), (ax + w / 2, ay - h / 2),
              (ax + w / 2, ay + h / 2), (ax - w / 2, ay + h / 2)]
        return ax, ay, "middle", 0, c0
    if side == "below_h":
        ax, ay = x, y + pad + h * 0.4
        c0 = [(ax - w / 2, ay - h / 2), (ax + w / 2, ay - h / 2),
              (ax + w / 2, ay + h / 2), (ax - w / 2, ay + h / 2)]
        return ax, ay, "middle", 0, c0
    raise ValueError(side)


def generate_candidates(x, y, label, font_size, station_radius):
    """Generate a wide set of candidate label placements at varying
    distances, sides, and angles. Returns list of (kind_label, anchor_x,
    anchor_y, anchor, rotation, polygon).
    """
    out = []
    # Primary tilted-rotation candidates (±32°)
    for distance in (8, 14, 22):
        for side in ("above", "above_right", "below", "below_left"):
            for angle in (-32, -20, -45):
                ax, ay, an, rot, poly = make_candidate(
                    x, y, label, font_size, station_radius, side, distance, angle
                )
                out.append((f"{side}@{distance}rot{angle}", ax, ay, an, rot, poly))
    # Pure horizontal candidates at multiple sides + distances
    for distance in (8, 14, 22, 36, 50):
        for side in ("above_h", "below_h", "right", "left"):
            ax, ay, an, rot, poly = make_candidate(
                x, y, label, font_size, station_radius, side, distance, 0
            )
            out.append((f"{side}@{distance}", ax, ay, an, rot, poly))
    return out


def _bbox(corners):
    xs = [c[0] for c in corners]
    ys = [c[1] for c in corners]
    return (min(xs), min(ys), max(xs), max(ys))


def _boxes_overlap(b1, b2, expand=0):
    return not (b1[2] + expand < b2[0] or b2[2] + expand < b1[0]
                or b1[3] + expand < b2[1] or b2[3] + expand < b1[1])


def _segments_intersect(p1, p2, p3, p4):
    """Return True iff line segment p1->p2 crosses segment p3->p4."""
    def ccw(a, b, c):
        return (c[1] - a[1]) * (b[0] - a[0]) > (b[1] - a[1]) * (c[0] - a[0])
    return (ccw(p1, p3, p4) != ccw(p2, p3, p4) and
            ccw(p1, p2, p3) != ccw(p1, p2, p4))


def _point_in_poly(pt, poly):
    """Standard ray-casting point-in-polygon test."""
    x, y = pt
    inside = False
    n = len(poly)
    j = n - 1
    for i in range(n):
        xi, yi = poly[i]
        xj, yj = poly[j]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / ((yj - yi) or 1e-9) + xi):
            inside = not inside
        j = i
    return inside


def _seg_crosses_polygon(seg, poly):
    """True if line segment intersects (or is fully inside) the polygon."""
    p1, p2 = seg
    if _point_in_poly(p1, poly) or _point_in_poly(p2, poly):
        return True
    n = len(poly)
    for i in range(n):
        a = poly[i]
        b = poly[(i + 1) % n]
        if _segments_intersect(p1, p2, a, b):
            return True
    return False


def _polygons_overlap(p1, p2):
    """True if two convex polygons overlap (cheap conservative check)."""
    return _boxes_overlap(_bbox(p1), _bbox(p2), expand=2)


def score_box(poly, this_xy, all_stations, all_segments_other, placed_label_polys,
              static_obstacles):
    """Lower score = better label position.

    Line crossings are treated as a *hard* rejection (5000+ penalty), so the
    optimizer will only accept a line-crossing label if literally no other
    candidate is available.

    poly is a list of 4 (x, y) rotated corner points.
    """
    score = 0
    bb = _bbox(poly)
    bx1, by1, bx2, by2 = bb

    # Off-canvas penalty (hard)
    if bx1 < 6 or by1 < 6 or bx2 > W - 6 or by2 > H - 6:
        score += 8000

    # Reserved areas (legend, key, title) — hard
    for ob in static_obstacles:
        if _boxes_overlap(bb, ob, expand=4):
            score += 6000

    # Other lines crossing the rotated label polygon — HARD rejection
    crossings = 0
    for seg in all_segments_other:
        if _seg_crosses_polygon(seg, poly):
            crossings += 1
    score += crossings * 5000

    # Overlap with already-placed label polygons (still hard but smaller)
    for pp in placed_label_polys:
        if _polygons_overlap(poly, pp):
            score += 800

    # Stations falling inside (or near) the label polygon
    for (sx, sy) in all_stations:
        if (sx, sy) == this_xy:
            continue
        if bx1 - 6 <= sx <= bx2 + 6 and by1 - 6 <= sy <= by2 + 6:
            if _point_in_poly((sx, sy), poly):
                score += 1200
            else:
                score += 80  # near-miss

    # Mild preference for closer-to-station labels (encourages compactness when
    # multiple positions are equally valid)
    cx = (bx1 + bx2) / 2
    cy = (by1 + by2) / 2
    dist_to_station = math.hypot(cx - this_xy[0], cy - this_xy[1])
    score += dist_to_station * 0.4

    return score


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

    # ------------------------------------------------------------------
    # Build obstacle data for collision-aware label placement
    # ------------------------------------------------------------------
    # All station centers (one entry per unique x,y — interchanges are deduped)
    all_station_xy = list({(x, y) for ln in LINES for (_, (x, y)) in ln["stations"]})

    # All segments per line (used to detect labels crossing OTHER lines).
    # Densely sample the actual Catmull-Rom curve so collision detection
    # matches the *rendered* line, not the straight-segment proxy.
    def sample_catmull_rom(points, samples_per_segment=10, tension=0.6):
        """Return list of (x,y) points sampled along the smooth curve."""
        if len(points) < 2:
            return list(points)
        out = [points[0]]
        n = len(points)
        for i in range(n - 1):
            p0 = points[i - 1] if i > 0 else points[i]
            p1 = points[i]
            p2 = points[i + 1]
            p3 = points[i + 2] if i + 2 < n else p2
            for k in range(1, samples_per_segment + 1):
                t = k / samples_per_segment
                # Catmull-Rom in cubic Bezier control points form
                # P(t) = (1-t)^3 p1 + 3(1-t)^2 t cp1 + 3(1-t) t^2 cp2 + t^3 p2
                cp1 = (p1[0] + (p2[0] - p0[0]) * tension / 3,
                       p1[1] + (p2[1] - p0[1]) * tension / 3)
                cp2 = (p2[0] - (p3[0] - p1[0]) * tension / 3,
                       p2[1] - (p3[1] - p1[1]) * tension / 3)
                u = 1 - t
                bx = u**3 * p1[0] + 3*u*u*t*cp1[0] + 3*u*t*t*cp2[0] + t**3 * p2[0]
                by = u**3 * p1[1] + 3*u*u*t*cp1[1] + 3*u*t*t*cp2[1] + t**3 * p2[1]
                out.append((bx, by))
        return out

    segments_by_line = []
    for ln in LINES:
        pts = [pos for (_, pos) in ln["stations"]]
        sampled = sample_catmull_rom(pts, samples_per_segment=12, tension=0.6)
        segs = [(sampled[i], sampled[i + 1]) for i in range(len(sampled) - 1)]
        segments_by_line.append(segs)

    # Reserved zones (legend column on the left, title at the top)
    static_obstacles = [
        (10, 0, 220, 80),                  # title
        (10, 85, 220, 320),                # legend + key column on the left
        (W - 50, H - 25, W, H),            # source line bottom-right
    ]

    # Collect placed label polygons as we go so subsequent labels don't overlap them
    placed_label_polys = []
    # Track which interchange names we've already drawn (one circle + one label each)
    drawn_inter = set()

    # Order: place interchange stations FIRST so they get the best placement,
    # then go line by line.
    iter_order = []
    for li, ln in enumerate(LINES):
        for si, (st, pos) in enumerate(ln["stations"]):
            iter_order.append((st in interchange_names, li, si))
    # Stable sort so interchanges (True) come first
    iter_order.sort(key=lambda t: (not t[0], t[1], t[2]))

    for is_inter_first, li, si in iter_order:
        ln = LINES[li]
        st, (x, y) = ln["stations"][si]
        is_inter = st in interchange_names
        r = INTERCHANGE_R if is_inter else STATION_R
        ring = "#1A1F2C" if is_inter else ln["color"]
        ring_w = INTERCHANGE_RING_W if is_inter else STATION_RING_W

        if is_inter and st in drawn_inter:
            continue  # already drawn (circle + label) on the first line we saw

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

        label = ABBREV.get(st, st)
        weight = "700" if is_inter else "600"
        font_size_n = 10.5 if is_inter else 10

        # Build the segment list against which this label must not cross.
        # All other lines are forbidden. The own line is forbidden EXCEPT the
        # segments immediately adjacent to this station (so a label perpendicular
        # to its own line is fine close in).
        own_segs = segments_by_line[li]
        # Find segments whose endpoints are within ~30px of this station — these
        # are local enough that a perpendicular label would naturally cross them.
        own_local = []
        own_far = []
        for s in own_segs:
            (ax_s, ay_s), (bx_s, by_s) = s
            d_a = math.hypot(ax_s - x, ay_s - y)
            d_b = math.hypot(bx_s - x, by_s - y)
            if min(d_a, d_b) < 32:
                own_local.append(s)
            else:
                own_far.append(s)

        forbidden_segments = own_far + [
            s for ll in range(len(LINES)) if ll != li for s in segments_by_line[ll]
        ]

        scored = []
        for tag, ax, ay, anchor, rot, poly in generate_candidates(
                x, y, label, font_size_n, r):
            s = score_box(poly, (x, y), all_station_xy, forbidden_segments,
                          placed_label_polys, static_obstacles)
            scored.append((s, tag, ax, ay, anchor, rot, poly))

        scored.sort(key=lambda t: t[0])
        best_score, best_tag, ax, ay, anchor, rot, poly = scored[0]
        placed_label_polys.append(poly)

        # Render the chosen label
        rot_attr = f' transform="rotate({rot} {ax} {ay})"' if rot else ''
        parts.append(
            f'<text x="{ax}" y="{ay}" font-size="{font_size_n}" fill="#1A1F2C" '
            f'text-anchor="{anchor}" font-weight="{weight}"{rot_attr}>'
            f'{html.escape(label)}</text>'
        )

        if is_inter:
            drawn_inter.add(st)

    # ----- Legend: stacked at top-left in the empty corner -----
    parts.append('<g>')
    lx0 = 30
    ly0 = 95
    parts.append(
        f'<text x="{lx0}" y="{ly0}" font-size="10" font-weight="700" fill="#1A1F2C" '
        f'letter-spacing="1.5">LINES</text>'
    )
    for i, ln in enumerate(LINES):
        cy = ly0 + 18 + i * 18
        parts.append(
            f'<line x1="{lx0}" y1="{cy - 3}" x2="{lx0 + 18}" y2="{cy - 3}" '
            f'stroke="{ln["color"]}" stroke-width="5" stroke-linecap="round" />'
        )
        parts.append(
            f'<text x="{lx0 + 26}" y="{cy}" font-size="10" fill="#1A1F2C" '
            f'font-weight="600">{html.escape(ln["name"])}</text>'
        )

    # ----- Key: bottom-left corner under the legend column -----
    kx = 30
    ky = ly0 + 18 + len(LINES) * 18 + 18
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
