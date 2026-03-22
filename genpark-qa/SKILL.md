---
name: genpark-qa
description: "Use this skill when the user wants to ask a product question and get answers from GenPark's community Q&A or AI-synthesized product FAQs. Triggers: 'does [product] work with X?', 'ask the GenPark community about', 'what do GenPark users say about', 'any Q&A on GenPark for this product', 'is [product] compatible with', 'GenPark question about'. NOT for: reading full review summaries (use genpark-review-summarizer) or general search (use genpark-search)."
metadata: {"openclaw": {"emoji": "💬", "requires": {}}}
---

# GenPark Q&A — Community Product Questions & Answers

Get answers to product-specific questions from **GenPark's** community Q&A threads and AI-synthesized product FAQs. Surface what real buyers are asking — and what the community actually knows.

## When to Use

✅ **USE this skill when:**
- User has a specific question about a product (compatibility, setup, warranty, etc.)
- User wants to know what the GenPark community says about a specific aspect of a product
- User wants to see the most-asked questions on a product page
- User wants to post a new question to GenPark community

❌ **DON'T use this skill when:**
- User wants a full review summary → use `genpark-review-summarizer`
- User is comparing two products → use `genpark-compare`
- User wants general product search → use `genpark-shop`

---

## Step 1: Identify the Question

If not explicit, ask:
- **What product?** (name or URL)
- **What's your question?** (specific concern, compatibility, use case)

Common question types:
| Type | Example |
|---|---|
| Compatibility | "Does this work with Mac?" |
| Use case | "Is this good for video editing?" |
| Setup | "Is this hard to set up?" |
| Comparison | "How does this differ from [Product B]?" |
| After-sale | "What's the return policy?" |

---

## Step 2: Search Existing Q&A on GenPark

Use your **browser**:

1. Navigate to the product's GenPark listing: `https://genpark.ai/product/{slug}`
2. Scroll to the **Q&A section** or **Community tab**
3. Search existing questions for matches to the user's query
4. If an answer exists: extract and present it (with upvote count for credibility signal)
5. Also check the **AI FAQ panel** if available (GenPark auto-generates common FAQs for popular products)

---

## Step 3: Present Findings

### If Answer Found:

---

💬 **GenPark Q&A: [Product Name]**

**Your question:** "[User's question]"

**Community answer** (👍 N upvotes):
> "[Exact community answer or paraphrase]"
> — @username, [date]

**Additional answers:**
> "[Second answer if available]"

**AI Summary** (if GenPark provides one):
> "[Synthesized answer from multiple community responses]"

---

### If No Answer Found:

> ❓ No existing Q&A found for this question on GenPark.
>
> **Do you want me to:**
> 1. **Post your question** to the GenPark community on this product? (Estimated response time: a few hours to 1 day)
> 2. **Search GenPark Circle** for any discussion about this topic?
> 3. **Check other sources** (manufacturer site, Reddit) for an answer?

---

## Step 4: Post a New Question (If Requested)

1. Navigate to the product listing on GenPark
2. Scroll to the Q&A section
3. Click **Ask a Question**
4. Type the user's question clearly and specifically
5. Submit and confirm: "✅ Your question has been posted to GenPark for [Product Name]. We'll notify you when a community member responds."

---

## Notes

- Q&A answers with 10+ upvotes are highly reliable — weight them accordingly
- If GenPark's AI FAQ directly answers the question, note it's AI-synthesized (not a human response)
- For technical/compatibility questions, cross-reference with the manufacturer's official specs if GenPark Q&A is sparse
- For niche products, GenPark Circle discussions often contain more detail than the Q&A tab
