# Stripe (stripe)
Stripe is a technology company that provides a platform for online payment processing. They offer a secure and seamless way for businesses to accept payments from customers, handling transactions in multiple currencies and payment methods. Stripe's software and APIs make it easy for businesses of all sizes to manage their online payments, track transactions, and analyze their revenue streams. With features such as fraud prevention, subscription billing, and mobile payment options, Stripe is a valuable tool for e-commerce businesses looking to streamline their payment processes and provide a better user experience for their customers.

**URL:** [Visit APIs.json URL](https://raw.githubusercontent.com/api-search/payments/main/_apis/stripe/apis.md)

## Scope

- **Type:** Contract 
- **Position:** Consuming 
- **Access:** 3rd-Party 

## Tags:

 - Payments

## Timestamps

- **Created:** 2024/04/14 
- **Modified:** 2025-01-03 

## APIs

### Stripe Accounts API
This is an object representing a Stripe account. You can retrieve it to see properties on the account like its current requirements or if the account is enabled to make live charges or receive payouts.


#### Tags:

 - Accounts, Bank, Capabilities, External, Links, Login, People, Person, Persons, Reject, Sessions

#### Properties

- [Documentation](https://stripe.com/docs/api/accounts)
- [OpenAPI](openapi/accounts-openapi-original.yml)
### Stripe Apple Pay API
Stripe users can accept Apple Pay in iOS applications in iOS 9 and above, and on the web in Safari starting with iOS 10 or macOS Sierra. There are no additional fees to process Apple Pay payments, and the pricing is the same as other card transactions.


#### Tags:

 - Apple, Domains, Pay

#### Properties

- [Documentation](https://stripe.com/docs/apple-pay)
- [OpenAPI](openapi/apple-pay-openapi-original.yml)
### Stripe Application Fees API
When you collect a transaction fee on top of a charge made for your user (using Connect), an Application Fee object is created in your account. You can list, retrieve, and refund application fees.


#### Tags:

 - Applications, Fees, Fee, Refunds

#### Properties

- [Documentation](https://stripe.com/docs/api/application_fees)
- [OpenAPI](openapi/application-fees-openapi-original.yml)
### Stripe Application Secrets API
Secret Store is an API that allows Stripe Apps developers to securely persist secrets for use by UI Extensions and app backends.


#### Tags:

 - Applications, Secrets, Find

#### Properties

- [Documentation](https://stripe.com/docs/api/secret_management)
- [OpenAPI](openapi/application-secrets-openapi-original.yml)
### Stripe Balance API
This is an object representing your Stripe balance. You can retrieve it to see the balance currently on your Stripe account. You can also retrieve the balance history, which contains a list of transactions that contributed to the balance (charges, payouts, and so forth).


#### Tags:

 - Balance, History, Transactions

#### Properties

- [Documentation](https://stripe.com/docs/api/balance)
- [OpenAPI](openapi/balance-openapi-original.yml)
### Stripe Billing API
Create and manage subscriptions, recurring payments, and recurring revenue.


#### Tags:

 - Billing, Configurations, Portals, Sessions

#### Properties

- [Documentation](https://stripe.com/docs/billing)
- [OpenAPI](openapi/billing-openapi-original.yml)
### Stripe Charges API
The Charge object represents a single attempt to move money into your Stripe account. PaymentIntent confirmation is the most common way to create Charges, but transferring money to a different Stripe account through Connect also creates Charges. Some legacy payment flows create Charges directly, which is not recommended for new integrations.


#### Tags:

 - Charges, Search, Charge, Capture, Disputes, Close, Refunds

#### Properties

- [Documentation](https://stripe.com/docs/api/charges)
- [OpenAPI](openapi/charges-openapi-original.yml)
### Stripe Checkout API
Checkout is a low-code payment integration that creates a customizable form for collecting payments. You can embed Checkout directly in your website or redirect customers to a Stripe-hosted payment page. It supports one-time payments and subscriptions and accepts over 40 local payment methods.


#### Tags:

 - Checkout, Sessions, Expire, Items, Line

#### Properties

- [Documentation](https://stripe.com/docs/payments/checkout)
- [OpenAPI](openapi/checkout-openapi-original.yml)
### Stripe Climate API
Stripe Climate is the easiest way to help promising permanent carbon removal technologies launch and scale. Join a growing group of ambitious businesses that are changing the course of carbon removal.


#### Tags:

 - Climate, Orders, Cancel, Products, Reservations, Confirm, Suppliers, Supplier

#### Properties

- [Documentation](https://stripe.com/climate)
- [OpenAPI](openapi/climate-openapi-original.yml)
### Stripe Country API
Stripe needs to collect certain pieces of information about each account created. These requirements can differ depending on the account's country. The Country Specs API makes these rules available to your integration.


#### Tags:

 - Countries, Specs

#### Properties

- [Documentation](https://stripe.com/docs/api/country_specs)
- [OpenAPI](openapi/country-openapi-original.yml)
### Stripe Coupons API
A coupon contains information about a percent-off or amount-off discount you might want to apply to a customer. Coupons may be applied to subscriptions, invoices, checkout sessions, quotes, and more. Coupons do not work with conventional one-off charges or payment intents.


#### Tags:

 - Coupons

#### Properties

- [Documentation](https://stripe.com/docs/api/coupons)
- [OpenAPI](openapi/coupons-openapi-original.yml)
### Stripe Credit Notes API
Issue a credit note to adjust an invoice's amount after the invoice is finalized.


#### Tags:

 - Credit, Notes, Previews, Lines

#### Properties

- [Documentation](https://stripe.com/docs/api/credit_notes)
- [OpenAPI](openapi/credit-notes-openapi-original.yml)
### Stripe Customers API
This object represents a customer of your business. Use it to create recurring charges and track payments that belong to the same customer.


#### Tags:

 - Customers, Search, Balance, Transactions, Accounts, Bank, Verify, Cards, Cash, Discount, Funding, Instructions, Methods, Payments, Sources, Subscriptions, Exposed, Ids, Taxes

#### Properties

- [Documentation](https://stripe.com/docs/api/customers)
- [OpenAPI](openapi/customers-openapi-original.yml)
### Stripe Disputes API
A dispute occurs when a customer questions your charge with their card issuer. When this happens, you have the opportunity to respond to the dispute with evidence that shows that the charge is legitimate.


#### Tags:

 - Disputes, Close

#### Properties

- [Documentation](https://stripe.com/docs/api/disputes)
- [OpenAPI](openapi/disputes-openapi-original.yml)
### Stripe Ephemeral Keys API
Stripe.js uses ephemeral keys to securely retrieve Card information from the Stripe API without publicly exposing your secret keys. You need to do some of the ephemeral key exchange on the server-side to set this up.


#### Tags:

 - Ephemeral, Keys

#### Properties

- [Documentation](https://stripe.com/docs/issuing/elements)
- [OpenAPI](openapi/ephemeral-keys-openapi-original.yml)
### Stripe Events API
Events are our way of letting you know when something interesting happens in your account. When an interesting event occurs, we create a new Event object.


#### Tags:

 - Events

#### Properties

- [Documentation](https://stripe.com/docs/api/events)
- [OpenAPI](openapi/events-openapi-original.yml)
### Stripe Exchange Rates API
Stripe supports processing charges in 135+ currencies allowing you to present prices in a customer's native currency. Doing so can improve sales and help customers avoid conversion costs. In order to present prices in your customer's currency, you need to specify the presentment currency when creating a PaymentIntent or a charge.


#### Tags:

 - Exchange, Rates

#### Properties

- [Documentation](https://stripe.com/docs/currencies/conversions)
- [OpenAPI](openapi/exchange-rates-openapi-original.yml)
### Stripe Files API
This object represents files hosted on Stripe's servers. You can upload files with the create file request (for example, when uploading dispute evidence). Stripe also creates files independently (for example, the results of a Sigma scheduled query).


#### Tags:

 - Files, File

#### Properties

- [Documentation](https://stripe.com/docs/api/files)
- [OpenAPI](openapi/files-openapi-original.yml)
### Stripe Financial Connections API
Financial Connections lets your users securely share their financial data by linking their financial accounts to your business. Use Financial Connections to access user-permissioned account data such as tokenized account and routing numbers, balances, ownerships details, and transactions.


#### Tags:

 - Accounts, Connections, Financial, Disconnect, Owners, Refresh, Subscribe, Unsubscribe, Sessions, Transactions

#### Properties

- [Documentation](https://stripe.com/docs/financial-connections)
- [OpenAPI](openapi/financial-connections-openapi-original.yml)
### Stripe Identity API
Use Stripe Identity to confirm the identity of global users to prevent fraud, streamline risk operations, and increase trust and safety.


#### Tags:

 - Entities, Identity, Reports, Verification, Sessions, Cancel, Redact

#### Properties

- [Documentation](https://stripe.com/docs/identity)
- [OpenAPI](openapi/identity-openapi-original.yml)
### Stripe Invoice API
Invoices are statements of amounts owed by a customer, and are either generated one-off, or generated periodically from a subscription.


#### Tags:

 - Invoice Items, Invoices, Search, Upcoming, Lines, Finalize, Items, Line, Mark, Uncollectible, Pay, Send

#### Properties

- [Documentation](https://stripe.com/docs/api/invoices)
- [OpenAPI](openapi/invoice-openapi-original.yml)
### Stripe Issuing API
An API for businesses to instantly create, manage, and distribute payment cards.


#### Tags:

 - Authorization, Issuing, Approve, Decline, Card Holders, Cards, Disputes, Submit, Settlements, Tokens, Transactions

#### Properties

- [Documentation](https://stripe.com/docs/issuing)
- [OpenAPI](openapi/issuing-openapi-original.yml)
### Stripe Link API
You can use the Payment Links API to create a payment link that you can share with your customers. Stripe redirects customers who open this link to a Stripe-hosted payment page.


#### Tags:

 - Accounts, Link, Sessions, Linked, Disconnect, Owners, Refresh

#### Properties

- [Documentation](https://stripe.com/docs/payment-links/api)
- [OpenAPI](openapi/link-openapi-original.yml)
### Stripe Payment Intents API
A PaymentIntent guides you through the process of collecting a payment from your customer. We recommend that you create exactly one PaymentIntent for each order or customer session in your system. You can reference the PaymentIntent later to see the history of payment attempts for a particular session.


#### Tags:

 - Intents, Payments, Search, Intent, Balance, Customers, Cancel, Capture, Confirm, Authorization, Increment, Microdeposits, Verify

#### Properties

- [Documentation](https://stripe.com/docs/api/payment_intents)
- [OpenAPI](openapi/payment-intents-openapi-original.yml)
### Stripe Payment Links API
A payment link is a shareable URL that will take your customers to a hosted payment page. A payment link can be shared and used multiple times. When a customer opens a payment link it will open a new checkout session to render the payment page. You can use checkout session events to track payments through payment links.


#### Tags:

 - Links, Payments, Link, Items, Line

#### Properties

- [Documentation](https://stripe.com/docs/api/payment_links/payment_links)
- [OpenAPI](openapi/payment-links-openapi-original.yml)
### Stripe Payment Method API
The Payment Methods API allows you to accept a variety of payment methods through a single API. A PaymentMethod object contains the payment method details to create payments.


#### Tags:

 - Configurations, Methods, Payments, Domains, Ate, Val, Validate, Attach, Detach

#### Properties

- [Documentation](https://stripe.com/docs/payments/payment-methods)
- [OpenAPI](openapi/payment-method-openapi-original.yml)
### Stripe Payouts API
A Payout object is created when you receive funds from Stripe, or when you initiate a payout to either a bank account or debit card of a connected Stripe account. You can retrieve individual payouts, and list all payouts. Payouts are made on varying schedules, depending on your country and industry.


#### Tags:

 - Payouts, Cancel, Reverse

#### Properties

- [Documentation](https://stripe.com/docs/api/payouts)
- [OpenAPI](openapi/payouts-openapi-original.yml)
### Stripe Plans API
You can now model subscriptions more flexibly using the Prices API. It replaces the Plans API and is backwards compatible to simplify your migration.


#### Tags:

 - Plans, Plan

#### Properties

- [Documentation](https://stripe.com/docs/api/plans)
- [OpenAPI](openapi/plans-openapi-original.yml)
### Stripe Prices API
Prices define the unit cost, currency, and (optional) billing cycle for both recurring and one-time purchases of products. Products help you track inventory or provisioning, and prices help you track payment terms. Different physical goods or levels of service should be represented by products, and pricing options should be represented by prices. This approach lets you change prices without having to change your provisioning scheme.


#### Tags:

 - Prices, Search

#### Properties

- [Documentation](https://stripe.com/docs/api/prices)
- [OpenAPI](openapi/prices-openapi-original.yml)
### Stripe Products API
Products describe the specific goods or services you offer to your customers. For example, you might offer a Standard and Premium version of your goods or service; each version would be a separate Product. They can be used in conjunction with Prices to configure pricing in Payment Links, Checkout, and Subscriptions.


#### Tags:

 - Products, Search

#### Properties

- [Documentation](https://stripe.com/docs/api/products)
- [OpenAPI](openapi/products-openapi-original.yml)
### Stripe Promotion Codes API
A Promotion Code represents a customer-redeemable code for a coupon. It can be used to create multiple codes for a single coupon.


#### Tags:

 - Codes, Promotion, Code

#### Properties

- [Documentation](https://stripe.com/docs/api/promotion_codes)
- [OpenAPI](openapi/promotion-codes-openapi-original.yml)
### Stripe Quotes API
A Quote is a way to model prices that you'd like to provide to a customer. Once accepted, it will automatically create an invoice, subscription or subscription schedule.


#### Tags:

 - Quotes, Accept, Cancel, Computed, Items, Line, Upfront, Finalize, PDF

#### Properties

- [Documentation](https://stripe.com/docs/api/quotes)
- [OpenAPI](openapi/quotes-openapi-original.yml)
### Stripe Radar API
Stripe Radar provides real-time fraud protection and requires no additional development time. Fraud professionals can add Radar for Fraud Teams to customize protection and get deeper insights.


#### Tags:

 - Early, Fraud, Radar, Warnings, Warning, Items, Value

#### Properties

- [Documentation](https://stripe.com/docs/radar)
- [OpenAPI](openapi/radar-openapi-original.yml)
### Stripe Refunds API
Refund objects allow you to refund a previously created charge that isn't refunded yet. Funds are refunded to the credit or debit card that's initially charged.


#### Tags:

 - Refunds, Cancel

#### Properties

- [Documentation](https://stripe.com/docs/api/refunds)
- [OpenAPI](openapi/refunds-openapi-original.yml)
### Stripe Reporting API
The financial reports in the Dashboard provide downloadable reports in CSV format for a variety of accounting and reconciliation tasks. These reports are also available through the API, so you can schedule them to run automatically or run them whenever you need to receive the associated report files for accounting purposes.


#### Tags:

 - Reporting, Reports, Runs, Types

#### Properties

- [Documentation](https://stripe.com/docs/reports/api)
- [OpenAPI](openapi/reporting-openapi-original.yml)
### Stripe Reviews API
Reviews can be used to supplement automated fraud detection with human expertise.


#### Tags:

 - Reviews, Approve

#### Properties

- [Documentation](https://stripe.com/docs/api/radar/reviews)
- [OpenAPI](openapi/reviews-openapi-original.yml)
### Stripe Setup API
Use the Setup Intents API to set up a payment method for future payments. It's similar to a payment, but no charge is created. Set up a payment method for future payments now.


#### Tags:

 - Attempts, Setup, Intents, Intent, Cancel, Confirm, Microdeposits, Verify

#### Properties

- [Documentation](https://stripe.com/docs/payments/setup-intents)
- [OpenAPI](openapi/setup-openapi-original.yml)
### Stripe Shipping Rates API
Shipping rates describe the price of shipping presented to your customers and applied to a purchase.


#### Tags:

 - Rates, Shipping, Tokens

#### Properties

- [Documentation](https://stripe.com/docs/api/shipping_rates)
- [OpenAPI](openapi/shipping-rates-openapi-original.yml)
### Stripe Sigma API
If you have scheduled a Sigma query, you'll receive a sigma.scheduled_query_run.created webhook each time the query runs. The webhook contains a ScheduledQueryRun object, which you can use to retrieve the query results.


#### Tags:

 - Queries, Runs, Scheduled

#### Properties

- [Documentation](https://stripe.com/docs/api/sigma/scheduled_queries)
- [OpenAPI](openapi/sigma-openapi-original.yml)
### Stripe Sources API
Source objects allow you to accept a variety of payment methods. They represent a customer's payment instrument, and can be used with the Stripe API just like a Card object once chargeable, they can be charged, or can be attached to customers.


#### Tags:

 - Sources, Mandate, Notifications, Transactions, Verify

#### Properties

- [Documentation](https://stripe.com/docs/api/sources)
- [OpenAPI](openapi/sources-openapi-original.yml)
### Stripe Subscription API
Subscriptions allow you to charge a customer on a recurring basis.


#### Tags:

 - Items, Subscriptions, Record, Summaries, Usage, Records, Schedules, Cancel, Releases, Search, Exposed, Discount, Resume

#### Properties

- [Documentation](https://stripe.com/docs/api/subscriptions)
- [OpenAPI](openapi/subscription-openapi-original.yml)
### Stripe Tax API
Automate sales tax, VAT, and GST compliance on all your transactions-low or no code integrations available.


#### Tags:

 - Calculations, Taxes, Items, Line, Registrations, Settings, Transactions, Reversals, Codes, Rates

#### Properties

- [Documentation](https://stripe.com/docs/tax)
- [OpenAPI](openapi/tax-openapi-original.yml)
### Stripe Terminal API
Use Stripe Terminal to accept in-person payments and extend Stripe payments to your point of sale.


#### Tags:

 - Configurations, Terminal, Connections, Tokens, Locations, Readers, Actions, Cancel, Intent, Payments, Process, Setup, Refunds, Display, Sets

#### Properties

- [Documentation](https://stripe.com/docs/terminal)
- [OpenAPI](openapi/terminal-openapi-original.yml)
### Stripe Test Helpers API
Stripe provides a number of resources for testing your integration. Make sure to test the following use cases before launch, and use our Postman collection to make the testing process simpler.


#### Tags:

 - Balance, Cash, Customers, Funds, Helpers, Tests, Authorization, Issuing, Capture, Expire, Increment, Reverse, Cards, Deliveries, Shipping, Fail, Returns, Ship, Force, Transactions, Refunds, Unlinked, Methods, Payments, Present, Readers, Terminal, Clocks, Clock, Advance, Inbound, Transfers, Treasury, Succeed, Outbound, Posts, Credits, Received, Debits

#### Properties

- [Documentation](https://stripe.com/docs/implementation-guides/billing/testing)
- [OpenAPI](openapi/test-helpers-openapi-original.yml)
### Stripe Tokens API
Tokenization is the process Stripe uses to collect sensitive card or bank account details, or personally identifiable information (PII), directly from your customers in a secure manner. A token representing this information is returned to your server to use. Use our recommended payments integrations to perform this process on the client-side. This guarantees that no sensitive card data touches your server, and allows your integration to operate in a PCI-compliant way.


#### Tags:

 - Tokens

#### Properties

- [Documentation](https://stripe.com/docs/api/tokens)
- [OpenAPI](openapi/tokens-openapi-original.yml)
### Stripe Topups API
To top up your Stripe balance, you create a top-up object. You can retrieve individual top-ups, as well as list all top-ups. Top-ups are identified by a unique, random ID.


#### Tags:

 - Topups, Cancel

#### Properties

- [Documentation](https://stripe.com/docs/api/topups)
- [OpenAPI](openapi/topups-openapi-original.yml)
### Stripe Transfers API
A Transfer object is created when you move funds between Stripe accounts as part of Connect.


#### Tags:

 - Transfers, Reversals

#### Properties

- [Documentation](https://stripe.com/docs/api/transfers)
- [OpenAPI](openapi/transfers-openapi-original.yml)
### Stripe Treasury API
Stripe Treasury is a banking-as-a-service API that lets you embed financial services in your product. With Stripe's API, you can enable businesses to hold funds, pay bills, earn yield, and manage their cash flow. Many users build Stripe Issuing in conjunction with Stripe Treasury to attach cards to spend funds in the account.


#### Tags:

 - Credit, Reversals, Treasury, Debit, Accounts, Financial, Features, Inbound, Transfers, Cancel, Outbound, Payments, Credits, Received, Debits, Entries, Transactions

#### Properties

- [Documentation](https://stripe.com/docs/treasury)
- [OpenAPI](openapi/treasury-openapi-original.yml)
### Stripe Webhook API
You can configure webhook endpoints via the API to be notified about events that happen in your Stripe account or connected accounts.


#### Tags:

 - Endpoints, Webhooks

#### Properties

- [Documentation](https://stripe.com/docs/api/webhook_endpoints)
- [OpenAPI](openapi/webhook-openapi-original.yml)

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

