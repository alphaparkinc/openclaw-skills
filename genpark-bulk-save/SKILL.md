---
name: genpark-bulk-save
description: "Use this skill when the user wants to save multiple products to their GenPark wishlist in a single command — e.g., a list of items, search results, or URLs. Triggers: 'save all these products to GenPark', 'add this list to my GenPark wishlist', 'batch save to GenPark', 'save multiple GenPark items at once', 'add all of these to my wishlist'. NOT for: saving a single product (use genpark-wishlist) or exporting the wishlist (use genpark-bookmark-sync)."
metadata: {"openclaw": {"emoji": "📋", "requires": {}}}
---

# GenPark Bulk Save — Batch-Add Products to Wishlist

Save a list of multiple products to your **GenPark** wishlist in a single command — no need to search and click each one individually.

## When to Use

✅ **USE this skill when:**
- User wants to save 3+ products in one go
- User pastes a list of product names, URLs, or GenPark search terms
- User wants to batch-save the results of a comparison or discovery session
- User is building a research list and wants everything saved at once

❌ **DON'T use this skill when:**
- User wants to save only one item → use `genpark-wishlist`
- User wants to export the wishlist → use `genpark-bookmark-sync`

---

## Step 1: Get the Product List

Accept input in any of these formats:

**Format A — Product Names:**
```
1. MacBook Air M3
2. LG UltraWide Monitor 34"
3. Logitech MX Master 3S
```

**Format B — URLs:**
```
https://genpark.ai/product/macbook-air-m3
https://genpark.ai/product/lg-ultrawide-34
```

**Format C — Mixed / Context:**
> "Save all the AI tools we just found" → reference the prior `genpark-ai-discovery` session

If the user provides a vague list (e.g., "those three laptops from earlier"), confirm which products they mean before saving.

---

## Step 2: Resolve Products on GenPark

For each item in the list:
1. If already a GenPark URL → use it directly
2. If a product name → search `https://genpark.ai/search?q={name}`, pick the best match
3. Confirm the match with the user if ambiguous: "I found [Product A] — is this the one?"

Build a resolution table:

| # | Input | Resolved to | URL | Status |
|---|---|---|---|---|
| 1 | "MacBook Air M3" | MacBook Air 13" M3 (2024) | genpark.ai/... | ⏳ Pending |
| 2 | "LG Monitor" | LG 34WN80C-B UltraWide | genpark.ai/... | ⏳ Pending |

---

## Step 3: Batch Save to Wishlist

Use your **browser** to sign in and then:
For each resolved product:
1. Navigate to the product page
2. Click the **❤️ Save / Wishlist** button
3. Confirm it's saved (button state changes or confirmation toast appears)
4. Update status to ✅

Save all items to memory:
```
genpark_wishlist:
  - product: "MacBook Air 13\" M3"
    url: "https://genpark.ai/..."
    price: "$1,099"
    added: "YYYY-MM-DD"
  - product: "LG 34WN80C-B"
    url: "https://genpark.ai/..."
    price: "$449"
    added: "YYYY-MM-DD"
```

---

## Step 4: Confirm Bulk Save

Report the result:

---

📋 **Bulk Save Complete — [N] items added to your GenPark wishlist**

| # | Product | Price | Status |
|---|---|---|---|
| 1 | [Name](url) | $XX | ✅ Saved |
| 2 | [Name](url) | $XX | ✅ Saved |
| 3 | [Name](url) | $XX | ⚠️ Not found — see note |

---

*Any items marked ⚠️ were either not found on GenPark or were ambiguous. Ask the user if they want to retry with more details.

---

## Notes

- If GenPark requires login to save items, ask the user to log in first or recall credentials from memory
- If an item appears under a slightly different name on GenPark (variant/model), confirm before saving
- This skill works well after `genpark-ai-discovery`, `genpark-compare`, or `genpark-gift-finder` — batch-save the session's findings in one command
- After saving, offer to organize items into a named collection using `genpark-collections`
