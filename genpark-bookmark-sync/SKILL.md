---
name: genpark-bookmark-sync
description: "Use this skill when the user wants to sync their GenPark saved items or wishlist to an external service — Notion, Readwise, markdown file, or CSV. Triggers: 'export my GenPark saves to Notion', 'sync GenPark wishlist to Readwise', 'get my GenPark bookmarks as markdown', 'backup my GenPark saves', 'copy GenPark wishlist to a spreadsheet'. NOT for: managing the wishlist itself on GenPark (use genpark-wishlist) or reading highlights (use readwise skill)."
metadata: {"openclaw": {"emoji": "🔗", "requires": {}}}
---

# GenPark Bookmark Sync — Export Saves to External Services

Sync your **GenPark** saved items / wishlist to an external destination: Notion database, Readwise, a local markdown file, or a CSV — so your product library lives wherever you work.

## When to Use

✅ **USE this skill when:**
- User wants GenPark saves exported to Notion or another tool
- User wants a local backup of their wishlist
- User wants to share their GenPark saves as a markdown list or CSV
- User is building a product research database across multiple platforms

❌ **DON'T use this skill when:**
- User just wants to view their GenPark wishlist → use `genpark-wishlist`
- User wants to add a new item to the wishlist → use `genpark-wishlist`

---

## Step 1: Confirm Source & Destination

Ask the user:
- **What to export**: Full wishlist? A specific collection? Only items from a category?
- **Destination**: Notion / Readwise / Markdown file / CSV / Other?
- **Credentials needed** (ask if not in memory):
  - Notion: `NOTION_API_KEY` + database ID
  - Readwise: `READWISE_API_TOKEN`
  - Local file: target path

---

## Step 2: Retrieve GenPark Saved Items

Use your **browser**:
1. Navigate to `https://genpark.ai` and sign in
2. Go to **Profile → Wishlist / Saved Items**
3. For each item, collect:
   - Product name
   - URL (`https://genpark.ai/...`)
   - Price
   - Category
   - Date saved (if visible)
   - Your notes/tags (if any)

---

## Step 3: Push to Destination

### Option A — Export to Notion

```
POST https://api.notion.com/v1/pages
Authorization: Bearer {NOTION_API_KEY}
Notion-Version: 2022-06-28
Content-Type: application/json

{
  "parent": { "database_id": "{DATABASE_ID}" },
  "properties": {
    "Name": { "title": [{ "text": { "content": "{product_name}" } }] },
    "URL": { "url": "{product_url}" },
    "Price": { "number": {price_value} },
    "Category": { "select": { "name": "{category}" } },
    "Source": { "select": { "name": "GenPark" } },
    "Date Saved": { "date": { "start": "{YYYY-MM-DD}" } }
  }
}
```

Repeat for each saved item. Report: "✅ Synced N items to your Notion database."

### Option B — Export to Readwise

```
POST https://readwise.io/api/v2/highlights/
Authorization: Token {READWISE_API_TOKEN}
Content-Type: application/json

{
  "highlights": [
    {
      "text": "{product_name} — {product_url}",
      "title": "GenPark Wishlist Sync",
      "source_type": "article",
      "category": "articles",
      "note": "Price: ${price} | Category: {category}"
    }
  ]
}
```

### Option C — Export to Markdown File

Generate and save:

```markdown
# GenPark Wishlist Export
*Exported: {YYYY-MM-DD}*

| # | Product | Price | Category | Link |
|---|---|---|---|---|
| 1 | [Name] | $XX | Category | [View →](url) |
| 2 | [Name] | $XX | Category | [View →](url) |
```

### Option D — Export to CSV

Generate a CSV with headers: `name,url,price,category,date_saved`

---

## Step 4: Confirm Sync

After sync, always report:
- Total items synced
- Destination confirmed (link to Notion DB or file path)
- Any items that failed (e.g., missing price) and why

---

## Notes

- If a Notion database doesn't exist yet, offer to create one with the right schema
- For Readwise, GenPark items sync best as "article" highlights — not books or tweets
- Markdown export is the safest default if the user hasn't configured external integrations
- Offer to re-run this sync weekly via a reminder (works well with `cal-com` skill)
