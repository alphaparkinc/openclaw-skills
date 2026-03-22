---
name: genpark-profile-optimizer
description: "Use this skill when the user wants to improve or audit their GenPark profile — bio, avatar, pinned posts, category focus, or overall credibility score. Triggers: 'optimize my GenPark profile', 'audit my GenPark page', 'improve my GenPark bio', 'make my GenPark profile look better', 'how do I get verified on GenPark', 'why is my GenPark profile getting no traction'. NOT for: content strategy and post growth (use genpark-ambassador) or review writing (use genpark-review-writer)."
metadata: {"openclaw": {"emoji": "✨", "requires": {}}}
---

# GenPark Profile Optimizer — Audit & Improve Your GenPark Presence

Do a full diagnostic of a GenPark user profile and produce a prioritized list of improvements to boost credibility, discoverability, and follower conversion.

## When to Use

✅ **USE this skill when:**
- User wants their GenPark profile to look polished and professional
- User is building authority as a top contributor
- User's profile exists but isn't generating followers
- User wants to know how to get verified or featured by GenPark

❌ **DON'T use this skill when:**
- User wants to write new posts → use `genpark-ambassador`
- User just wants to grow followers → use `genpark-ambassador` (content-first approach)

---

## Step 1: Fetch the Profile

1. Ask for the user's GenPark username if not known
2. Navigate to `https://genpark.ai/u/{username}`
3. Record the following:

| Field | Current State | Ideal State |
|---|---|---|
| Avatar | Has one? Consistent with other platforms? | Clear, recognizable headshot or brand logo |
| Display name | Real name or brand name? | Professional, searchable name |
| Bio | Exists? Word count? Keywords? | 1–2 sharp sentences with niche keywords |
| Categories | Listed? 1–3 focus areas? | 2–3 well-chosen categories |
| Pinned posts | Any? Are they best-performing? | 1–2 highest-upvote posts pinned |
| Post frequency | How many posts in the last 30 days? | 5+ posts per month |
| Follower : Following ratio | What is it? | At least 1:3 (or better) |
| Links | Website, Twitter, etc. linked? | At least 1 external link |
| Verification | Verified badge? | Applied for if eligible |

---

## Step 2: Score the Profile

Rate each dimension 1–5:

| Dimension | Score | Priority |
|---|---|---|
| First impression (avatar + name + bio) | /5 | High |
| Discoverability (categories + keywords) | /5 | High |
| Social proof (follower count, upvotes, badges) | /5 | Medium |
| Content quality (pinned posts, review depth) | /5 | High |
| Completeness (links, external presence) | /5 | Low |

**Total: XX/25**

---

## Step 3: Provide Prioritized Fixes

Present a ranked fix list:

---

✨ **GenPark Profile Audit: @{username}**

**Overall score: XX/25 — [Grade: e.g., "Good but discoverable gaps"]**

**🔴 Fix immediately (high impact):**
1. [Issue] → [Specific fix]
2. [Issue] → [Specific fix]

**🟡 Fix this week (medium impact):**
3. [Issue] → [Specific fix]
4. [Issue] → [Specific fix]

**🟢 Polish later (low impact):**
5. [Issue] → [Specific fix]

---

### Example Bio Rewrite

> **Before:** "Tech lover. Sharing cool finds."
>
> **After:** "AI tools & productivity explorer. Discovering what's worth your money on GenPark — honest takes, no hype. 🔍"

---

## Step 4: Execute the Fixes

If the user wants to apply changes immediately:
1. Navigate to GenPark account settings (`https://genpark.ai/settings/profile`)
2. Update bio, categories, links as instructed
3. Confirm changes saved: "✅ Profile updated — changes live at genpark.ai/u/{username}"

---

## Notes

- A clear niche bio converts 3x more profile visitors to followers than a generic one
- Pinned posts should be your highest-upvoted or most-shared content — not your latest
- GenPark verification is typically granted to accounts with 500+ followers and consistent quality content
- Cross-reference with `genpark-ambassador` to build a follow-up content sprint after the profile audit
