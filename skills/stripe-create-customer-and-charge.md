---
generated: '2026-07-17'
method: generated
name: Create a customer and charge them
description: Create a Stripe customer, open a PaymentIntent for them, and confirm it to take a card payment in test mode.
api: openapi/stripe-payment-intents-api-openapi.yml
operations: [postCustomers, postPaymentIntents, postPaymentIntentsIntentConfirm]
source: >-
  Grounded in arazzo/stripe-create-customer-and-pay-workflow.yml and the
  conventions in conventions/stripe-conventions.yml; operationIds verified in
  openapi/stripe-customers-api-openapi.yml and
  openapi/stripe-payment-intents-api-openapi.yml.
---

# Create a customer and charge them

Use this to take a one-time card payment attached to a saved customer.

## Auth
- HTTP Basic with your secret key as the username, empty password (or `Authorization: Bearer sk_test_...`). See `authentication/stripe-authentication.yml`.
- Use a **test** key (`sk_test_`) while developing. Test vs live is chosen by the key, not a URL. See `sandbox/stripe-sandbox.yml`.

## Idempotency (required for the write steps)
- Send an `Idempotency-Key` header (a client-generated UUID v4) on every POST so a retried request does not double-charge. Keys are retained 24h; replaying returns the original response. See `conventions/stripe-conventions.yml`.

## Steps
1. **Create the customer** — `postCustomers` (`POST /v1/customers`). Pass `email` and any `name`/`metadata`. Capture the returned `id` (`cus_...`).
2. **Create the PaymentIntent** — `postPaymentIntents` (`POST /v1/payment_intents`). Pass `amount` (in the smallest currency unit, e.g. `2000` = $20.00), `currency`, `customer` = the `cus_...` id, and `payment_method` (in test mode use `pm_card_visa`). Capture the returned `id` (`pi_...`).
3. **Confirm the PaymentIntent** — `postPaymentIntentsIntentConfirm` (`POST /v1/payment_intents/{intent}/confirm`) with the `pi_...` id. On success `status` is `succeeded`.

## Errors
- Card failures surface as a `card_error` with a `decline_code`; see `errors/stripe-decline-codes.yml`. API-level problems use the Stripe error envelope in `errors/stripe-problem-types.yml`.
- On `authentication_required`, complete the returned `next_action` (3DS) before the intent can succeed.

## Test values
- Card that always succeeds: `pm_card_visa`. Card that triggers a decline: `pm_card_chargeDeclined`. See `sandbox/stripe-sandbox.yml`.
