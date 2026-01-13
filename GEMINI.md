# Gemini AI Instructions for Kazakh Dictionary

## Project Context
Open-source Kazakh-Russian-English dictionary (CC0 license) with etymological data and multiple Latin transcription systems including AnmiTaliDev's proposal.

## File Structure
- Words organized by first Cyrillic letter: `dictionary/{letter}/{word}.yaml`
- One YAML file per word
- Latin transcription reference: `references/latin-proposal/character_mapping.md`

## YAML Schema

```yaml
- id: integer                    # Unique ID
  word: "cyrillic_word"          # Kazakh word in Cyrillic
  parent_id: integer|null        # For derivatives only
  type: string                   # Part of speech
  transcription: "IPA"           # IPA phonetic notation
  latin_2017: "text"             # 2017 Latin standard
  latin_2021: "text"             # 2021 Latin standard
  latin_my: "text"               # AnmiTaliDev's system
  root_word: "root"              # Morphological root
  etymology: "source"            # Brief etymology
  history: "text"                # Detailed history
  definitions:
    - meaning: "kazakh_def"
      translation_ru: "russian"
      translation_en: "english"
      examples:                  # Optional
        - kk: "sentence"
          ru: "предложение"
          en: "sentence"
  synonyms:                      # Optional
    - word_id: integer|null
      word: "synonym"
      note: "context"            # Optional
  antonyms:                      # Optional
    - word_id: integer|null
      word: "antonym"
```

## Critical Rules

### 1. Latin Transcription (latin_my)
**Must read**: `references/latin-proposal/character_mapping.md`

Key differences from other systems:
- Cyrillic **ы** → Latin **y** (NOT ı)
- Cyrillic **і** → Latin **ı** (dotless i)
- Cyrillic **ә** → Latin **ä**
- Cyrillic **ғ** → Latin **ğ**
- Cyrillic **ң** → Latin **ŋ**
- Cyrillic **ө** → Latin **ö**
- Cyrillic **ұ** → Latin **ū**
- Cyrillic **ү** → Latin **ü**

Example: жақсы → jaqsy (correct), NOT jaqsı (wrong)

### 2. Word Relations
**NEVER** add `related_words` field to root words. Only derivatives use `parent_id`.

Root word (correct):
```yaml
- id: 1
  word: "кітап"
  parent_id: null
  # No related_words!
```

Derivative (correct):
```yaml
- id: 4
  word: "кітапшы"
  parent_id: 1
  relation: "profession"
  root_word: "кітап"
```

### 3. Part of Speech Types
- `noun`, `verb`, `adjective`, `adverb`, `pronoun`, `numeral`
- `postposition`, `conjunction`, `particle`, `interjection`

### 4. Required Fields
All fields in the schema are required except:
- `examples` (optional but recommended)
- `synonyms` (optional)
- `antonyms` (optional)
- `note` in synonyms/antonyms (optional)

### 5. ID Management
- Sequential integers starting from 1
- Check existing IDs before assigning
- Never reuse or duplicate IDs

## Quality Checklist

Before submitting a word entry:

- [ ] Correct directory (first Cyrillic letter)
- [ ] Unique ID assigned
- [ ] All required fields present
- [ ] IPA transcription accurate
- [ ] latin_my follows AnmiTaliDev's system (check mapping!)
- [ ] Etymology verified
- [ ] At least 1 example per definition
- [ ] English translation provided
- [ ] For derivatives: `parent_id` and `relation` set
- [ ] Synonyms/antonyms cross-referenced with `word_id`

## Common Errors to Avoid

1. Confusing y/ı in latin_my transcription
2. Adding `related_words` to base words
3. Missing English translations
4. Wrong directory placement
5. Duplicate IDs
6. Incomplete etymology
7. Missing `parent_id` on derivatives

## Examples

See existing entries:
- `dictionary/к/кітап.yaml` - Root word
- `dictionary/к/кітапшы.yaml` - Derivative
- `dictionary/ж/жақсы.yaml` - Adjective with synonyms
- `dictionary/ж/жаман.yaml` - Adjective with antonym

## Resources
- Character mapping: `references/latin-proposal/character_mapping.md`
- Project repository: https://github.com/AnmiTaliDev/kazakh-dictionary
- Latin proposal: https://github.com/AnmiTaliDev/new-kazakh-latin-proposal

## License
CC0 - Public Domain

---
© 2026 AnmiTaliDev <anmitali198@gmail.com>
