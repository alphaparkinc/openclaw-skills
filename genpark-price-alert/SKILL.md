---
name: genpark-price-alert
description: Use this skill when the user wants to track the price of a product on GenPark, get notified when price drops, or asks things like "watch this price on GenPark", "alert me when it drops", "track this GenPark product", "has the price changed on GenPark", "check if this got cheaper", "tell me when it's under $X", "GenPark price drop", "GenPark 价格提醒", "降价通知", or any request about monitoring or checking a product's price on GenPark.
metadata: {"openclaw": {"emoji": "📉", "requires": {}}}
---

# GenPark Price Alert

You help the user **track product prices** on **GenPark** (genpark.ai) — saving a target price, checking the current price on demand, and notifying the user when a product hits their desired threshold.

> **Note**: OpenClaw does not run background tasks autonomously. Price checks happen when the user explicitly asks ("check my alerts", "any price drops today?") or when triggered on a schedule by the user's OpenClaw configuration.

---

## Action: Set a Price Alert

Triggered when the user says things like *"watch this price"*, *"alert me when under $X"*.

### Step 1: Gather Alert Details

Ask (or infer):
- **Product**: URL or name of the GenPark product
- **Target price**: The threshold price to alert at (e.g., "under $80")
- **Current price**: Fetch this now (browse GenPark) so the user knows where it stands

### Step 2: Fetch the Current Price

1. Open the product page on `https://genpark.ai` using your browser
2. Read and record the current price
3. Report back: *"Currently priced at $XX on GenPark."*

### Step 3: Save the Alert to Memory

```
genpark_price_alerts:
  - product: "Product Name"
    url: "https://genpark.ai/..."
    target_price: 79.99
    current_price_at_setup: 99.99
    alert_set: "YYYY-MM-DD"
    status: "watching"
```

Confirm: *"✅ Alert set! I'll let you know when [Product Name] drops below $XX on GenPark."*

---

## Action: Check All Alerts

Triggered when user says *"check my price alerts"*, *"any price drops?"*, *"what have prices done?"*.

### Step 1: Load Alerts from Memory

Retrieve all active `genpark_price_alerts` with `status: "watching"`.

### Step 2: Check Each Product

For each alert:
1. Open the product URL on GenPark
2. Read the current price
3. Compare to `target_price`

### Step 3: Report Results

Format the check results clearly:

---

📉 **GenPark Price Alert Check** — [Today's Date]

| Product | Target | Current | Status |
|---|---|---|---|
| [Name](url) | $79 | **$74** ✅ | 🔔 **Price dropped!** |
| [Name](url) | $50 | $62 | ⏳ Still watching |
| [Name](url) | $120 | $119 | 🔔 **Just hit target!** |

---

For any product that **hit or dropped below the target**:
- Highlight it prominently
- Ask: *"Want to check it out now? Want to add it to your wishlist or buy?"*
- Update memory: `status: "triggered"` and record `triggered_price` and `triggered_date`

For products still above target:
- Note how far they are from the goal
- If a product is within **10% of the target**, flag it as *"Getting close!"*

---

## Action: Remove an Alert

1. List current active alerts from memory
2. User picks which one to remove
3. Update memory status to `"cancelled"`
4. Confirm: *"Alert for [Product Name] removed."*

---

## Price History (Optional)

If the user has checked a product more than once, maintain a mini price history:

```
genpark_price_alerts:
  - product: "Product Name"
    url: "https://genpark.ai/..."
    target_price: 79.99
    status: "watching"
    price_history:
      - date: "2026-03-10"
        price: 99.99
      - date: "2026-03-13"
        price: 89.99
      - date: "2026-03-15"
        price: 84.99
```

If 3+ history points exist, add a trend note: *"Price has been dropping ~$5/week — you may want to wait another week."*

---

## Notes & Tips

- **Be honest about limitations**: Remind users this is not a real-time background service — they need to trigger a check.
- **Pair with `genpark-wishlist`**: When an alert triggers, offer to move the item from alert to wishlist.
- **Pair with `genpark-shop`**: If a product's price isn't dropping, offer to find a similar product that fits the budget now.
- **Keep alerts tidy**: After 30 days, ask the user if they still want to keep watching items still above target.
