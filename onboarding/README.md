# Programmatic API Onboarding — Stripe

A single-file, zero-dependency Node.js (18+) CLI that reproduces SoundCloud's
`sc-api-auth.mjs` pattern for Stripe: register an application / obtain credentials
programmatically instead of clicking through a dashboard, so agents and developers
can onboard at the command line.

- Script: [`stripe-api-auth.mjs`](stripe-api-auth.mjs)
- Run `node stripe-api-auth.mjs --help` for usage and the required environment variables.
- Story / rationale: https://apievangelist.com/2026/08/13/even-stripe-makes-you-click-for-api-key/

Part of the API Evangelist "Programmatic API Onboarding for the Agentic Moment" series.
