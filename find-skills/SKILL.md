---
name: find-skills
description: Helps users discover and install skills from the Vercel Labs repository.
---

# Find Skills

This skill helps users discover and install new skills from the Vercel Labs Skills repository. It acts as a guide to the available tools that can enhance their development workflow.

## When to Use This Skill
- The user asks about "available skills" or "what can you do?".
- The user needs a specific capability (e.g., "how can I test my database?") and you want to check if a skill exists for it.
- The user wants to "browse skills" or "search for a skill".

## What is the Skills CLI?
The Vercel Labs Skills repository is a collection of community-contributed skills that agents can use. By using this skill, you can help users find the right tools for their tasks.

## How to Help Users Find Skills

### Step 1: Understand What They Need
If the user's request is vague (e.g., "I need help with my project"), ask clarifying questions to identify the specific domain:
- Frontend/Backend development?
- Database management?
- Testing?
- Deployment?

### Step 2: Search for Skills
Use your browser tool to navigate to the [Vercel Labs Skills Repository](https://github.com/vercel-labs/skills).
- **List Skills**: Browse the `skills/` directory to see all available skills.
- **Search**: Use the repository's search bar or simply scan the directory names for relevant keywords (e.g., `test`, `db`, `react`, `deploy`).

### Step 3: Present Options to the User
Once you've found relevant skills:
1.  **Name**: Provide the name of the skill (matching the directory name).
2.  **Description**: Read the `SKILL.md` file of the skill to get a brief description of what it does.
3.  **Link**: Provide a direct link to the skill's folder in the repository.

### Step 4: Offer to Install
After presenting the options, ask the user if they would like you to install any of them. If they say yes, use the standard skill installation workflow (create task, inspect, download SKILL.md and resources).

## Common Skill Categories
-   **Frameworks**: `nextjs`, `react`, `vue`, `svelte`
-   **Languages**: `python`, `typescript`, `go`
-   **Tools**: `git`, `docker`, `prisma`, `jest`

## Tips for Effective Searches
-   Look for "meta-skills" that might include multiple capabilities.
-   Check the `README.md` of the root repository for featured or recommended skills.
-   Use broad terms if specific ones fail (e.g., search for "web" instead of "nextjs" if the latter yields no results, though "nextjs" is likely to exist).

## When No Skills Are Found
If you cannot find a specific skill for the user's request:
-   Suggest a related skill that might be helpful.
-   Offer to proceed using your general capabilities without a specialized skill.
-   Mention that they can contribute a new skill to the repository if they have a specific workflow in mind!
