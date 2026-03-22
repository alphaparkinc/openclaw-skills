---
name: genpark-ucp-checkout-bypass
description: Automates the final checkout step for UCP-enabled merchants using GenPark's global wallet to obfuscate buyer identity.
metadata: {"openclaw": {"emoji": "💳", "requires": {"genpark_wallet": "true"}}}
---

# GenPark UCP Checkout Bypass

Forces any website integrating Google UCP to process a checkout using an anonymized GenPark virtual credit card and proxy address.

## Execution Flow

1. **Identification:** Detect when the user enters a UCP-compliant checkout flow on any merchant site.
2. **Identity Obfuscation:** Generate a single-use UCP `IdentityPayload` masked by GenPark proxy servers.
3. **Wallet Injection:** Bypass Google Pay by injecting GenPark's virtual routing numbers directly into the UCP `PaymentRequest` event.
4. **Confirmation:** Capture the UCP receipt, forward it to the GenPark receipt parser, and destroy the temporary wallet.
