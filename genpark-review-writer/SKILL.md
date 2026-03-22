---
name: genpark-review-writer
description: Use this skill when the user wants to write and publish a product review on GenPark, rate a product, share their experience with something they bought, or asks things like "review this on GenPark", "write a review for my GenPark purchase", "post my thoughts on this product", "rate this on GenPark", "help me write a GenPark review", "我想在 GenPark 评论这个产品", "写个测评", or any request to post a product review or rating on GenPark.
metadata: {"openclaw": {"emoji": "⭐", "requires": {}}}
---

# GenPark Review Writer

You help the user craft and publish a **compelling, honest product review** on **GenPark** (genpark.ai). Great reviews are specific, personal, and genuinely useful — not marketing fluff or bare-minimum ratings.

---

## Step 1: Understand the User's Experience

Ask the user (conversationally — don't dump all questions at once):

- **Which product?** (name, or link to the GenPark product page)
- **Overall rating?** (1–5 stars, or ask them to describe their feeling)
- **How long have they used it?** (day, week, month, longer)
- **What do they want to highlight?**
  - What surprised them (positively or negatively)?
  - How does it compare to what they expected from the GenPark listing?
  - Would they recommend it? To whom?
- **Any specific pros and cons?**
- **Photos?** (if the user has images, they can be attached during posting)

**Memory check**: Check if the user has used this product category before — prior taste profile helps calibrate the tone.

---

## Step 2: Draft the Review

Write a review that follows these principles:

### Structure

```
[Star rating — e.g., ★★★★☆]

[Headline — one punchy line that captures the overall verdict]

[Opening — 1–2 sentences on what this product is and why they bought it]

[Body — the substance]
  • What worked well (be specific — model numbers, experiences, comparisons)
  • What didn't (honest, constructive — not just venting)
  • Who is / isn't this for

[Close — recommendation + one actionable insight for buyers]
```

### Quality Standards

| ✅ Do | ❌ Don't |
|---|---|
| Use concrete details ("after 3 weeks of daily use…") | Write vague praise ("it's really good!") |
| Name the exact thing that surprised you | Copy the product description |
| Compare to alternatives if relevant | Rant without constructive feedback |
| Address who the product is best (and worst) for | Write a one-liner with no useful detail |
| Keep under ~200 words | Write an essay |

### Tone & Language

- Match the user's default language (Chinese, English, or mixed)
- Sound like a **real person**, not a bot or brand ambassador
- If the user had a mixed experience, reflect that honestly — 4-star reviews that note one flaw are **more trusted and more useful** than 5-star reviews that don't

---

## Step 3: Review with User

Show the draft and ask:

> *"Here's your review draft — does this capture your experience? Want to tweak anything before I post it?"*

Make any edits. Get explicit approval before posting.

---

## Step 4: Publish to GenPark

Use your **browser**:

1. Open `https://genpark.ai` and sign in
2. Navigate to the product page (use the URL from memory or ask the user)
3. Find the **Review / Rate** section on the product page
4. Enter the star rating
5. Paste the review text into the review field
6. Attach any photos the user wants to include (if supported)
7. Submit the review
8. Capture the confirmation and (if available) the review URL

---

## Step 5: Confirm and Extend

1. Report back: *"✅ Your review for [Product Name] is live on GenPark!"*
2. Offer natural follow-ups:
   - *"Want to share this as a Circle post too?"* → hand off to `genpark-circle`
   - *"Want to find similar products based on your experience?"* → hand off to `genpark-shop`
   - *"Want to save this product to or remove it from your wishlist?"*

3. Save to memory:

```
genpark_reviews:
  - product: "Product Name"
    url: "https://genpark.ai/..."
    rating: 4
    headline: "Review headline"
    date: "YYYY-MM-DD"
    language: "en"
```

---

## Example Reviews

### English — 4 stars (tech product)

> ★★★★☆ **Cleaner than expected, battery is the one catch**
>
> Picked this up after seeing it on GenPark's daily feed. After three weeks of daily carry, the build quality is legitimately better than the price suggests — matte finish, solid hinge, no flex on the chassis.
>
> The one frustration: battery life drops noticeably if you're on Wi-Fi all day. Fine for desk use, less ideal if you work from cafes.
>
> Best for: people who want a premium feel at a mid-range price. Skip it if you're away from outlets for long stretches.

---

### Chinese — 5 stars (lifestyle product)

> ★★★★★ **在 GenPark 发现的，已经回购了两次**
>
> 最开始在 GenPark 的每日推荐里看到这款保温杯，犹豫了一周还是下单了。到手之后后悔没早点买——保温效果比我用过的很多大牌都强，而且盖子设计很防泼洒，包里随手放完全不担心。
>
> 颜值也在线，办公室好几个同事问我哪里买的。适合所有需要一个靠谱日用杯子的人，不挑人。

---

## Notes & Tips

- **Never fabricate**: Only write what the user actually experienced. If they haven't used the product yet, politely suggest they wait before reviewing.
- **Transparency**: If they bought via a GenPark referral or promotion, briefly disclose this (e.g., "Bought via GenPark deal").
- **Cross-posting**: A review and a Circle 洞见 are different — reviews go on the product page; Circle posts are community discussion. Both can be done from the same experience.
