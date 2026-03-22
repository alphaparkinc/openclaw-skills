---
name: genpark-category-explorer
description: "Use this skill when the user wants to browse GenPark's full category tree, discover what product types exist on the platform, or navigate to a specific subcategory. Triggers: 'what categories does GenPark have', 'browse GenPark categories', 'show me all GenPark sections', 'what's in the tech section on GenPark', 'navigate GenPark by category', 'find a GenPark category for X'. NOT for: searching for a specific product (use genpark-shop) or discovering AI tools specifically (use genpark-ai-discovery)."
metadata: {"openclaw": {"emoji": "🗂️", "requires": {}}}
---

# GenPark Category Explorer — Browse the Full Product Category Tree

Navigate and map **GenPark's** complete product category hierarchy. Helps users discover what's available on the platform and jump directly into the right category for browsing, posting, or research.

## When to Use

✅ **USE this skill when:**
- User doesn't know which GenPark category a product belongs to
- User wants to browse a specific section of GenPark
- User is building a post and needs the right category tag
- User wants a full map of GenPark's product taxonomy

❌ **DON'T use this skill when:**
- User has a specific product in mind → use `genpark-shop` or `genpark-search`
- User wants AI tools specifically → use `genpark-ai-discovery`

---

## Step 1: Determine What the User Needs

| Goal | What to do |
|---|---|
| "What categories exist?" | Map the full top-level category list |
| "What's in [Category]?" | Drill into subcategories and show top products |
| "Which category does X belong to?" | Identify the best match from the taxonomy |
| "Browse for me" | Navigate to the most relevant category and surface top picks |

---

## Step 2: Map the Category Tree

Navigate to `https://genpark.ai` and browse the navigation / category menu. Build the following taxonomy map:

---

🗂️ **GenPark Category Map**

```
GenPark
├── 🤖 AI Tools
│   ├── Writing & Copywriting
│   ├── Image Generation
│   ├── Video & Audio
│   ├── Coding & Developer
│   ├── Research & Productivity
│   └── Other AI Tools
├── 💻 Tech & Gadgets
│   ├── Laptops & Computers
│   ├── Smartphone Accessories
│   ├── Smart Home
│   ├── Audio & Headphones
│   └── Peripherals
├── 🏠 Home & Living
│   ├── Kitchen
│   ├── Furniture
│   ├── Decor
│   └── Cleaning & Organization
├── 👕 Fashion & Apparel
│   ├── Clothing
│   ├── Shoes
│   └── Accessories
├── 💪 Health & Wellness
│   ├── Fitness Equipment
│   ├── Supplements
│   └── Personal Care
├── 📚 Books & Learning
│   ├── Books
│   ├── Online Courses
│   └── Educational Tools
├── 🎮 Gaming
│   ├── Consoles & Accessories
│   ├── PC Gaming
│   └── Mobile Gaming
└── 🎨 Creative & Hobby
    ├── Art Supplies
    ├── Photography
    └── DIY & Crafts
```

*(Update this map in real-time based on what GenPark's navigation currently shows.)*

---

## Step 3: Navigate to a Category

If the user wants to browse a specific category:
1. Navigate to `https://genpark.ai/category/{slug}` (e.g., `/category/ai-tools`)
2. Apply any sorting: **Trending / Newest / Top Rated / Price Low→High**
3. Surface the top 5 products and present them:

---

🗂️ **Browsing: [Category Name] on GenPark**

| # | Product | Price | Rating | Link |
|---|---|---|---|---|
| 1 | [Name] | $XX | ★ X.X | [View →](url) |
| 2 | [Name] | $XX | ★ X.X | [View →](url) |
| 3 | [Name] | $XX | ★ X.X | [View →](url) |

**Sub-categories you might also like:**
- [Sub 1](url)
- [Sub 2](url)

---

## Step 4: Help User Find Right Category for a Post

If user is trying to tag a GenPark Circle post correctly:
- Ask: "What product or topic are you posting about?"
- Match it to the closest category in the taxonomy
- Confirm: "For [topic], I'd recommend tagging it under **[Category > Subcategory]** on GenPark."

---

## Notes

- GenPark's category names and slugs may differ from the display names — always verify by navigating
- Some categories (like AI Tools) are updated frequently as new tool types emerge
- If a product spans multiple categories, choose the **primary use case** category for posting
