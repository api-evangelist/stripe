#!/usr/bin/env python3
"""Build the Stripe API tube-style map.

Defines Stripe's product taxonomy as colored subway lines and hand-places
each station's coordinates so the lines have real metro-map shapes (arcs,
L-shapes, vertical branches). The shared rendering engine in
`.claude/skills/_subway_engine.py` handles SVG output and collision-aware
label placement.
"""

import sys
from pathlib import Path

# Import the shared engine
sys.path.insert(0, "/Users/kinlane/GitHub/all/.claude/skills")
from _subway_engine import build_subway  # noqa: E402

ABBREV = {
    "Payment Method Configurations": "PM Configurations",
    "Application Secrets": "App Secrets",
    "Application Fees": "App Fees",
}

# Three interchange hubs anchor the map. Their (x,y) is shared across every
# line they belong to so transfer markers collapse cleanly.
HUBS = {
    "Customers": (240, 330),
    "Accounts":  (240, 600),
    "Refunds":   (940, 330),
}

LINES = [
    {
        "name": "Checkout & Links",
        "color": "#7B3FE4",
        "stations": [
            ("Crypto Onramp",   (300, 140)),
            ("Link",            (440, 110)),
            ("Customer Portal", (580, 100)),
            ("Payment Links",   (720, 110)),
            ("Checkout",        (860, 140)),
        ],
    },
    {
        "name": "Payments",
        "color": "#E0245E",
        "stations": [
            ("Customers",                     HUBS["Customers"]),
            ("Tokens",                        (320, 330)),
            ("Sources",                       (390, 330)),
            ("Apple Pay",                     (470, 330)),
            ("Payment Methods",               (550, 330)),
            ("Payment Method Configurations", (640, 330)),
            ("Setup",                         (720, 330)),
            ("Payment Intents",               (800, 330)),
            ("Charges",                       (870, 330)),
            ("Refunds",                       HUBS["Refunds"]),
        ],
    },
    {
        "name": "Billing — Core",
        "color": "#0E9D6E",
        "stations": [
            ("Customers",      HUBS["Customers"]),
            ("Invoice",        (240, 400)),
            ("Subscription",   (240, 460)),
            ("Plans",          (300, 510)),
            ("Prices",         (370, 510)),
            ("Products",       (440, 510)),
            ("Billing",        (510, 510)),
            ("Billing Meters", (580, 510)),
        ],
    },
    {
        "name": "Billing — Catalog & Tax",
        "color": "#0B7956",
        "stations": [
            ("Coupons",             (650, 510)),
            ("Promotion Codes",     (720, 510)),
            ("Credit Notes",        (790, 510)),
            ("Quotes",              (855, 490)),
            ("Shipping Rates",      (905, 455)),
            ("Tax",                 (945, 415)),
            ("Entitlements",        (970, 370)),
            ("Revenue Recognition", (990, 320)),
        ],
    },
    {
        "name": "Connect",
        "color": "#E68B1F",
        "stations": [
            ("Accounts",            HUBS["Accounts"]),
            ("Connect",             (320, 600)),
            ("Application Fees",    (400, 600)),
            ("Application Secrets", (490, 600)),
            ("Transfers",           (570, 600)),
            ("Payouts",             (650, 600)),
            ("Topups",              (730, 600)),
            ("Balance",             (810, 600)),
        ],
    },
    {
        "name": "Issuing & Treasury",
        "color": "#1E5BD0",
        "stations": [
            ("Accounts",              HUBS["Accounts"]),
            ("Issuing",               (240, 660)),
            ("Treasury",              (240, 720)),
            ("Financial Connections", (240, 780)),
        ],
    },
    {
        "name": "Risk & Disputes",
        "color": "#C5318B",
        "stations": [
            ("Identity", (470, 730)),
            ("Radar",    (610, 720)),
            ("Reviews",  (740, 680)),
            ("Disputes", (860, 600)),
            ("Refunds",  HUBS["Refunds"]),
        ],
    },
    {
        "name": "Reporting & Data",
        "color": "#5A6275",
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
        "stations": [
            ("Climate",      (1015, 590)),
            ("Forwarding",   (1045, 650)),
            ("Terminal",     (1045, 720)),
            ("Test Helpers", (1010, 780)),
        ],
    },
]


def main():
    seen = set()
    n_unique = 0
    for ln in LINES:
        for (st, _) in ln["stations"]:
            if st not in seen:
                n_unique += 1
                seen.add(st)

    # Stations whose API slug doesn't follow the simple plural-name convention.
    # All other stations use the default {provider_id}-{slug(name)}-api template.
    overrides = {
        "Payment Methods": "https://apis.apis.io/apis/stripe/stripe-payment-method-api/",
    }

    build_subway(
        title="The Stripe API · Underground Map",
        subtitle=f"{n_unique} APIs · {len(LINES)} functional lines · "
                 f"Customers, Accounts & Refunds are interchange hubs · "
                 f"click any station for the apis.io page",
        lines=LINES,
        hubs=HUBS,
        abbrev=ABBREV,
        source_label="Source: stripe/openapi/*-openapi.yml · github.com/api-evangelist/stripe",
        out_dir=Path(__file__).resolve().parent,
        out_basename="stripe-subway-map",
        provider_id="stripe",
        station_url_overrides=overrides,
    )


if __name__ == "__main__":
    main()
