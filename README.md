# Stripe (stripe)
Online payment processing for internet businesses. Stripe is a suite of payment APIs that powers commerce for online businesses of all sizes.

**URL:** [Visit APIs.json URL](https://raw.githubusercontent.com/api-search/payments/main/_apis/stripe/apis.md)

## Scope

- **Type:** Contract 
- **Position:** Consuming 
- **Access:** 3rd-Party 

## Tags:

 - API, Commerce, Financial Services, Fintech, Payments, T1

## Timestamps

- **Created:** 2024/04/14 
- **Modified:** 2025-12-27 

## APIs

### Stripe Accounts API
This is an object representing a Stripe account. You can retrieve it to see properties on the account like its current requirements or if the account is enabled to make live charges or receive payouts.


#### Tags:

 - Accounts

#### Properties

- [Documentation](https://stripe.com/docs/api/accounts)
- [OpenAPI](properties/stripe-accounts-api-openapi.yml)

### Stripe Apple Pay API
Stripe users can accept Apple Pay in iOS applications in iOS 9 and above, and on the web in Safari starting with iOS 10 or macOS Sierra. There are no additional fees to process Apple Pay payments, and the pricing is the same as other card transactions.


#### Tags:

 - Apple, Apply Pay, Payments

#### Properties

- [Documentation](https://stripe.com/docs/apple-pay)
- [OpenAPI](properties/stripe-apple-pay-api-openapi.yml)

### Stripe Application Fees API
When you collect a transaction fee on top of a charge made for your user (using Connect), an Application Fee object is created in your account. You can list, retrieve, and refund application fees.


#### Tags:

 - Applications, Fees, Refunds

#### Properties

- [Documentation](https://stripe.com/docs/api/application_fees)
- [OpenAPI](properties/stripe-application-fees-api-openapi.yml)

### Stripe Application Secrets API
Secret Store is an API that allows Stripe Apps developers to securely persist secrets for use by UI Extensions and app backends.


#### Tags:

 - Applications, Secrets

#### Properties

- [Documentation](https://stripe.com/docs/api/secret_management)
- [OpenAPI](openapi/stripe-application-secrets-api-openapi.yml)

### Stripe Balance API
This is an object representing your Stripe balance. You can retrieve it to see the balance currently on your Stripe account. You can also retrieve the balance history, which contains a list of transactions that contributed to the balance (charges, payouts, and so forth).


#### Tags:

 - Balance, History, Transactions

#### Properties

- [Documentation](https://stripe.com/docs/api/balance)
- [OpenAPI](openapi/stripe-balance-api-openapi.yml)

### Stripe Billing API
Create and manage subscriptions, recurring payments, and recurring revenue.


#### Tags:

 - Billing

#### Properties

- [Documentation](https://stripe.com/docs/billing)
- [OpenAPI](openapi/stripe-billing-api-openapi.yml)

### Stripe Charges API
The Charge object represents a single attempt to move money into your Stripe account. PaymentIntent confirmation is the most common way to create Charges, but transferring money to a different Stripe account through Connect also creates Charges. Some legacy payment flows create Charges directly, which is not recommended for new integrations.


#### Tags:

 - Charges, Disputes, Refunds

#### Properties

- [Documentation](https://stripe.com/docs/api/charges)
- [OpenAPI](openapi/stripe-charges-api-openapi.yml)

### Stripe Checkout API
Checkout is a low-code payment integration that creates a customizable form for collecting payments. You can embed Checkout directly in your website or redirect customers to a Stripe-hosted payment page. It supports one-time payments and subscriptions and accepts over 40 local payment methods.


#### Tags:

 - Checkout

#### Properties

- [Documentation](https://stripe.com/docs/payments/checkout)
- [OpenAPI](openapi/stripe-checkout-api-openapi.yml)

### Stripe Climate API
Stripe Climate is the easiest way to help promising permanent carbon removal technologies launch and scale. Join a growing group of ambitious businesses that are changing the course of carbon removal.


#### Tags:

 - Climate, Carbon

#### Properties

- [Documentation](https://stripe.com/climate)
- [OpenAPI](openapi/stripe-climate-api-openapi.yml)

### Stripe Country API
Stripe needs to collect certain pieces of information about each account created. These requirements can differ depending on the account's country. The Country Specs API makes these rules available to your integration.


#### Tags:

 - Countries

#### Properties

- [Documentation](https://stripe.com/docs/api/country_specs)
- [OpenAPI](openapi/stripe-country-api-openapi.yml)

### Stripe Coupons API
A coupon contains information about a percent-off or amount-off discount you might want to apply to a customer. Coupons may be applied to subscriptions, invoices, checkout sessions, quotes, and more. Coupons do not work with conventional one-off charges or payment intents.


#### Tags:

 - Coupons

#### Properties

- [Documentation](https://stripe.com/docs/api/coupons)
- [OpenAPI](openapi/stripe-coupons-api-openapi.yml)

### Stripe Credit Notes API
Issue a credit note to adjust an invoice's amount after the invoice is finalized.


#### Tags:

 - Credit, Notes

#### Properties

- [Documentation](https://stripe.com/docs/api/credit_notes)
- [OpenAPI](openapi/stripe-credit-notes-api-openapi.yml)

### Stripe Customers API
This object represents a customer of your business. Use it to create recurring charges and track payments that belong to the same customer.


#### Tags:

 - Customers

#### Properties

- [Documentation](https://stripe.com/docs/api/customers)
- [OpenAPI](openapi/stripe-customers-api-openapi.yml)

### Stripe Disputes API
A dispute occurs when a customer questions your charge with their card issuer. When this happens, you have the opportunity to respond to the dispute with evidence that shows that the charge is legitimate.


#### Tags:

 - Disputes

#### Properties

- [Documentation](https://stripe.com/docs/api/disputes)
- [OpenAPI](openapi/stripe-disputes-api-openapi.yml)

### Stripe Ephemeral Keys API
Stripe.js uses ephemeral keys to securely retrieve Card information from the Stripe API without publicly exposing your secret keys. You need to do some of the ephemeral key exchange on the server-side to set this up.


#### Tags:

 - Ephemeral, Keys

#### Properties

- [Documentation](https://stripe.com/docs/issuing/elements)
- [OpenAPI](openapi/stripe-ephemeral-keys-api-openapi.yml)

### Stripe Events API
Events are our way of letting you know when something interesting happens in your account. When an interesting event occurs, we create a new Event object.


#### Tags:

 - Events

#### Properties

- [Documentation](https://stripe.com/docs/api/events)
- [OpenAPI](openapi/stripe-events-api-openapi.yml)

### Stripe Exchange Rates API
Stripe supports processing charges in 135+ currencies allowing you to present prices in a customer's native currency. Doing so can improve sales and help customers avoid conversion costs. In order to present prices in your customer's currency, you need to specify the presentment currency when creating a PaymentIntent or a charge.


#### Tags:

 - Rates, Exchanges

#### Properties

- [Documentation](https://stripe.com/docs/currencies/conversions)
- [OpenAPI](openapi/stripe-exchange-rates-api-openapi.yml)

### Stripe Files API
This object represents files hosted on Stripe's servers. You can upload files with the create file request (for example, when uploading dispute evidence). Stripe also creates files independently (for example, the results of a Sigma scheduled query).


#### Tags:

 - Files

#### Properties

- [Documentation](https://stripe.com/docs/api/files)
- [OpenAPI](openapi/stripe-files-api-openapi.yml)

### Stripe Financial Connections API
Financial Connections lets your users securely share their financial data by linking their financial accounts to your business. Use Financial Connections to access user-permissioned account data such as tokenized account and routing numbers, balances, ownerships details, and transactions.


#### Tags:

 - Connections, Financial

#### Properties

- [Documentation](https://stripe.com/docs/financial-connections)
- [OpenAPI](openapi/stripe-financial-connections-api-openapi.yml)

### Stripe Identity API
Use Stripe Identity to confirm the identity of global users to prevent fraud, streamline risk operations, and increase trust and safety.


#### Tags:

 - Entities, Identity, Reports, Verification, Sessions, Cancel, Redact

#### Properties

- [Documentation](https://stripe.com/docs/identity)
- [OpenAPI](openapi/stripe-identity-api-openapi.yml)

### Stripe Invoice API
Invoices are statements of amounts owed by a customer, and are either generated one-off, or generated periodically from a subscription.


#### Tags:

 - Invoices

#### Properties

- [Documentation](https://stripe.com/docs/api/invoices)
- [OpenAPI](openapi/stripe-invoice-api-openapi.yml)

### Stripe Issuing API
An API for businesses to instantly create, manage, and distribute payment cards.


#### Tags:

 - Issuing, Cards

#### Properties

- [Documentation](https://stripe.com/docs/issuing)
- [OpenAPI](openapi/stripe-issuing-api-openapi.yml)

### Stripe Link API
You can use the Payment Links API to create a payment link that you can share with your customers. Stripe redirects customers who open this link to a Stripe-hosted payment page.


#### Tags:

 - Payments, Links

#### Properties

- [Documentation](https://stripe.com/docs/payment-links/api)
- [OpenAPI](openapi/stripe-link-api-openapi.yml)

### Stripe Payment Intents API
A PaymentIntent guides you through the process of collecting a payment from your customer. We recommend that you create exactly one PaymentIntent for each order or customer session in your system. You can reference the PaymentIntent later to see the history of payment attempts for a particular session.


#### Tags:

 - Intents, Payments, Intent

#### Properties

- [Documentation](https://stripe.com/docs/api/payment_intents)
- [OpenAPI](openapi/stripe-payment-intents-api-openapi.yml)

### Stripe Payment Links API
A payment link is a shareable URL that will take your customers to a hosted payment page. A payment link can be shared and used multiple times. When a customer opens a payment link it will open a new checkout session to render the payment page. You can use checkout session events to track payments through payment links.


#### Tags:

 - Links, Payments, Link

#### Properties

- [Documentation](https://stripe.com/docs/api/payment_links/payment_links)
- [OpenAPI](openapi/stripe-payment-links-api-openapi.yml)

### Stripe Payment Method API
The Payment Methods API allows you to accept a variety of payment methods through a single API. A PaymentMethod object contains the payment method details to create payments.


#### Tags:

 - Methods, Payments, Detach

#### Properties

- [Documentation](https://stripe.com/docs/payments/payment-methods)
- [OpenAPI](openapi/stripe-payment-method-api-openapi.yml)

### Stripe Payouts API
A Payout object is created when you receive funds from Stripe, or when you initiate a payout to either a bank account or debit card of a connected Stripe account. You can retrieve individual payouts, and list all payouts. Payouts are made on varying schedules, depending on your country and industry.


#### Tags:

 - Payouts

#### Properties

- [Documentation](https://stripe.com/docs/api/payouts)
- [OpenAPI](openapi/stripe-payouts-api-openapi.yml)

### Stripe Plans API
You can now model subscriptions more flexibly using the Prices API. It replaces the Plans API and is backwards compatible to simplify your migration.


#### Tags:

 - Plans, Plan

#### Properties

- [Documentation](https://stripe.com/docs/api/plans)
- [OpenAPI](openapi/stripe-plans-api-openapi.yml)

### Stripe Prices API
Prices define the unit cost, currency, and (optional) billing cycle for both recurring and one-time purchases of products. Products help you track inventory or provisioning, and prices help you track payment terms. Different physical goods or levels of service should be represented by products, and pricing options should be represented by prices. This approach lets you change prices without having to change your provisioning scheme.


#### Tags:

 - Prices

#### Properties

- [Documentation](https://stripe.com/docs/api/prices)
- [OpenAPI](openapi/stripe-prices-api-openapi.yml)

### Stripe Products API
Products describe the specific goods or services you offer to your customers. For example, you might offer a Standard and Premium version of your goods or service; each version would be a separate Product. They can be used in conjunction with Prices to configure pricing in Payment Links, Checkout, and Subscriptions.


#### Tags:

 - Products

#### Properties

- [Documentation](https://stripe.com/docs/api/products)
- [OpenAPI](openapi/stripe-products-api-openapi.yml)

### Stripe Promotion Codes API
A Promotion Code represents a customer-redeemable code for a coupon. It can be used to create multiple codes for a single coupon.


#### Tags:

 - Codes, Promotion, Promotions

#### Properties

- [Documentation](https://stripe.com/docs/api/promotion_codes)
- [OpenAPI](openapi/stripe-promotion-codes-api-openapi.yml)

### Stripe Quotes API
A Quote is a way to model prices that you'd like to provide to a customer. Once accepted, it will automatically create an invoice, subscription or subscription schedule.


#### Tags:

 - Quotes

#### Properties

- [Documentation](https://stripe.com/docs/api/quotes)
- [OpenAPI](openapi/stripe-quotes-api-openapi.yml)

### Stripe Radar API
Stripe Radar provides real-time fraud protection and requires no additional development time. Fraud professionals can add Radar for Fraud Teams to customize protection and get deeper insights.


#### Tags:

 - Fraud, Radar

#### Properties

- [Documentation](https://stripe.com/docs/radar)
- [OpenAPI](openapi/stripe-radar-api-openapi.yml)

### Stripe Refunds API
Refund objects allow you to refund a previously created charge that isn't refunded yet. Funds are refunded to the credit or debit card that's initially charged.


#### Tags:

 - Refunds

#### Properties

- [Documentation](https://stripe.com/docs/api/refunds)
- [OpenAPI](openapi/stripe-refunds-api-openapi.yml)

### Stripe Reporting API
The financial reports in the Dashboard provide downloadable reports in CSV format for a variety of accounting and reconciliation tasks. These reports are also available through the API, so you can schedule them to run automatically or run them whenever you need to receive the associated report files for accounting purposes.


#### Tags:

 - Reporting, Reports

#### Properties

- [Documentation](https://stripe.com/docs/reports/api)
- [OpenAPI](openapi/stripe-reporting-api-openapi.yml)

### Stripe Reviews API
Reviews can be used to supplement automated fraud detection with human expertise.


#### Tags:

 - Reviews

#### Properties

- [Documentation](https://stripe.com/docs/api/radar/reviews)
- [OpenAPI](openapi/stripe-reviews-api-openapi.yml)

### Stripe Setup API
Use the Setup Intents API to set up a payment method for future payments. It's similar to a payment, but no charge is created. Set up a payment method for future payments now.


#### Tags:

 - Setup, Intents, Intent

#### Properties

- [Documentation](https://stripe.com/docs/payments/setup-intents)
- [OpenAPI](openapi/stripe-setup-api-openapi.yml)

### Stripe Shipping Rates API
Shipping rates describe the price of shipping presented to your customers and applied to a purchase.


#### Tags:

 - Rates, Shipping

#### Properties

- [Documentation](https://stripe.com/docs/api/shipping_rates)
- [OpenAPI](openapi/stripe-shipping-rates-api-openapi.yml)

### Stripe Sigma API
If you have scheduled a Sigma query, you'll receive a sigma.scheduled_query_run.created webhook each time the query runs. The webhook contains a ScheduledQueryRun object, which you can use to retrieve the query results.


#### Tags:

 - Sigma

#### Properties

- [Documentation](https://stripe.com/docs/api/sigma/scheduled_queries)
- [OpenAPI](openapi/stripe-sigma-api-openapi.yml)

### Stripe Sources API
Source objects allow you to accept a variety of payment methods. They represent a customer's payment instrument, and can be used with the Stripe API just like a Card object once chargeable, they can be charged, or can be attached to customers.


#### Tags:

 - Sources, Transactions

#### Properties

- [Documentation](https://stripe.com/docs/api/sources)
- [OpenAPI](openapi/stripe-sources-api-openapi.yml)

### Stripe Subscription API
Subscriptions allow you to charge a customer on a recurring basis.


#### Tags:

 - Subscriptions, Recurring

#### Properties

- [Documentation](https://stripe.com/docs/api/subscriptions)
- [OpenAPI](openapi/stripe-subscription-api-openapi.yml)

### Stripe Tax API
Automate sales tax, VAT, and GST compliance on all your transactions-low or no code integrations available.


#### Tags:

 - Taxes

#### Properties

- [Documentation](https://stripe.com/docs/tax)
- [OpenAPI](openapi/stripe-tax-api-openapi.yml)

### Stripe Terminal API
Use Stripe Terminal to accept in-person payments and extend Stripe payments to your point of sale.


#### Tags:

 - Terminal, Terminals, Point of Sale

#### Properties

- [Documentation](https://stripe.com/docs/terminal)
- [OpenAPI](openapi/stripe-terminal-api-openapi.yml)

### Stripe Test Helpers API
Stripe provides a number of resources for testing your integration. Make sure to test the following use cases before launch, and use our Postman collection to make the testing process simpler.


#### Tags:

 - Synthetic, Virtualization, Testing

#### Properties

- [Documentation](https://stripe.com/docs/implementation-guides/billing/testing)
- [OpenAPI](openapi/stripe-test-helpers-api-openapi.yml)

### Stripe Tokens API
Tokenization is the process Stripe uses to collect sensitive card or bank account details, or personally identifiable information (PII), directly from your customers in a secure manner. A token representing this information is returned to your server to use. Use our recommended payments integrations to perform this process on the client-side. This guarantees that no sensitive card data touches your server, and allows your integration to operate in a PCI-compliant way.


#### Tags:

 - Tokens

#### Properties

- [Documentation](https://stripe.com/docs/api/tokens)
- [OpenAPI](openapi/stripe-tokens-api-openapi.yml)

### Stripe Topups API
To top up your Stripe balance, you create a top-up object. You can retrieve individual top-ups, as well as list all top-ups. Top-ups are identified by a unique, random ID.


#### Tags:

 - Topups

#### Properties

- [Documentation](https://stripe.com/docs/api/topups)
- [OpenAPI](openapi/stripe-topups-api-openapi.yml)

### Stripe Transfers API
A Transfer object is created when you move funds between Stripe accounts as part of Connect.


#### Tags:

 - Transfers

#### Properties

- [Documentation](https://stripe.com/docs/api/transfers)
- [OpenAPI](openapi/stripe-transfers-api-openapi.yml)

### Stripe Treasury API
Stripe Treasury is a banking-as-a-service API that lets you embed financial services in your product. With Stripe's API, you can enable businesses to hold funds, pay bills, earn yield, and manage their cash flow. Many users build Stripe Issuing in conjunction with Stripe Treasury to attach cards to spend funds in the account.


#### Tags:

 - Treasury

#### Properties

- [Documentation](https://stripe.com/docs/treasury)
- [OpenAPI](openapi/stripe-treasury-api-openapi.yml)

### Stripe Webhook API
You can configure webhook endpoints via the API to be notified about events that happen in your Stripe account or connected accounts.


#### Tags:

 - Webhooks

#### Properties

- [Documentation](https://stripe.com/docs/api/webhook_endpoints)
- [OpenAPI](openapi/stripe-webhook-api-openapi.yml)

## Common Properties

- [Sign Up](https://dashboard.stripe.com/register)
- [Authentication](https://stripe.com/docs/api/authentication)
- [Blog](https://stripe.com/blog)
- [Status](https://status.stripe.com/)
- [Change Log](https://stripe.com/docs/upgrades#api-versions)
- [Terms of Service](https://stripe.com/privacy)
- [Support](https://support.stripe.com/)

## Maintainers

**FN:** APIs.json

**Email:** info@apis.io
**FN:** Stripe

**Email:** support@stripe.com
