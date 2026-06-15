# Stripe (stripe)

Online payment processing for internet businesses. Stripe is a suite of payment APIs that powers commerce for online businesses of all sizes.

**APIs.json:** [https://raw.githubusercontent.com/api-search/payments/main/_apis/stripe/apis.md](https://raw.githubusercontent.com/api-search/payments/main/_apis/stripe/apis.md)

## Scope

- **Position:** Consuming
- **Access:** 3rd-Party

## Tags

- Commerce
- Financial Services
- Fintech
- Payments
- T1

## Timestamps

- **Created:** 2024/04/14
- **Modified:** 2026-05-19

## APIs

### Stripe Accounts API

This is an object representing a Stripe account. You can retrieve it to see properties on the account like its current requirements or if the account is enabled to make live charges or receive payouts.

#### Tags

- Accounts

#### Properties

- [Documentation](https://stripe.com/docs/api/accounts)
- [API Reference](https://docs.stripe.com/api/accounts)
- [OpenAPI](properties/stripe-accounts-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-accounts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-accounts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Apple Pay API

Stripe users can accept Apple Pay in iOS applications in iOS 9 and above, and on the web in Safari starting with iOS 10 or macOS Sierra. There are no additional fees to process Apple Pay payments, and the pricing is the same as other card transactions.

#### Tags

- Apple
- Apply Pay
- Payments

#### Properties

- [Documentation](https://stripe.com/docs/apple-pay)
- [OpenAPI](properties/stripe-apple-pay-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-apple-pay-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-apple-pay-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Application Fees API

When you collect a transaction fee on top of a charge made for your user (using Connect), an Application Fee object is created in your account. You can list, retrieve, and refund application fees.

#### Tags

- Applications
- Fees
- Refunds

#### Properties

- [Documentation](https://stripe.com/docs/api/application_fees)
- [API Reference](https://docs.stripe.com/api/application_fees)
- [OpenAPI](properties/stripe-application-fees-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-application-fees-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-application-fees-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Application Secrets API

Secret Store is an API that allows Stripe Apps developers to securely persist secrets for use by UI Extensions and app backends.

#### Tags

- Applications
- Secrets

#### Properties

- [Documentation](https://stripe.com/docs/api/secret_management)
- [OpenAPI](openapi/stripe-application-secrets-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-application-secrets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-application-secrets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Balance API

This is an object representing your Stripe balance. You can retrieve it to see the balance currently on your Stripe account. You can also retrieve the balance history, which contains a list of transactions that contributed to the balance (charges, payouts, and so forth).

#### Tags

- Balance
- History
- Transactions

#### Properties

- [Documentation](https://stripe.com/docs/api/balance)
- [API Reference](https://docs.stripe.com/api/balance)
- [OpenAPI](openapi/stripe-balance-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-balance-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-balance-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Billing API

Create and manage subscriptions, recurring payments, and recurring revenue.

#### Tags

- Billing

#### Properties

- [Documentation](https://stripe.com/docs/billing)
- [OpenAPI](openapi/stripe-billing-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-billing-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-billing-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Charges API

The Charge object represents a single attempt to move money into your Stripe account. PaymentIntent confirmation is the most common way to create Charges, but transferring money to a different Stripe account through Connect also creates Charges. Some legacy payment flows create Charges directly, which is not recommended for new integrations.

#### Tags

- Charges
- Disputes
- Refunds

#### Properties

- [Documentation](https://stripe.com/docs/api/charges)
- [API Reference](https://docs.stripe.com/api/charges)
- [OpenAPI](openapi/stripe-charges-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-charges-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-charges-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Checkout API

Checkout is a low-code payment integration that creates a customizable form for collecting payments. You can embed Checkout directly in your website or redirect customers to a Stripe-hosted payment page. It supports one-time payments and subscriptions and accepts over 40 local payment methods.

#### Tags

- Checkout

#### Properties

- [Documentation](https://stripe.com/docs/payments/checkout)
- [OpenAPI](openapi/stripe-checkout-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-checkout-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-checkout-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Climate API

Stripe Climate is the easiest way to help promising permanent carbon removal technologies launch and scale. Join a growing group of ambitious businesses that are changing the course of carbon removal.

#### Tags

- Carbon
- Climate

#### Properties

- [Documentation](https://stripe.com/climate)
- [OpenAPI](openapi/stripe-climate-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-climate-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-climate-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Country API

Stripe needs to collect certain pieces of information about each account created. These requirements can differ depending on the account's country. The Country Specs API makes these rules available to your integration.

#### Tags

- Countries

#### Properties

- [Documentation](https://stripe.com/docs/api/country_specs)
- [OpenAPI](openapi/stripe-country-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-country-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-country-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Coupons API

A coupon contains information about a percent-off or amount-off discount you might want to apply to a customer. Coupons may be applied to subscriptions, invoices, checkout sessions, quotes, and more. Coupons do not work with conventional one-off charges or payment intents.

#### Tags

- Coupons

#### Properties

- [Documentation](https://stripe.com/docs/api/coupons)
- [OpenAPI](openapi/stripe-coupons-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-coupons-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-coupons-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Credit Notes API

Issue a credit note to adjust an invoice's amount after the invoice is finalized.

#### Tags

- Credit
- Notes

#### Properties

- [Documentation](https://stripe.com/docs/api/credit_notes)
- [OpenAPI](openapi/stripe-credit-notes-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-credit-notes-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-credit-notes-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Customers API

This object represents a customer of your business. Use it to create recurring charges and track payments that belong to the same customer.

#### Tags

- Customers

#### Properties

- [Documentation](https://stripe.com/docs/api/customers)
- [API Reference](https://docs.stripe.com/api/customers)
- [OpenAPI](openapi/stripe-customers-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-customers-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-customers-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Disputes API

A dispute occurs when a customer questions your charge with their card issuer. When this happens, you have the opportunity to respond to the dispute with evidence that shows that the charge is legitimate.

#### Tags

- Disputes

#### Properties

- [Documentation](https://stripe.com/docs/api/disputes)
- [API Reference](https://docs.stripe.com/api/disputes)
- [OpenAPI](openapi/stripe-disputes-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-disputes-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-disputes-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Ephemeral Keys API

Stripe.js uses ephemeral keys to securely retrieve Card information from the Stripe API without publicly exposing your secret keys. You need to do some of the ephemeral key exchange on the server-side to set this up.

#### Tags

- Ephemeral
- Keys

#### Properties

- [Documentation](https://stripe.com/docs/issuing/elements)
- [OpenAPI](openapi/stripe-ephemeral-keys-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-ephemeral-keys-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-ephemeral-keys-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Events API

Events are our way of letting you know when something interesting happens in your account. When an interesting event occurs, we create a new Event object.

#### Tags

- Events

#### Properties

- [Documentation](https://stripe.com/docs/api/events)
- [API Reference](https://docs.stripe.com/api/events)
- [OpenAPI](openapi/stripe-events-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Exchange Rates API

Stripe supports processing charges in 135+ currencies allowing you to present prices in a customer's native currency. Doing so can improve sales and help customers avoid conversion costs. In order to present prices in your customer's currency, you need to specify the presentment currency when creating a PaymentIntent or a charge.

#### Tags

- Exchanges
- Rates

#### Properties

- [Documentation](https://stripe.com/docs/currencies/conversions)
- [OpenAPI](openapi/stripe-exchange-rates-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-exchange-rates-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-exchange-rates-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Files API

This object represents files hosted on Stripe's servers. You can upload files with the create file request (for example, when uploading dispute evidence). Stripe also creates files independently (for example, the results of a Sigma scheduled query).

#### Tags

- Files

#### Properties

- [Documentation](https://stripe.com/docs/api/files)
- [API Reference](https://docs.stripe.com/api/files)
- [OpenAPI](openapi/stripe-files-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-files-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-files-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Financial Connections API

Financial Connections lets your users securely share their financial data by linking their financial accounts to your business. Use Financial Connections to access user-permissioned account data such as tokenized account and routing numbers, balances, ownerships details, and transactions.

#### Tags

- Connections
- Financial

#### Properties

- [Documentation](https://stripe.com/docs/financial-connections)
- [OpenAPI](openapi/stripe-financial-connections-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-financial-connections-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-financial-connections-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Identity API

Use Stripe Identity to confirm the identity of global users to prevent fraud, streamline risk operations, and increase trust and safety.

#### Tags

- Cancel
- Entities
- Identity
- Redact
- Reports
- Sessions
- Verification

#### Properties

- [Documentation](https://stripe.com/docs/identity)
- [OpenAPI](openapi/stripe-identity-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-identity-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-identity-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Invoice API

Invoices are statements of amounts owed by a customer, and are either generated one-off, or generated periodically from a subscription.

#### Tags

- Invoices

#### Properties

- [Documentation](https://stripe.com/docs/api/invoices)
- [API Reference](https://docs.stripe.com/api/invoices)
- [OpenAPI](openapi/stripe-invoice-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-invoice-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-invoice-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Issuing API

An API for businesses to instantly create, manage, and distribute payment cards.

#### Tags

- Cards
- Issuing

#### Properties

- [Documentation](https://stripe.com/docs/issuing)
- [OpenAPI](openapi/stripe-issuing-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-issuing-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-issuing-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Link API

You can use the Payment Links API to create a payment link that you can share with your customers. Stripe redirects customers who open this link to a Stripe-hosted payment page.

#### Tags

- Links
- Payments

#### Properties

- [Documentation](https://stripe.com/docs/payment-links/api)
- [OpenAPI](openapi/stripe-link-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-link-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-link-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Payment Intents API

A PaymentIntent guides you through the process of collecting a payment from your customer. We recommend that you create exactly one PaymentIntent for each order or customer session in your system. You can reference the PaymentIntent later to see the history of payment attempts for a particular session.

#### Tags

- Intent
- Intents
- Payments

#### Properties

- [Documentation](https://stripe.com/docs/api/payment_intents)
- [API Reference](https://docs.stripe.com/api/payment_intents)
- [OpenAPI](openapi/stripe-payment-intents-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-payment-intents-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-payment-intents-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Payment Links API

A payment link is a shareable URL that will take your customers to a hosted payment page. A payment link can be shared and used multiple times. When a customer opens a payment link it will open a new checkout session to render the payment page. You can use checkout session events to track payments through payment links.

#### Tags

- Link
- Links
- Payments

#### Properties

- [Documentation](https://stripe.com/docs/api/payment_links/payment_links)
- [OpenAPI](openapi/stripe-payment-links-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-payment-links-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-payment-links-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Payment Method API

The Payment Methods API allows you to accept a variety of payment methods through a single API. A PaymentMethod object contains the payment method details to create payments.

#### Tags

- Detach
- Methods
- Payments

#### Properties

- [Documentation](https://stripe.com/docs/payments/payment-methods)
- [OpenAPI](openapi/stripe-payment-method-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-payment-method-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-payment-method-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Payouts API

A Payout object is created when you receive funds from Stripe, or when you initiate a payout to either a bank account or debit card of a connected Stripe account. You can retrieve individual payouts, and list all payouts. Payouts are made on varying schedules, depending on your country and industry.

#### Tags

- Payouts

#### Properties

- [Documentation](https://stripe.com/docs/api/payouts)
- [API Reference](https://docs.stripe.com/api/payouts)
- [OpenAPI](openapi/stripe-payouts-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-payouts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-payouts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Plans API

You can now model subscriptions more flexibly using the Prices API. It replaces the Plans API and is backwards compatible to simplify your migration.

#### Tags

- Plan
- Plans

#### Properties

- [Documentation](https://stripe.com/docs/api/plans)
- [OpenAPI](openapi/stripe-plans-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-plans-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-plans-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Prices API

Prices define the unit cost, currency, and (optional) billing cycle for both recurring and one-time purchases of products. Products help you track inventory or provisioning, and prices help you track payment terms. Different physical goods or levels of service should be represented by products, and pricing options should be represented by prices. This approach lets you change prices without having to change your provisioning scheme.

#### Tags

- Prices

#### Properties

- [Documentation](https://stripe.com/docs/api/prices)
- [API Reference](https://docs.stripe.com/api/prices)
- [OpenAPI](openapi/stripe-prices-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-prices-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-prices-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Products API

Products describe the specific goods or services you offer to your customers. For example, you might offer a Standard and Premium version of your goods or service; each version would be a separate Product. They can be used in conjunction with Prices to configure pricing in Payment Links, Checkout, and Subscriptions.

#### Tags

- Products

#### Properties

- [Documentation](https://stripe.com/docs/api/products)
- [API Reference](https://docs.stripe.com/api/products)
- [OpenAPI](openapi/stripe-products-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-products-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-products-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Promotion Codes API

A Promotion Code represents a customer-redeemable code for a coupon. It can be used to create multiple codes for a single coupon.

#### Tags

- Codes
- Promotion
- Promotions

#### Properties

- [Documentation](https://stripe.com/docs/api/promotion_codes)
- [OpenAPI](openapi/stripe-promotion-codes-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-promotion-codes-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-promotion-codes-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Quotes API

A Quote is a way to model prices that you'd like to provide to a customer. Once accepted, it will automatically create an invoice, subscription or subscription schedule.

#### Tags

- Quotes

#### Properties

- [Documentation](https://stripe.com/docs/api/quotes)
- [OpenAPI](openapi/stripe-quotes-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-quotes-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-quotes-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Radar API

Stripe Radar provides real-time fraud protection and requires no additional development time. Fraud professionals can add Radar for Fraud Teams to customize protection and get deeper insights.

#### Tags

- Fraud
- Radar

#### Properties

- [Documentation](https://stripe.com/docs/radar)
- [OpenAPI](openapi/stripe-radar-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-radar-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-radar-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Refunds API

Refund objects allow you to refund a previously created charge that isn't refunded yet. Funds are refunded to the credit or debit card that's initially charged.

#### Tags

- Refunds

#### Properties

- [Documentation](https://stripe.com/docs/api/refunds)
- [API Reference](https://docs.stripe.com/api/refunds)
- [OpenAPI](openapi/stripe-refunds-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-refunds-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-refunds-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Reporting API

The financial reports in the Dashboard provide downloadable reports in CSV format for a variety of accounting and reconciliation tasks. These reports are also available through the API, so you can schedule them to run automatically or run them whenever you need to receive the associated report files for accounting purposes.

#### Tags

- Reporting
- Reports

#### Properties

- [Documentation](https://stripe.com/docs/reports/api)
- [OpenAPI](openapi/stripe-reporting-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-reporting-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-reporting-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Reviews API

Reviews can be used to supplement automated fraud detection with human expertise.

#### Tags

- Reviews

#### Properties

- [Documentation](https://stripe.com/docs/api/radar/reviews)
- [OpenAPI](openapi/stripe-reviews-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)

### Stripe Setup API

Use the Setup Intents API to set up a payment method for future payments. It's similar to a payment, but no charge is created. Set up a payment method for future payments now.

#### Tags

- Intent
- Intents
- Setup

#### Properties

- [Documentation](https://stripe.com/docs/payments/setup-intents)
- [OpenAPI](openapi/stripe-setup-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-setup-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-setup-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Shipping Rates API

Shipping rates describe the price of shipping presented to your customers and applied to a purchase.

#### Tags

- Rates
- Shipping

#### Properties

- [Documentation](https://stripe.com/docs/api/shipping_rates)
- [OpenAPI](openapi/stripe-shipping-rates-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-shipping-rates-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-shipping-rates-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Sigma API

If you have scheduled a Sigma query, you'll receive a sigma.scheduled_query_run.created webhook each time the query runs. The webhook contains a ScheduledQueryRun object, which you can use to retrieve the query results.

#### Tags

- Sigma

#### Properties

- [Documentation](https://stripe.com/docs/api/sigma/scheduled_queries)
- [OpenAPI](openapi/stripe-sigma-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-sigma-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-sigma-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Sources API

Source objects allow you to accept a variety of payment methods. They represent a customer's payment instrument, and can be used with the Stripe API just like a Card object once chargeable, they can be charged, or can be attached to customers.

#### Tags

- Sources
- Transactions

#### Properties

- [Documentation](https://stripe.com/docs/api/sources)
- [OpenAPI](openapi/stripe-sources-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-sources-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-sources-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Subscription API

Subscriptions allow you to charge a customer on a recurring basis.

#### Tags

- Recurring
- Subscriptions

#### Properties

- [Documentation](https://stripe.com/docs/api/subscriptions)
- [API Reference](https://docs.stripe.com/api/subscriptions)
- [OpenAPI](openapi/stripe-subscription-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-subscription-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-subscription-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Tax API

Automate sales tax, VAT, and GST compliance on all your transactions-low or no code integrations available.

#### Tags

- Taxes

#### Properties

- [Documentation](https://stripe.com/docs/tax)
- [OpenAPI](openapi/stripe-tax-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-tax-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-tax-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Terminal API

Use Stripe Terminal to accept in-person payments and extend Stripe payments to your point of sale.

#### Tags

- Point of Sale
- Terminal
- Terminals

#### Properties

- [Documentation](https://stripe.com/docs/terminal)
- [OpenAPI](openapi/stripe-terminal-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-terminal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-terminal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Test Helpers API

Stripe provides a number of resources for testing your integration. Make sure to test the following use cases before launch, and use our Postman collection to make the testing process simpler.

#### Tags

- Synthetic
- Testing
- Virtualization

#### Properties

- [Documentation](https://stripe.com/docs/implementation-guides/billing/testing)
- [OpenAPI](openapi/stripe-test-helpers-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-test-helpers-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-test-helpers-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Tokens API

Tokenization is the process Stripe uses to collect sensitive card or bank account details, or personally identifiable information (PII), directly from your customers in a secure manner. A token representing this information is returned to your server to use. Use our recommended payments integrations to perform this process on the client-side. This guarantees that no sensitive card data touches your server, and allows your integration to operate in a PCI-compliant way.

#### Tags

- Tokens

#### Properties

- [Documentation](https://stripe.com/docs/api/tokens)
- [API Reference](https://docs.stripe.com/api/tokens)
- [OpenAPI](openapi/stripe-tokens-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-tokens-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-tokens-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Topups API

To top up your Stripe balance, you create a top-up object. You can retrieve individual top-ups, as well as list all top-ups. Top-ups are identified by a unique, random ID.

#### Tags

- Topups

#### Properties

- [Documentation](https://stripe.com/docs/api/topups)
- [API Reference](https://docs.stripe.com/api/topups)
- [OpenAPI](openapi/stripe-topups-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-topups-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-topups-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Transfers API

A Transfer object is created when you move funds between Stripe accounts as part of Connect.

#### Tags

- Transfers

#### Properties

- [Documentation](https://stripe.com/docs/api/transfers)
- [API Reference](https://docs.stripe.com/api/transfers)
- [OpenAPI](openapi/stripe-transfers-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-transfers-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-transfers-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Treasury API

Stripe Treasury is a banking-as-a-service API that lets you embed financial services in your product. With Stripe's API, you can enable businesses to hold funds, pay bills, earn yield, and manage their cash flow. Many users build Stripe Issuing in conjunction with Stripe Treasury to attach cards to spend funds in the account.

#### Tags

- Treasury

#### Properties

- [Documentation](https://stripe.com/docs/treasury)
- [OpenAPI](openapi/stripe-treasury-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-treasury-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-treasury-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Webhook API

You can configure webhook endpoints via the API to be notified about events that happen in your Stripe account or connected accounts.

#### Tags

- Webhooks

#### Properties

- [Documentation](https://stripe.com/docs/api/webhook_endpoints)
- [API Reference](https://docs.stripe.com/api/webhook_endpoints)
- [OpenAPI](openapi/stripe-webhook-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-webhook-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-webhook-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [AsyncAPI](asyncapi/stripe-webhooks-asyncapi.yml) — [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)

### Stripe Connect API

Stripe Connect is a set of programmable APIs and tools that lets you facilitate payments on your software platform, build a marketplace, and pay out sellers or service providers globally.

#### Tags

- Connect
- Marketplaces
- Platforms

#### Properties

- [Documentation](https://docs.stripe.com/connect)
- [API Reference](https://docs.stripe.com/api/connected-accounts)
- [OpenAPI](openapi/stripe-connect-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-connect-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-connect-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Customer Portal API

The Billing customer portal is a Stripe-hosted UI for subscription and billing management. A portal session describes the instantiation of the customer portal for a particular customer. By visiting the session URL, the customer can manage their subscriptions and billing details.

#### Tags

- Billing
- Customers
- Portal
- Subscriptions

#### Properties

- [Documentation](https://docs.stripe.com/customer-management)
- [API Reference](https://docs.stripe.com/api/customer_portal)
- [OpenAPI](openapi/stripe-customer-portal-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-customer-portal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-customer-portal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Entitlements API

Entitlements enable you to map the features of your internal service to Stripe products. After you map your features, Stripe notifies you about when to provision or de-provision access according to your customers subscription status.

#### Tags

- Billing
- Entitlements
- Features

#### Properties

- [Documentation](https://docs.stripe.com/billing/entitlements)
- [API Reference](https://docs.stripe.com/api/entitlements/active-entitlement)
- [OpenAPI](openapi/stripe-entitlements-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-entitlements-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-entitlements-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Forwarding API

The Vault and Forward API allows you to tokenize and store card details in Stripes PCI-compliant vault and forward that data to supported third-party processors or endpoints.

#### Tags

- Cards
- Forwarding
- Vault

#### Properties

- [Documentation](https://docs.stripe.com/payments/vault-and-forward)
- [API Reference](https://docs.stripe.com/api/forwarding/request)
- [OpenAPI](openapi/stripe-forwarding-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-forwarding-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-forwarding-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Crypto Onramp API

The Stripe fiat-to-crypto onramp lets your customers securely purchase and exchange cryptocurrencies directly from your platform or decentralized application at checkout.

#### Tags

- Crypto
- Onramp
- Payments

#### Properties

- [Documentation](https://docs.stripe.com/crypto/onramp)
- [API Reference](https://docs.stripe.com/api/crypto/onramp_sessions)
- [OpenAPI](openapi/stripe-crypto-onramp-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-crypto-onramp-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-crypto-onramp-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Revenue Recognition API

Automate your accrual accounting process with Stripe Revenue Recognition. Import transaction data, set up rules, and download revenue reports for compliance with accounting standards like ASC 606.

#### Tags

- Accounting
- Recognition
- Revenue

#### Properties

- [Documentation](https://docs.stripe.com/revenue-recognition)
- [API Reference](https://docs.stripe.com/revenue-recognition/api)
- [OpenAPI](openapi/stripe-revenue-recognition-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-revenue-recognition-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-revenue-recognition-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Billing Meters API

Meters specify how to aggregate meter events over a billing period for usage-based pricing. Meter events represent customer actions and support up to 10,000 events per second via the V2 meter event streams API.

#### Tags

- Billing
- Meters
- Usage-Based

#### Properties

- [API Reference](https://docs.stripe.com/api/billing/meter)
- [Documentation](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-api)
- [API Reference](https://docs.stripe.com/api/v2/billing-meter)
- [API Reference](https://docs.stripe.com/api/v2/billing-meter-stream)
- [OpenAPI](openapi/stripe-billing-meters-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-billing-meters-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-billing-meters-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Stripe Payment Method Configurations API

Payment method configurations allow you to configure which payment methods are available to your customers during checkout. Manage payment method availability across multiple Connect accounts.

#### Tags

- Configuration
- Payments

#### Properties

- [API Reference](https://docs.stripe.com/api/payment_method_configurations)
- [Documentation](https://docs.stripe.com/connect/payment-method-configurations)
- [OpenAPI](openapi/stripe-payment-method-configurations-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/stripe-payment-method-configurations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/stripe-payment-method-configurations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

## Common Properties

- [Arazzo Workflows](arazzo/) — [Arazzo Specification](https://spec.openapis.org/arazzo/latest.html)
- [LinkedIn](https://www.linkedin.com/company/stripe)
- [Sign Up](https://dashboard.stripe.com/register)
- [Portal](https://dashboard.stripe.com)
- [Documentation](https://docs.stripe.com/)
- [Getting Started](https://docs.stripe.com/get-started)
- [API Reference](https://docs.stripe.com/api)
- [Authentication](https://stripe.com/docs/api/authentication)
- [Errors](https://docs.stripe.com/api/errors)
- [S D Ks](https://docs.stripe.com/sdks)
- [C L I](https://docs.stripe.com/stripe-cli)
- [Blog](https://stripe.com/blog)
- [Changelog](https://docs.stripe.com/changelog)
- [A P I  Versioning](https://docs.stripe.com/upgrades)
- [Status Page](https://status.stripe.com/)
- [Rate Limits](https://docs.stripe.com/rate-limits)
- [Security](https://docs.stripe.com/security)
- [Privacy Policy](https://stripe.com/privacy)
- [Terms of Service](https://stripe.com/legal/ssa)
- [Pricing](https://stripe.com/pricing)
- [Support](https://support.stripe.com/)
- [Discord](https://discord.com/invite/stripe)
- [GitHub Organization](https://github.com/stripe)
- [Open A P I  Source](https://github.com/stripe/openapi)
- [Postman  Workspace](https://www.postman.com/stripedev/workspace/stripe-developers/overview)
- [Node.js  S D K](https://github.com/stripe/stripe-node)
- [Python  S D K](https://github.com/stripe/stripe-python)
- [P H P  S D K](https://github.com/stripe/stripe-php)
- [Ruby  S D K](https://github.com/stripe/stripe-ruby)
- [Java  S D K](https://github.com/stripe/stripe-java)
- [Go  S D K](https://github.com/stripe/stripe-go)
- [. N E T  S D K](https://github.com/stripe/stripe-dotnet)
- [i O S  S D K](https://github.com/stripe/stripe-ios)
- [Android  S D K](https://github.com/stripe/stripe-android)
- [X ( Twitter)](https://x.com/stripe)
- [X ( Twitter)  Developer](https://x.com/StripeDev)
- [Webhooks](https://docs.stripe.com/webhooks)
- [Testing](https://docs.stripe.com/testing)
- [Expanding  Objects](https://docs.stripe.com/api/expanding_objects)
- [Pagination](https://docs.stripe.com/api/pagination)
- [Idempotent  Requests](https://docs.stripe.com/api/idempotent_requests)
- [Metadata](https://docs.stripe.com/api/metadata)
- [Stripe  Apps](https://docs.stripe.com/building-extensions/stripe-apps)
- [Marketplace](https://marketplace.stripe.com/)
- [YouTube](https://www.youtube.com/@StripeDevelopers)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/stripe-payments)
- [Website](https://stripe.com)
- [Login](https://dashboard.stripe.com/login)
- [Code  Samples](https://docs.stripe.com/samples)
- [A P I  Keys](https://docs.stripe.com/keys)
- [AsyncAPI](asyncapi/stripe-webhooks-asyncapi.yml) — [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
- [J S O N  Schema](json-schema/stripe-customer.json)
- [J S O N  Schema](json-schema/stripe-payment-intent.json)
- [J S O N  Schema](json-schema/stripe-subscription.json)
- [J S O N  Schema](json-schema/stripe-charge.json)
- [J S O N  Schema](json-schema/stripe-invoice.json)
- [J S O N  Schema](json-schema/stripe-event.json)
- [J S O N  Schema](json-schema/stripe-product.json)
- [J S O N  Schema](json-schema/stripe-price.json)
- [J S O N- L D  Context](json-ld/stripe-context.jsonld)
- [Spectral  Rules](rules/stripe-rules.yml)
- [Vocabulary](vocabulary/stripe-vocabulary.yml)
- [J S O N  Structure](json-structure/stripe-payment-intent-structure.json)
- [J S O N  Structure](json-structure/stripe-customer-structure.json)
- [J S O N  Structure](json-structure/stripe-invoice-structure.json)
- [Example](examples/stripe-create-payment-intent-example.json)
- [Example](examples/stripe-create-checkout-session-example.json)
- [Example](examples/stripe-create-customer-example.json)
- [Features](undefined)
- [Integrations](https://stripe.com/apps)
- [L L Ms Txt](https://docs.stripe.com/llms.txt)

## Maintainers

**FN:** Kin Lane
**Email:** kin@apievangelist.com
**FN:** APIs.json
**Email:** info@apis.io
**Email:** support@stripe.com
**URL:** https://stripe.com
