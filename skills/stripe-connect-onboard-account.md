---
generated: '2026-07-17'
method: generated
name: Onboard a Connect account
description: Create a Stripe Connect connected account and mint a hosted onboarding link.
api: openapi/stripe-connect-api-openapi.yml
operations: [PostAccounts, PostAccountLinks]
source: >-
  Grounded in arazzo/stripe-connect-onboard-account-workflow.yml; operationIds
  verified in openapi/stripe-connect-api-openapi.yml.
---

# Onboard a Connect account

Bring a seller/platform participant onto Stripe Connect with Stripe-hosted onboarding.

## Auth
- Platform secret key (`sk_test_` in test mode). See `authentication/stripe-authentication.yml`.

## Idempotency
- Send an `Idempotency-Key` header on each POST. See `conventions/stripe-conventions.yml`.

## Steps
1. **Create the connected account** — `PostAccounts` (`POST /v1/accounts`) with `type` (e.g. `express` or `standard`), `country`, and `email`. Capture the `acct_...` id.
2. **Create the account link** — `PostAccountLinks` (`POST /v1/account_links`) with `account` = `acct_...`, `type` = `account_onboarding`, and `refresh_url` / `return_url`. Redirect the user to the returned `url` to complete KYC.

## Errors
- Account links are single-use and short-lived; if the user returns via `refresh_url`, mint a fresh link. API errors follow `errors/stripe-problem-types.yml`.

## Notes
- Check `account.requirements` and `charges_enabled` / `payouts_enabled` after onboarding to confirm the account is fully verified before routing funds.
