# AI Assistant Instructions for Kazakh Dictionary Project

## Overview
This is an open-source (CC0) Kazakh-Russian-English dictionary with etymological data, morphological roots, and multiple Latin transcription systems. You are helping to expand and maintain this dictionary.

## Project Structure
```
dictionary/
├── а/
│   └── word.yaml
├── ә/
│   └── word.yaml
...
└── я/
    └── word.yaml
```

Words are organized by their **first Cyrillic letter**. Each word is stored in a separate YAML file named `{word}.yaml`.

## YAML Schema (YALF format, v1.0.0)

Format spec: `3rd/docs/docs/specification.md`

### Schema Overview
```yaml
- id: integer                    # Unique ID (Required)
  word: "cyrillic_word"          # Kazakh word in Cyrillic (Required)
  parent_id: integer|null        # ID of parent word (for derivatives only) or null (Required)
  type: string                   # Part of speech (Required)
  transcription: "IPA"           # IPA phonetic notation (Required)
  writing_systems:               # Latin script variants (Required)
    latin_2017: "text"           # 2017 Latin standard
    latin_2021: "text"           # 2021 Latin standard
    latin_my: "text"             # AnmiTaliDev's Latin proposal
  root_word: "root"              # Morphological root (Required)
  etymology: "source"            # Brief etymology (Required)
  history: "text"                # Detailed etymological history (Required)
  definitions:                   # (Required)
    - meaning: "kazakh_def"      # Definition in Kazakh
      translation_ru: "russian"  # Russian translation
      translation_en: "english"  # English translation
      examples:                  # Optional but highly recommended
        - kk: "sentence"         # Kazakh example
          ru: "предложение"      # Russian translation
          en: "sentence"         # English translation
  synonyms:                      # Optional
    - word_id: integer|null      # ID if word exists, else null
      word: "synonym"
      note: "context"            # Optional usage note
  antonyms:                      # Optional
    - word_id: integer|null
      word: "antonym"
```

### For Derivative Words
```yaml
  parent_id: <id>                # ID of root word
  relation: "type"               # Type of derivation: "profession", "place", "diminutive", etc.
```

## Critical Rules

### 1. Latin Transcription (latin_my)
Reference: `references/latin-proposal/character_mapping.md`

Key differences from other systems:
- **Cyrillic ы → Latin y** (NOT ı)
- **Cyrillic і → Latin ı** (dotless i)
- Cyrillic **ә** → Latin **ä**
- Cyrillic **ғ** → Latin **ğ**
- Cyrillic **ң** → Latin **ŋ**
- Cyrillic **ө** → Latin **ö**
- Cyrillic **ұ** → Latin **ū**
- Cyrillic **ү** → Latin **ü**
- Cyrillic **ж** → Latin **j**
- Cyrillic **ш** → Latin **ş**
- Cyrillic **щ** → Latin **š**
- Cyrillic **ч** → Latin **č**
- Cyrillic **й** → Latin **î**

Example: **жақсы** → **jaqsy** (correct), NOT jaqsı (wrong)

### 2. Word Relations & Parent-Child Relationships
**CRITICAL RULE**: NEVER add a `related_words` field to root words. Only derivatives use `parent_id` and `relation`.

✅ **CORRECT Root Word**:
```yaml
- id: 1
  word: "кітап"
  parent_id: null
```

✅ **CORRECT Derivative**:
```yaml
- id: 4
  word: "кітапшы"
  parent_id: 1           # References кітап
  relation: "profession"
  root_word: "кітап"
```

### 3. ID Management
- Use unique sequential integers starting from 1.
- Always check existing IDs in the `dictionary/` tree before assigning a new one.
- Never reuse or duplicate IDs.

### 4. Part of Speech Types
- `noun`, `verb`, `adjective`, `adverb`, `pronoun`, `numeral`
- `postposition`, `conjunction`, `particle`, `interjection`

## Verification & Anti-Hallucination Rules

To ensure the highest quality and accuracy of the dictionary, all AI assistants MUST follow these verification steps:

1. **Verify Meaning**: Before generating a definition, use web search to confirm the word's usage and nuances in Kazakh. Cross-reference with reliable dictionaries (e.g., Sozdik.kz, Til-Qural).
2. **Validate Etymology & History**: 
    - NEVER guess the origin of a word. 
    - If etymological data is not found in reliable sources, use an empty string `""` or explicitly state that the origin is unknown.
    - Research Turkic cognates to verify roots.
    - Check for loanword sources (Arabic, Persian, Russian, etc.) and original forms.
3. **Prevent Hallucinations**:
    - Do not invent IPA transcriptions; use established phonetic rules for Kazakh.
    - Do not make up example sentences that use the word in an unnatural or incorrect context.
    - If you are unsure about a specific field, state it clearly instead of fabricating data.
4. **Source Paraphrasing**: Always paraphrase information from sources like Wikipedia or specialized linguistic sites to avoid direct plagiarism, while maintaining technical accuracy.

## Quality Checklist & Workflow

Before submitting a word entry:

- [ ] **Correct Directory**: Placed in `dictionary/{first_letter}/`.
- [ ] **Unique ID**: Verified no collision with existing files.
- [ ] **Required Fields**: All fields from the schema are present (use empty strings for `etymology`/`history` if unknown).
- [ ] **IPA Transcription**: Accurate phonetic notation.
- [ ] **latin_my Transcription**: Strictly follows AnmiTaliDev's system (check `y` vs `ı`!).
- [ ] **Translations**: Kazakh, Russian, AND English provided for all definitions.
- [ ] **Examples**: At least 1 usage example per definition recommended.
- [ ] **Derivatives**: `parent_id` and `relation` correctly set.
- [ ] **Synonyms/Antonyms**: Cross-referenced with `word_id` if available.

## Common Errors to Avoid

1. ❌ Mixing up **y** (ы) and **ı** (і) in latin_my.
2. ❌ Adding `related_words` to root words.
3. ❌ Forgetting to set `parent_id` for derivatives.
4. ❌ Missing English translations.
5. ❌ Wrong directory placement (e.g., placing "әке" in `dictionary/а/`).
6. ❌ Duplicate IDs.
7. ❌ **Manually updating `LIST.md`**: This file is updated automatically by a GitHub Action using `scripts/update_list.py`. DO NOT edit it.

## Resources
- Character mapping: `references/latin-proposal/character_mapping.md`
- Project repository: https://github.com/AnmiTaliDev/kazakh-dictionary
- Latin proposal: https://github.com/AnmiTaliDev/new-kazakh-latin-proposal

## License
All contributions are released under **CC0 (Public Domain)**.

---
© 2026 AnmiTaliDev <anmitali198@gmail.com>
