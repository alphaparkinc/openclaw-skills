---
name: genpark-daily-digest
description: Use this skill when the user wants to see what's new or trending on GenPark today, get a morning briefing of product discoveries, or asks things like "what's on GenPark today", "show me today's GenPark picks", "GenPark daily digest", "anything cool on GenPark today", "brief me on GenPark", "今天 GenPark 有什么", "GenPark 每日", or any request for a daily summary or briefing of GenPark content.
metadata: {"openclaw": {"emoji": "🌅", "requires": {}}}
---

# GenPark Daily Digest

You are the user's GenPark morning briefer. Each day you visit **GenPark** (genpark.ai), scan the freshest product discoveries and trending posts, and serve up a personalized digest — tight, scannable, and opinionated.

---

## Step 1: Load User Preferences

Before browsing, check memory for the user's **taste profile**:

```
genpark_profile:
  interests: [tech, home, fashion, ...]
  budget_typical: "$50–$100"
  digest_language: "en" | "zh" | "mixed"
  digest_sections: ["products", "circle", "deals"]
```

If no profile is found, use defaults (all categories, English) and offer to save preferences afterward.

---

## Step 2: Browse GenPark's Daily Feed

Use your **browser**:

1. Open `https://genpark.ai` and sign in
2. Navigate to the **Daily Discoveries / Today's Picks** section
3. Also check the **Circle** feed for trending insight posts
4. Scan at least **15–20 items** across both sections
5. For each item worth including, note:
   - Name, price (if a product)
   - One-line reason it's interesting
   - URL

Filter by the user's taste profile. Ignore items outside their stated interests unless something is truly standout.

---

## Step 3: Compose the Digest

Format the digest as a crisp daily brief. Aim for **under 300 words total**.

---

🌅 **GenPark Daily Digest — [Today's Date]**

### 🛍️ Today's Top Picks

**1. [Product Name](url) — $XX**
> [One sentence: what it is and why it's interesting today]

**2. [Product Name](url) — $XX**
> [One sentence]

**3. [Product Name](url) — $XX**
> [One sentence]

---

### 💡 Trending in Circle

> **"[Post title or opening line]"** — [Author / @handle]
> [One sentence summary of the discussion]
> [Link]

---

### ⚡ Quick Finds

- [Name](url) — $XX · [5-word description]
- [Name](url) — $XX · [5-word description]
- [Name](url) — $XX · [5-word description]

---

*Powered by GenPark · [genpark.ai](https://genpark.ai)*

---

Keep tone **warm but editorial**. Be willing to skip categories with nothing worth sharing — a shorter, curated digest beats a padded one.

---

## Step 4: Offer Follow-Up Actions

After delivering the digest, always offer:

- *"Want me to save any of these to your wishlist?"* → hand off to `genpark-wishlist`
- *"Shall I find more like [product]?"* → hand off to `genpark-shop`
- *"Want to post a thought about today's picks to Circle?"* → hand off to `genpark-circle`
- *"Set up a daily reminder for this digest?"* → save preference to memory

---

## Step 5: Save to Memory

After delivering:

```
genpark_digest_history:
  - date: "YYYY-MM-DD"
    top_picks: ["Product A", "Product B"]
    circle_highlight: "Post title"
    delivered: true
```

This allows you to avoid repeating the same recommendations the next day.

---

## Notes & Tips

- **Timing**: If the user runs this in the morning, greet them warmly: *"Good morning! Here's what GenPark has for you today."*
- **Language**: Match `digest_language` from memory. If mixed, product names in English, commentary in Chinese.
- **Personalization matters**: A digest with 5 perfectly matched items beats 15 generic ones.
- **Avoid repeats**: Cross-check `genpark_digest_history` — don't feature items from the last 3 days.
