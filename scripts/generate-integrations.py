#!/usr/bin/env python3
"""Generate Naftiko v0.5 alpha2 capability YAMLs for each integration in
integrations-source.yml. Writes to temp/stripe/integrations/<slug>.yaml.

Each capability:
  - consumes both Stripe (api.stripe.com) operations + partner API operations
  - exposes a REST adapter + MCP adapter that surface the integration as
    a single coherent tool
"""
import datetime, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "integrations-source.yml"
OUT_DIR = ROOT / "integrations"


def load_yaml(p):
    import yaml
    with open(p) as f: return yaml.safe_load(f)


def dump_yaml(p, data):
    import yaml
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w") as f:
        yaml.dump(data, f, sort_keys=False, allow_unicode=True, default_flow_style=False,
                  width=10000)


def slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


# Map common Stripe op names → minimal HTTP shape. Each value is
# (method, path, description, body_required).
STRIPE_OPS = {
    "getCustomers":       ("GET",  "/v1/customers",                       "List Stripe customers",                 False),
    "getCustomer":        ("GET",  "/v1/customers/{id}",                  "Retrieve a Stripe customer",            False),
    "postCustomer":       ("POST", "/v1/customers",                       "Create a Stripe customer",              True),
    "getCharges":         ("GET",  "/v1/charges",                         "List Stripe charges",                   False),
    "getCharge":          ("GET",  "/v1/charges/{id}",                    "Retrieve a Stripe charge",              False),
    "getDispute":         ("GET",  "/v1/disputes/{id}",                   "Retrieve a Stripe dispute",             False),
    "postDispute":        ("POST", "/v1/disputes/{id}",                   "Update a Stripe dispute",               True),
    "getPaymentIntents":  ("GET",  "/v1/payment_intents",                 "List Stripe payment intents",           False),
    "getPaymentIntent":   ("GET",  "/v1/payment_intents/{id}",            "Retrieve a Stripe payment intent",      False),
    "postPaymentIntent":  ("POST", "/v1/payment_intents",                 "Create a Stripe payment intent",        True),
    "postPaymentIntentCapture": ("POST", "/v1/payment_intents/{id}/capture", "Capture a Stripe payment intent",   True),
    "getPaymentMethod":   ("GET",  "/v1/payment_methods/{id}",            "Retrieve a Stripe payment method",      False),
    "getSubscriptions":   ("GET",  "/v1/subscriptions",                   "List Stripe subscriptions",             False),
    "getSubscription":    ("GET",  "/v1/subscriptions/{id}",              "Retrieve a Stripe subscription",        False),
    "postSubscription":   ("POST", "/v1/subscriptions",                   "Create a Stripe subscription",          True),
    "postSubscriptionItemUsage": ("POST", "/v1/subscription_items/{id}/usage_records", "Report subscription metered usage", True),
    "getInvoices":        ("GET",  "/v1/invoices",                        "List Stripe invoices",                  False),
    "getInvoice":         ("GET",  "/v1/invoices/{id}",                   "Retrieve a Stripe invoice",             False),
    "getCheckoutSession": ("GET",  "/v1/checkout/sessions/{id}",          "Retrieve a Stripe Checkout session",    False),
    "getCheckoutSessions":("GET",  "/v1/checkout/sessions",               "List Stripe Checkout sessions",         False),
    "postCheckoutSession":("POST", "/v1/checkout/sessions",               "Create a Stripe Checkout session",      True),
    "getPayout":          ("GET",  "/v1/payouts/{id}",                    "Retrieve a Stripe payout",              False),
    "getPayouts":         ("GET",  "/v1/payouts",                         "List Stripe payouts",                   False),
    "getBalanceTransactions": ("GET", "/v1/balance_transactions",         "List Stripe balance transactions",      False),
    "getEvents":          ("GET",  "/v1/events",                          "List Stripe events",                    False),
}


def build_resource(name, path, op_name, method, description, body_required=False):
    op = {
        "name": op_name,
        "method": method,
        "description": description,
        "outputRawFormat": "json",
        "outputParameters": [{"name": "result", "type": "object", "value": "$."}],
        "inputParameters": [],
    }
    # path parameters
    for m in re.finditer(r"\{([^}]+)\}", path):
        op["inputParameters"].append({
            "name": m.group(1), "in": "path", "type": "string",
            "description": f"Path parameter {m.group(1)}.", "required": True,
        })
    # body if needed
    if method in ("POST", "PUT", "PATCH") or body_required:
        op["inputParameters"].append({
            "name": "body", "in": "body", "type": "object",
            "description": "Request body (JSON).", "required": body_required or method == "POST",
        })
    return {"name": name, "path": path, "operations": [op]}


