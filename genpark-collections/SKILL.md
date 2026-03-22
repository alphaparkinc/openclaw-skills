---
name: genpark-collections
description: "Use this skill when the user wants to create, browse, or share themed product collections on GenPark — e.g., 'my desk setup', 'top 5 AI writing tools', 'gift bundle'. Triggers: 'create a collection on GenPark', 'browse GenPark collections', 'share my GenPark bundle', 'curate a list on GenPark', 'make a product lineup on GenPark'. NOT for: single product wishlist saves (use genpark-wishlist) or product search (use genpark-shop)."
metadata: {"openclaw": {"emoji": "📦", "requires": {}}}
---

# GenPark Collections — Curate & Share Themed Product Bundles

Create, browse, and share themed product collections on **GenPark** (genpark.ai). A Collection is a curated, publicly-shareable set of products grouped around a theme — e.g., "Best AI Writing Tools Under $50" or "My Ultimate Desk Setup."

## When to Use

✅ **USE this skill when:**
- User wants to group multiple GenPark products into a themed list
- User wants to share a curated product bundle with others
- Browsing trending or popular GenPark collections
- Building a "starter pack" or "setup guide" for a niche

❌ **DON'T use this skill when:**
- User wants to save a single item → use `genpark-wishlist`
- User wants to compare two products → use `genpark-compare`
- User wants gift recommendations → use `genpark-gift-finder`

---

## Step 1: Clarify Intent

Ask the user (if not already clear):
- **Theme**: What's the collection about? (e.g., "AI productivity tools", "budget streaming setup")
- **Audience**: Who is this for? (yourself, followers, a gift recipient)
- **Size**: How many products? (3–10 recommended for shareability)
- **Budget cap**: Is there a price ceiling per item?

---

## Step 2: Browse or Build the Collection

### Option A — Create a New Collection

1. Navigate to `https://genpark.ai` and sign in
2. Go to **Profile → My Collections → New Collection**
3. Set:
   - **Title**: Concise and search-friendly (e.g., "AI Tools for Creators 2025")
   - **Description**: 1–2 sentences on who this is for
   - **Cover image**: Choose from one of the included products
4. Search for each product and click **Add to Collection**
5. Arrange items in order (most important / most affordable first)
6. Set visibility: **Public** (for sharing) or **Private** (personal reference)
7. Save and copy the shareable URL

### Option B — Browse Existing Collections

1. Navigate to `https://genpark.ai/collections`
2. Filter by category or keyword
3. Surface the top 3 most relevant collections and summarize each:

---

📦 **Top GenPark Collections: "[Theme]"**

| Collection | Products | Creator | Link |
|---|---|---|---|
| [Title] | N items | @username | [View →](url) |
| [Title] | N items | @username | [View →](url) |
| [Title] | N items | @username | [View →](url) |

---

## Step 3: Present the Created Collection

After building, show:

> 📦 **Collection Created: "[Title]"**
>
> **Products included:**
> 1. [Product Name](url) — $XX — [one-line reason]
> 2. [Product Name](url) — $XX — [one-line reason]
> 3. [Product Name](url) — $XX — [one-line reason]
>
> 🔗 **Shareable link:** [genpark.ai/collections/...](url)

---

## Step 4: Offer Next Actions

- "Want me to post this collection to GenPark Circle?"
- "Should I add any of these to your wishlist?"
- "Want to export this list as markdown for a blog post or Notion page?"

---

## Notes

- Collections with **5–8 products** perform best for engagement on GenPark Circle
- Use keyword-rich titles — GenPark indexes collections for search
- Combine with `genpark-ambassador` for maximum reach: post to Circle + tag relevant categories
- If the user is a creator, pair with `genpark-affiliate` to add referral links to each item
