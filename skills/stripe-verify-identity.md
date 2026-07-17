---
generated: '2026-07-17'
method: generated
name: Verify a user's identity
description: Start a Stripe Identity verification session and poll it until the identity check completes.
api: openapi/stripe-identity-api-openapi.yml
operations: [postIdentityVerificationSessions, getIdentityVerificationSessionsSession]
source: >-
  Grounded in arazzo/stripe-verify-identity-workflow.yml; operationIds verified
  in openapi/stripe-identity-api-openapi.yml.
---

# Verify a user's identity

Run a KYC/document check with Stripe Identity.

## Auth
- Secret key (`sk_test_` in test mode). See `authentication/stripe-authentication.yml`.

## Idempotency
- Send an `Idempotency-Key` header on the create POST. See `conventions/stripe-conventions.yml`.

## Steps
1. **Create the verification session** — `postIdentityVerificationSessions` (`POST /v1/identity/verification_sessions`) with `type` = `document` (or `id_number`). Capture the `vs_...` id and redirect the user to the returned hosted `url` (or use the `client_secret` in the client SDK).
2. **Poll the session** — `getIdentityVerificationSessionsSession` (`GET /v1/identity/verification_sessions/{session}`) with the `vs_...` id until `status` is `verified` (or `requires_input` / `canceled`). Prefer reacting to the `identity.verification_session.verified` webhook over tight polling; see `asyncapi/stripe-webhooks-asyncapi.yml`.

## Errors
- `requires_input` means the user must resubmit; surface `last_error` to guide them. API errors follow `errors/stripe-problem-types.yml`.

## Notes
- Verified outputs (`verified_outputs`) are only readable when the session reaches `verified`.
