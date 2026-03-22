---
name: genpark-deal-hunter
description: "Use this skill when the user wants to find deals, discounts, flash sales, coupon codes, or limited-time offers on GenPark. Triggers: 'find me a deal on GenPark', 'any discounts on GenPark?', 'GenPark flash sale', 'coupon code for GenPark', 'cheapest price on GenPark', 'what's on sale on GenPark today'. NOT for: tracking price changes over time (use genpark-price-tracker) or restock alerts (use genpark-restock-alert)."
metadata: {"openclaw": {"emoji": "🏷️", "requires": {}}}
---

# GenPark Deal Hunter — Flash Sales, Discounts & Coupon Codes

Surface the best active deals, discounts, and limited-time offers on **GenPark** (genpark.ai). This skill scans GenPark's Deals section and product pages to find genuine savings — not just low base prices.

## When to Use

✅ **USE this skill when:**
- User asks for deals, discounts, or sales on GenPark
- User has a specific product and wants to know if there's a coupon
- User wants today's / this week's best GenPark offers
- User is on a tight budget and wants maximum value

❌ **DON'T use this skill when:**
- User wants to track a price over time → use `genpark-price-tracker`
- User wants restock notifications → use `genpark-restock-alert`
- User is comparing two specific products at full price → use `genpark-compare`

---

## Step 1: Understand the Deal Request

Clarify if needed:
- **Specific product?** Or open to any category?
- **Budget range?** (helps filter noise)
- **Deal type preference?** (percentage off, flash sale, coupon code, bundle deal, free shipping)
- **Urgency?** ("today only" vs. "this week")

---

## Step 2: Scan GenPark Deals

Use your **browser**:

1. Navigate to `https://genpark.ai/deals` — scan all featured deals
2. If user has a specific product: navigate to that product's page and check:
   - Price badge (e.g., "20% OFF", "Limited Deal")
   - Available coupon codes in the product description
   - Bundle pricing options
3. Check GenPark Circle for posts tagged `#deals` or `#sale` in the last 24 hours

Look for:
| Signal | What to Check |
|---|---|
| % discount badge | Shown next to price on product cards |
| Flash sale timer | Countdown visible on product page |
| Coupon code field | On checkout page or product description |
| Bundle offer | "Buy X get Y" section |
| Community-sourced | Circle posts with deal codes |

---

## Step 3: Present the Deals

Format findings as:

---

🏷️ **GenPark Deals — [Category / "Today's Best"]**

**🔥 Top Deal:**
**[Product Name](url)** | ~~$XX~~ → **$XX** (XX% off)
> [What the deal is — e.g., "Limited flash sale, ends in 4h"]
> Coupon: `SAVE20` (if available)

**More Deals:**
| Product | Original | Deal Price | Discount | Expires |
|---|---|---|---|---|
| [Name](url) | $XX | $XX | XX% | [time/date or "ongoing"] |
| [Name](url) | $XX | $XX | XX% | [time/date or "ongoing"] |

---

If no active deal found for a product:
> ⚠️ No active discount found for [Product]. The lowest recent price was $XX on [date].
> 💡 Want me to set a price alert for when it drops? (use `genpark-price-alert`)

---

## Step 4: Offer Next Actions

- "Want me to set a price alert so you don't miss the next sale?"
- "Should I add any of these to your wishlist before the sale ends?"
- "Want me to find similar products that are currently discounted?"

---

## Notes

- GenPark flash sales often expire within 2–24 hours — always note urgency in the response
- Coupon codes found in Circle posts should be verified on the checkout page before presenting
- If GenPark shows a "Compare at" price, note it may be the manufacturer's list price, not a real discount
- For recurring buyers, suggest combining with `genpark-price-tracker` to catch the historical low
