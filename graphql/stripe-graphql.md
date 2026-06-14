# Stripe GraphQL

## Description

Stripe does not offer a public GraphQL API. Its developer-facing surface is entirely REST-based
(`https://api.stripe.com/v1/`), with JSON responses, OpenAPI specifications, and official SDKs for
Node.js, Python, PHP, Ruby, Java, Go, and .NET.

Internally, Stripe's engineering teams use GraphQL for service-to-service communication and
tooling, but this infrastructure is not accessible to external developers. There have been no
public announcements of a planned public GraphQL endpoint as of mid-2026.

The schema file in this directory (`stripe-schema.graphql`) is a **conceptual SDL representation**
derived directly from Stripe's extensively documented REST data model. Every type, field, and
relationship maps 1-to-1 to objects and fields described in the official Stripe API reference
(`https://docs.stripe.com/api`). It can be used for:

- API design reference and data-model exploration
- Code-generation tooling that targets GraphQL types
- Schema stitching or federation gateways that wrap the Stripe REST API
- Documentation, training, and educational purposes
- Building a GraphQL-over-REST proxy (e.g., using StepZen, Hasura, or a custom Apollo Server)

## Endpoint

No public GraphQL endpoint exists. REST base URL: `https://api.stripe.com/v1/`

## Authentication

Stripe uses HTTP Basic Auth with a secret API key as the username and an empty password:

```
Authorization: Basic <base64(sk_live_...>:)>
```

Alternatively, pass the key as a Bearer token:

```
Authorization: Bearer sk_live_...
```

Keys are created in the Stripe Dashboard under **Developers > API keys**. Restricted keys can
limit access to specific resources. For webhook signature verification, Stripe signs payloads with
a `Stripe-Signature` header using HMAC-SHA256.

## Notes

- **Conceptual schema only.** All types in `stripe-schema.graphql` are derived from the REST API
  data model. Field names follow the Stripe REST convention (snake_case mapped to camelCase where
  idiomatic for GraphQL).
- **Pagination.** Stripe REST uses cursor-based list objects (`has_more`, `starting_after`,
  `ending_before`). These are represented via a generic `StripeList` wrapper type in the schema.
- **Expandable objects.** Many Stripe fields can be expanded from an ID string into the full
  object via `?expand[]=field`. The schema models these as the full object type rather than a
  union, which reflects the expanded state.
- **Metadata.** Most Stripe objects accept a `metadata` key-value map (up to 50 keys, 500 chars
  each). This is represented as a `JSON` scalar in the schema.
- **Versioning.** Stripe versions its API by date (`Stripe-Version` header). The schema reflects
  the 2024-2025 object model. The v2 API (meter event streams) introduces a slightly different
  structure documented separately.
- **Sources.** Stripe REST API reference: https://docs.stripe.com/api | Stripe OpenAPI spec:
  https://github.com/stripe/openapi
