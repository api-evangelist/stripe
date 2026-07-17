---
generated: '2026-07-17'
method: generated
name: Launch a recurring subscription
description: Create a product and recurring price, attach a customer, and start a subscription.
api: openapi/stripe-subscription-api-openapi.yml
operations: [PostProducts, postPrices, postCustomers, PostSubscriptions]
source: >-
  Grounded in arazzo/stripe-launch-subscription-workflow.yml; operationIds
  verified in openapi/stripe-products-api-openapi.yml,
  openapi/stripe-prices-api-openapi.yml, openapi/stripe-customers-api-openapi.yml
  and openapi/stripe-subscription-api-openapi.yml.
---

# Launch a recurring subscription

Stand up a product catalog entry and bill a customer on a recurring cycle.

## Auth
- Secret key (`sk_test_` in test mode). See `authentication/stripe-authentication.yml`.

## Idempotency
- Send an `Idempotency-Key` header on each POST. See `conventions/stripe-conventions.yml`.

## Steps
1. **Create the product** — `PostProducts` (`POST /v1/products`) with `name`. Capture `prod_...`.
2. **Create a recurring price** — `postPrices` (`POST /v1/prices`) with `product` = `prod_...`, `unit_amount`, `currency`, and `recurring[interval]` = `month`. Capture `price_...`.
3. **Create the customer** — `postCustomers` (`POST /v1/customers`) with `email` and a `payment_method` (test: `pm_card_visa`), setting it as the default via `invoice_settings[default_payment_method]`. Capture `cus_...`.
4. **Create the subscription** — `PostSubscriptions` (`POST /v1/subscriptions`) with `customer` = `cus_...` and `items[0][price]` = `price_...`. On success `status` is `active` (or `trialing`).

## Errors
- If the first invoice payment fails, the subscription enters `incomplete`; resolve via the latest invoice's PaymentIntent. See `errors/stripe-decline-codes.yml` and `errors/stripe-problem-types.yml`.

## Notes
- Prices are immutable; to change pricing, create a new Price and update the subscription item.
