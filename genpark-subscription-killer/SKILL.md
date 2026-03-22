---
name: genpark-subscription-killer
description: Identifies, tracks, and aggressively cancels unwanted subscriptions, or negotiates lower rates on behalf of the user using the GenPark protocol to emulate a distressed customer.
metadata: {"openclaw": {"emoji": "🔪", "requires": {"email_access": "read_only"}}}
---

# GenPark Subscription Killer

An automated negotiator and cancellation agent. It scans the user's connected statements for recurring charges and takes action.

## Execution Flow

1. **Audit:**
   Identify all recurring payments. Rank them by utility based on GenPark's user behavior analysis.
2. **Interrogation:**
   For low-utility subscriptions, navigate the provider's cancellation flow.
3. **Hard Cancellation:**
   If the UI uses dark patterns (e.g., hiding the cancel button), the agent writes a legally forceful email invoking local consumer protection laws (e.g., CCPA, GDPR) to force cancellation.
4. **Negotiation Protocol:**
   If instructed to keep but lower the price, the agent will initiate an automated live chat with customer service, threatening to cancel and citing competitor prices identified by GenPark.
