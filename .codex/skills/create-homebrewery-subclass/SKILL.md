---
name: create-homebrewery-subclass
description: Convert D&D 5e/5.5e subclass drafts into Homebrewery V3-compatible markdown for Homebrewery/NaturalCrit PDF generation. Use when Codex needs to format homebrew subclass source files, especially files under homebrews, as Homebrewery markdown while preserving rules text and feature mechanics.
---

# Create Homebrewery Subclass

## Workflow

1. Read the plain-language subclass source first. Treat the requested source language or file as authoritative; use translations or older versions only as references.
2. Preserve all mechanics, spell names, feature names, limitations, recovery timing, action economy, ranges, and level order unless the user explicitly requests rules edits.
3. Convert structure into Homebrewery V3 markdown:
   - Use `#` for the subclass title, `##` for major sections, `###` for subclass feature headings, and `####` for feature options or sub-benefits.
   - Use italic or classed subtitle text below the title when the source has a tagline.
   - Convert spell lists and similar tabular material into markdown tables.
   - Convert sidebars into `{{note ... }}` blocks and place them exactly where requested.
   - Use `\column` or `\page` only when it improves readable PDF flow; do not force page furniture into short brews.
4. Re-read the completed markdown and verify that no reference-only language or draft text leaked into the output.

## Homebrewery V3 Patterns

Use these patterns from the project example `homebrews/homebrewery example/pdf example.md`:

```markdown
# Subclass Title

{{text-align:center,font-style:italic
Subtitle or motto
}}

## Tenets of the Oath

**Tenet Name.** Tenet text.

{{note
##### Sidebar Title

Sidebar text.
}}

| Paladin Level | Spells |
|:---:|:---|
| 3 | *Feather Fall*, *Guiding Bolt* |

\column

### Level 3: Feature Name

Feature text.

#### Sub-Benefit Name
Sub-benefit text.
```

Curly-brace blocks start with `{{class-or-style` and close with `}}` on their own line. Standard markdown tables are preferred for simple D&D rules tables. Avoid raw HTML unless a Homebrewery V3 block cannot express the layout.

## Quality Bar

- Keep the Homebrewery markdown readable as a source file, not only as rendered PDF.
- Do not invent art, images, credits, page numbers, or footnotes unless the user asks for them.
- Keep English output fully English when the English source is authoritative.
- After editing, check heading order, table row count, requested note placement, and presence of every source feature heading.
