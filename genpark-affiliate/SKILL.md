---
name: genpark-affiliate
description: "Use this skill when the user wants to generate GenPark affiliate or referral links for products, track their referral performance, or build a shareable referral campaign. Triggers: 'generate a GenPark affiliate link', 'how do I earn from GenPark referrals', 'get my GenPark referral link for this product', 'build a referral campaign on GenPark', 'track my GenPark affiliate clicks', 'monetize my GenPark posts'. NOT for: general content growth strategy (use genpark-ambassador) or writing reviews (use genpark-review-writer)."
metadata: {"openclaw": {"emoji": "💰", "requires": {}}}
---

# GenPark Affiliate — Generate Referral Links & Track Campaigns

Generate **GenPark** affiliate/referral links for products, build campaigns, and track how your referral traffic is performing — so you can monetize your GenPark content.

## When to Use

✅ **USE this skill when:**
- User is a content creator or influencer wanting to earn from GenPark recommendations
- User wants to generate a referral link for a specific product
- User wants to see their referral performance dashboard
- User is building a campaign (newsletter, blog, Circle posts) and needs trackable links

❌ **DON'T use this skill when:**
- User wants to grow followers without monetization → use `genpark-ambassador`
- User wants to write a review → use `genpark-review-writer`
- User wants product collections without affiliate tracking → use `genpark-collections`

---

## Step 1: Access the Affiliate Program

1. Navigate to `https://genpark.ai/affiliate` or `https://genpark.ai/creators`
2. If not enrolled: walk the user through sign-up:
   - Apply with their GenPark username and a brief description of their platform (blog, newsletter, social)
   - Note: GenPark typically approves creators with 100+ followers or an established content platform
3. If enrolled: navigate to the **Affiliate Dashboard**

---

## Step 2: Generate an Affiliate Link

For a specific product:
1. Navigate to the product page on GenPark
2. Look for the **"Share & Earn"** or **"Get Affiliate Link"** button
3. Copy the generated link — it should contain a tracking parameter, e.g.:
   ```
   https://genpark.ai/product/{slug}?ref={username}
   ```
4. For multiple products at once, use the affiliate dashboard's **bulk link generator** if available

Present to user:

---

💰 **GenPark Affiliate Link Generated**

**Product:** [Product Name]
**Your Affiliate Link:** `https://genpark.ai/product/{slug}?ref={username}`
**Estimated Commission:** [XX%] per sale (check your tier in the dashboard)
**Cookie Duration:** 30 days (user earns you credit for 30 days after clicking)

**Short link:** [Copy →] *(if GenPark provides a link shortener)*

---

## Step 3: Build a Campaign

For organized campaigns (newsletter, blog, social post):

### Campaign Link Table

| Product | Affiliate URL | Campaign Tag | Use In |
|---|---|---|---|
| [Product A] | `?ref=username&utm_campaign=blog-march` | blog-march | Blog post |
| [Product B] | `?ref=username&utm_campaign=newsletter-wk12` | newsletter-wk12 | Email digest |
| [Product C] | `?ref=username&utm_campaign=circle-post` | circle-post | GenPark Circle |

Add UTM parameters if supported:
```
https://genpark.ai/product/{slug}?ref={username}&utm_source={source}&utm_campaign={campaign}
```

---

## Step 4: Check Performance Dashboard

1. Navigate to `https://genpark.ai/affiliate/dashboard`
2. Extract:
   - Total clicks (all-time / this month)
   - Conversions (clicks → purchases)
   - Conversion rate
   - Total earnings (pending / paid)
   - Top-performing products
3. Present:

---

📊 **Your GenPark Affiliate Performance**

| Metric | This Month | All-Time |
|---|---|---|
| Clicks | N | N |
| Conversions | N | N |
| Conversion Rate | X.X% | X.X% |
| Earnings | $XX | $XX |

**Top Product:** [Product Name] — N conversions

**Payout status:** [Pending / On track for payout on date]

---

## Step 5: Embed Links in Content

If the user wants to post their affiliate links on GenPark Circle:
→ Hand off to `genpark-ambassador` for post drafting with the affiliate links embedded

If sharing via newsletter:
→ Suggest wrapping with a disclosure: *"This link contains an affiliate referral — I may earn a commission at no extra cost to you."*

---

## Notes

- Always disclose affiliate relationships — GenPark's TOS requires it, and it builds trust
- Products with higher price points tend to generate more commission even at lower conversion rates
- Combine with `genpark-collections` to create a curated affiliate collection page
- High-upvoted Circle posts with affiliate links can be a compound earning asset long after posting
