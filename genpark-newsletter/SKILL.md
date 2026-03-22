---
name: genpark-newsletter
description: "Use this skill when the user wants to manage their GenPark email newsletter subscription — subscribe, unsubscribe, change frequency, preview the latest issue, or share newsletter content. Triggers: 'subscribe to GenPark newsletter', 'unsubscribe GenPark digest email', 'change GenPark email frequency', 'show me the latest GenPark newsletter', 'what's in GenPark's weekly digest', 'stop GenPark emails'. NOT for: viewing the GenPark daily digest on-platform (use genpark-daily-digest)."
metadata: {"openclaw": {"emoji": "📧", "requires": {}}}
---

# GenPark Newsletter — Manage Email Digest Subscriptions

Manage your **GenPark** email newsletter: subscribe, unsubscribe, change frequency, preview the latest issue, and extract share-worthy content.

## When to Use

✅ **USE this skill when:**
- User wants to subscribe or unsubscribe from GenPark email digests
- User wants to change how often they get GenPark emails (daily / weekly / never)
- User wants to preview what's in the latest newsletter
- User wants to share or react to a newsletter highlight in GenPark Circle

❌ **DON'T use this skill when:**
- User wants to see what's trending on GenPark right now → use `genpark-daily-digest`
- User wants to manage their GenPark account broadly → use `genpark-profile-optimizer`

---

## Detecting Intent

| Intent | Trigger Words |
|---|---|
| **Subscribe** | "subscribe", "sign up", "get emails", "opt in" |
| **Unsubscribe** | "unsubscribe", "stop emails", "opt out", "too many emails" |
| **Change frequency** | "less often", "daily instead", "weekly digest", "change frequency" |
| **Preview** | "show me", "what's in", "latest issue", "this week's email" |
| **Share** | "share this", "post this to circle", "forward" |

---

## Action: Subscribe

1. Navigate to `https://genpark.ai/settings/notifications` (or email preferences page)
2. Find **Email Digest** or **Newsletter** toggle
3. Enable it and set preferred frequency:
   - **Daily Digest** (every morning, top picks from past 24h)
   - **Weekly Digest** (every Monday, weekly roundup)
   - **Major launches only** (low frequency, only when something big happens)
4. Confirm email address is correct
5. Report: "✅ Subscribed to GenPark [Frequency] Digest at [email]."

---

## Action: Unsubscribe

1. Navigate to `https://genpark.ai/settings/notifications`
2. Toggle off **Email Digest / Newsletter**
3. Alternatively, click the unsubscribe link at the bottom of any GenPark email
4. Confirm: "✅ Unsubscribed from GenPark emails. You can re-subscribe anytime in Settings → Notifications."

---

## Action: Change Frequency

1. Navigate to notification settings
2. Find frequency selector
3. Update to user's preference
4. Save and confirm

---

## Action: Preview Latest Newsletter

1. Navigate to `https://genpark.ai/digest` or check the user's email for the latest issue
2. Extract key highlights:
   - 🔥 Most upvoted product this week
   - 🆕 New AI tool launches featured
   - 💬 Top GenPark Circle discussion
   - 🏷️ Best deal highlighted
3. Present as:

---

📧 **Latest GenPark Digest — [Week of Date]**

| Section | Highlight |
|---|---|
| 🔥 Top Product | [Name](url) |
| 🆕 New Launch | [Tool name](url) |
| 💬 Hot Discussion | [Thread title](url) |
| 🏷️ Best Deal | [Product name](url) — XX% off |

---

## Action: Share Newsletter Content

If user wants to share a newsletter item to GenPark Circle:
1. Identify the product/story they want to share
2. Draft a Circle post using `genpark-ambassador` format
3. Submit using the `genpark-circle` skill

---

## Notes

- GenPark email digest is usually sent 7–8am local time if daily, or Monday morning if weekly
- The digest email often contains exclusive deals not shown on the website
- If the user's email provider filters GenPark to promotions, recommend whitelisting `digest@genpark.ai`