def build_stripe_consume(stripe_ops):
    resources = []
    for op_key in stripe_ops:
        if op_key not in STRIPE_OPS:
            print(f"  WARN: unknown Stripe op '{op_key}', skipping", file=sys.stderr)
            continue
        method, path, desc, body_req = STRIPE_OPS[op_key]
        rname = re.sub(r"[^a-z0-9]+", "-", path.lower()).strip("-")[:60]
        resources.append(build_resource(rname, path, op_key.lower(), method, desc, body_req))
    return {
        "type": "http", "namespace": "stripe",
        "baseUri": "https://api.stripe.com",
        "description": "Stripe API operations consumed by this integration.",
        "resources": resources,
    }


def build_partner_consume(partner_slug, partner_baseUri, partner_api, partner_ops):
    resources = []
    for o in partner_ops:
        method = o["method"]
        path = o["path"]
        name = o["name"]
        rname = re.sub(r"[^a-z0-9]+", "-", path.lower()).strip("-")[:60] or partner_slug
        resources.append(build_resource(rname, path, name.lower(),
                                        method, f"{partner_api}: {name}",
                                        body_required=(method in ("POST","PUT","PATCH"))))
    return {
        "type": "http", "namespace": partner_slug,
        "baseUri": partner_baseUri,
        "description": f"{partner_api} operations consumed by this integration.",
        "resources": resources,
    }


def build_exposes(integration_slug, stripe_ops, partner_ops, partner_slug):
    """Expose ONE MCP tool that runs the integration end-to-end, plus a REST
    surface mirroring each consumed operation."""
    mcp_tools = []
    # Synthesize the lead tool from the integration name
    mcp_tools.append({
        "name": integration_slug.replace("-", "_"),
        "description": f"Execute the {integration_slug.replace('-', ' ')} integration end-to-end.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "trigger_event": {"type": "object", "description": "The triggering event payload (Stripe event or partner event)."}
            },
            "required": ["trigger_event"],
        },
    })
    return [
        {
            "type": "mcp", "namespace": f"{integration_slug}-mcp",
            "description": f"MCP adapter for the {integration_slug} integration.",
            "tools": mcp_tools,
        },
        {
            "type": "rest", "namespace": f"{integration_slug}-rest",
            "port": 8080,
            "description": f"REST adapter for the {integration_slug} integration.",
            "resources": [{
                "path": f"/{integration_slug}",
                "name": integration_slug,
                "description": f"REST surface for the {integration_slug} integration.",
                "operations": [{
                    "method": "POST",
                    "name": "trigger",
                    "description": f"Trigger the {integration_slug} integration.",
                    "call": f"{integration_slug.replace('-', '_')}",
                    "with": {"trigger_event": "rest.body"},
                    "outputParameters": [{"type": "object", "mapping": "$."}],
                }],
            }],
        },
    ]


def build_capability(entry):
    integration_slug = f"stripe-{entry['partner']}"
    today = datetime.date.today().isoformat()

    stripe_consume = build_stripe_consume(entry["stripe_ops"])
    partner_consume = build_partner_consume(
        entry["partner"], entry["partner_baseUri"],
        entry["partner_api"], entry["partner_ops"],
    )
    exposes = build_exposes(integration_slug, entry["stripe_ops"], entry["partner_ops"], entry["partner"])

    cap = {
        "naftiko": "1.0.0-alpha2",
        "info": {
            "label": entry["name"],
            "description": entry["use_case"],
            "tags": ["Stripe", "Integration", entry["category"], entry["partner"]],
            "created": today,
            "modified": today,
        },
        "binds": [
            {"namespace": "env", "keys": {
                "STRIPE_API_KEY": "STRIPE_API_KEY",
                f"{entry['partner'].upper().replace('-','_')}_API_KEY":
                    f"{entry['partner'].upper().replace('-','_')}_API_KEY",
            }},
        ],
        "capability": {
            "consumes": [stripe_consume, partner_consume],
            "exposes": exposes,
        },
    }
    return integration_slug, cap


def main():
    if not SOURCE.exists():
        sys.exit(f"Missing {SOURCE}")
    entries = load_yaml(SOURCE) or []
    print(f"Loaded {len(entries)} integration entries")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    n = 0
    index = []
    for entry in entries:
        slug, cap = build_capability(entry)
        out = OUT_DIR / f"{slug}.yaml"
        dump_yaml(out, cap)
        index.append({
            "slug": slug, "label": entry["name"], "partner": entry["partner"],
            "category": entry["category"], "use_case": entry["use_case"],
        })
        n += 1
    # Write integrations index
    dump_yaml(OUT_DIR / "_index.yml", index)
    print(f"Wrote {n} integration capability YAMLs → {OUT_DIR}")
    print(f"Wrote index → {OUT_DIR / '_index.yml'}")


if __name__ == "__main__":
    main()
