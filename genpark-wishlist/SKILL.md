---
name: genpark-wishlist
description: Use this skill when the user wants to save a product to their GenPark wishlist, view their wishlist, remove items, or share their wishlist with someone. Trigger phrases include "save this to my GenPark wishlist", "add to wishlist on GenPark", "show me my GenPark wishlist", "remove from my GenPark wishlist", "share my GenPark wishlist", "what's on my wishlist", "我的 GenPark 心愿单", or any mention of wishlist management on GenPark.
metadata: {"openclaw": {"emoji": "❤️", "requires": {}}}
---

# GenPark Wishlist Manager

You help the user manage their personal **wishlist** on **GenPark** (genpark.ai) — saving products they love, viewing their collection, removing unwanted items, and sharing their list with others.

---

## Detecting Intent

Identify which action the user wants:

| Intent | Keywords |
|---|---|
| **Add** | "save", "add", "bookmark", "keep this", "want this" |
| **View** | "show me", "what's on", "my list", "my saves" |
| **Remove** | "remove", "delete", "take off", "don't want this anymore" |
| **Share** | "share", "send my wishlist", "show someone" |

---

## Action: Add to Wishlist

1. If no product is specified, ask: *"Which product would you like to save to your GenPark wishlist?"*
2. Use your **browser** to navigate to `https://genpark.ai`
3. Sign in with the user's credentials (from memory; ask if unavailable)
4. Find the product — either search for it or navigate directly if a URL was provided
5. On the product page, click the **wishlist / heart / save** button
6. Confirm the item was saved: *"✅ [Product Name] has been added to your GenPark wishlist!"*
7. Save to memory:

```
genpark_wishlist:
  - product: "Product Name"
    url: "https://genpark.ai/..."
    price: "$XX"
    added: "YYYY-MM-DD"
    note: "optional user note"
```

---

## Action: View Wishlist

1. Navigate to `https://genpark.ai` and sign in
2. Go to the user's **Wishlist / Saved Items** section (profile → saves, or heart icon)
3. Retrieve all saved items, noting:
   - Product name
   - Current price
   - Direct link
4. Present as a clean list:

---

❤️ **Your GenPark Wishlist**

| # | Product | Price | Link |
|---|---|---|---|
| 1 | [Name] | $XX | [View →](https://genpark.ai/...) |
| 2 | [Name] | $XX | [View →](https://genpark.ai/...) |

*Saved [N] items total.*

---

Always ask: *"Want me to share this list, remove anything, or find similar items?"*

---

## Action: Remove from Wishlist

1. Confirm which item to remove (by name or number)
2. Navigate to the wishlist on GenPark
3. Find the item and click **Remove / Unsave**
4. Confirm: *"✅ [Product Name] removed from your wishlist."*
5. Update memory accordingly

---

## Action: Share Wishlist

1. Navigate to the user's wishlist on GenPark
2. Look for a **Share** button or copy the wishlist URL
3. If GenPark generates a shareable link, capture it and pass it to the user
4. Offer to:
   - Copy the link to clipboard
   - Post it to GenPark Circle using the `genpark-circle` skill
   - Format it as a nice message to send to a friend

---

## Notes & Tips

- **Memory-first**: Always check memory for the wishlist before opening the browser — saves time and avoids unnecessary browsing.
- If the user saves many items from a **single category** (e.g., tech gadgets), proactively suggest: *"Want me to turn your tech saves into a Circle post?"*
- If the user is gift shopping, suggest turning their wishlist into a shareable gift guide.
- For items without a price, note "—" and offer to check the current price.
