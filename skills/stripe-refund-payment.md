---
generated: '2026-07-17'
method: generated
name: Refund a payment
description: Take a card payment with a PaymentIntent, then refund all or part of it.
api: openapi/stripe-refunds-api-openapi.yml
operations: [postPaymentIntents, postPaymentIntentsIntentConfirm, PostRefunds]
source: >-
  Grounded in arazzo/stripe-refund-payment-intent-workflow.yml; operationIds
  verified in openapi/stripe-payment-intents-api-openapi.yml and
  openapi/stripe-refunds-api-openapi.yml.
---

# Refund a payment

Refund a PaymentIntent fully or partially.

## Auth
- Secret key (`sk_test_` in test mode) via HTTP Basic or Bearer. See `authentication/stripe-authentication.yml`.

## Idempotency
- Send an `Idempotency-Key` header on the refund POST so a retry does not issue a second refund. See `conventions/stripe-conventions.yml`.

## Steps
1. **Create the PaymentIntent** — `postPaymentIntents` (`POST /v1/payment_intents`) with `amount`, `currency`, `payment_method` = `pm_card_visa`. Capture `pi_...`.
2. **Confirm it** — `postPaymentIntentsIntentConfirm` (`POST /v1/payment_intents/{intent}/confirm`). Wait for `status: succeeded`.
3. **Refund** — `PostRefunds` (`POST /v1/refunds`). Pass `payment_intent` = the `pi_...` id. Omit `amount` for a full refund, or pass `amount` (smallest currency unit) for a partial refund. Capture the `re_...` id; `status` is `succeeded` or `pending`.

## Errors
- `charge_already_refunded` if the payment is already fully refunded; check the charge's `amount_refunded` before retrying. API errors follow `errors/stripe-problem-types.yml`.

## Notes
- Refunds return funds to the original payment method; timing depends on the method (`conventions/stripe-conventions.yml`).
