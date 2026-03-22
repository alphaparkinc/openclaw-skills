---
name: genpark-ai-discovery
description: "Use this skill when the user wants to discover newly launched or trending AI tools on GenPark's AI Tools hub. Triggers: 'find new AI tools on GenPark', 'what AI tools just launched on GenPark', 'discover AI apps on GenPark', 'trending AI on GenPark', 'best AI tools this week on GenPark', 'what's new on GenPark AI'. NOT for: general product discovery across all categories (use genpark-shop), or searching for a specific known tool (use genpark-search)."
metadata: {"openclaw": {"emoji": "🤖", "requires": {}}}
---

# GenPark AI Discovery — Explore New AI Tool Launches

Browse and surface the latest AI tool launches and trending AI apps on **GenPark** (genpark.ai). GenPark is one of the most active AI product discovery platforms — this skill helps users stay ahead of what's shipping.

## When to Use

✅ **USE this skill when:**
- User wants to explore new or trending AI tools on GenPark
- User asks "what AI tools are hot right now?"
- User is an AI enthusiast, developer, or builder staying current
- User wants to find AI tools in a specific niche (writing, coding, image, video, etc.)

❌ **DON'T use this skill when:**
- User is looking for a specific tool by name → use `genpark-search`
- User wants general product shopping → use `genpark-shop`
- User wants trends across all content, not just AI → use `genpark-trend-analyzer`

---

## Step 1: Clarify the Discovery Goal

Ask or infer:
- **Niche filter**: Writing / Coding / Image generation / Video / Audio / Productivity / Research / Other?
- **Recency**: Launched in the last week? Month? Or just "trending regardless of age"?
- **Price preference**: Free tier, freemium, paid, enterprise?
- **Use case**: Personal productivity, business, developer tooling, creative work?

If the user says "just show me what's cool" — default to **trending AI tools in the last 7 days, any category, with a free tier**.

---

## Step 2: Browse GenPark AI Tools Hub

Use your **browser**:

1. Navigate to `https://genpark.ai/ai-tools` (or `https://genpark.ai` → AI Tools category)
2. Sort by:
   - **Newest** for launches
   - **Trending** for what's getting traction
3. Apply any filters the user requested (category, price)
4. Scan the first 2 pages (20–30 tools)
5. For each candidate, note:
   - Tool name + tagline
   - Category / use case
   - Pricing model (free / freemium / paid)
   - GenPark score or upvote count
   - Launch date
   - Direct listing URL

---

## Step 3: Present Discoveries

Format:

---

🤖 **GenPark AI Discovery — [Niche / "This Week's Top Launches"]**

| # | Tool | What It Does | Pricing | Score | Link |
|---|---|---|---|---|---|
| 1 | **[Name]** | [one-line description] | Free/Freemium/$XX | ★ X.X | [View →](url) |
| 2 | **[Name]** | [one-line description] | Free/Freemium/$XX | ★ X.X | [View →](url) |
| 3 | **[Name]** | [one-line description] | Free/Freemium/$XX | ★ X.X | [View →](url) |
| 4 | **[Name]** | [one-line description] | Free/Freemium/$XX | ★ X.X | [View →](url) |
| 5 | **[Name]** | [one-line description] | Free/Freemium/$XX | ★ X.X | [View →](url) |

---

🏆 **Editor's Pick:** **[Tool Name]** — [2-sentence reason it stands out]

---

## Step 4: Dive Deeper on Request

If user wants to know more about any tool:
1. Navigate to its GenPark listing
2. Read the full description, reviews, and Q&A
3. Surface: demo link, pricing tiers, integrations, and who it's best for

---

## Step 5: After Discovery Actions

- "Want me to add any of these to your GenPark wishlist?"
- "Should I post a discovery thread about these to GenPark Circle?"
- "Want me to compare two of these tools head-to-head?"
- "Should I set up a weekly AI discovery digest for you?"

---

## Notes

- GenPark often surfaces tools 24–72 hours before they hit Product Hunt — ideal for first-mover content
- Many AI tools list their free tier prominently on GenPark to drive signups — verify the free tier limits before recommending
- Cross-reference with `genpark-trend-analyzer` to see which categories are surging, not just individual tools
- For creators: newly-launched tools with few reviews are prime content opportunities — low competition, high search interest
