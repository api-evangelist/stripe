---
generated: '2026-07-17'
method: generated
name: Calculate and settle tax
description: Calculate sales tax/VAT for a set of line items, then record a Tax transaction from that calculation.
api: openapi/stripe-tax-api-openapi.yml
operations: [PostTaxCalculations, PostTaxTransactionsCreateFromCalculation]
source: >-
  Grounded in arazzo/stripe-calculate-and-settle-tax-workflow.yml; operationIds
  verified in openapi/stripe-tax-api-openapi.yml.
---

# Calculate and settle tax

Compute tax with Stripe Tax and commit it as a recorded transaction for reporting.

## Auth
- Secret key (`sk_test_` in test mode). See `authentication/stripe-authentication.yml`.

## Idempotency
- Send an `Idempotency-Key` header on each POST. See `conventions/stripe-conventions.yml`.

## Steps
1. **Calculate tax** — `PostTaxCalculations` (`POST /v1/tax/calculations`) with `currency`, `line_items[]` (each with `amount` and `reference`), and `customer_details[address]` (or a `customer`). Capture the calculation `id` and the per-line tax breakdown.
2. **Record the transaction** — `PostTaxTransactionsCreateFromCalculation` (`POST /v1/tax/transactions/create_from_calculation`) with `calculation` = the calculation id and a `reference` (your order id). This commits the tax for filing/reporting.

## Errors
- Calculations are ephemeral; create the transaction promptly after settling payment. API errors follow `errors/stripe-problem-types.yml`.

## Notes
- Use the calculation's tax amounts when charging so the amount collected matches what you record.
