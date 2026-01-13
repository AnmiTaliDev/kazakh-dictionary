# AI Assistant Instructions for Kazakh Dictionary Project

## Overview
This is an open-source (CC0) Kazakh language dictionary with etymology, morphological roots, and multiple Latin transcription systems. You are helping to expand and maintain this dictionary.

## Project Structure
```
dictionary/
├── а/
│   └── word.yaml
├── ә/
│   └── word.yaml
├── б/
│   └── word.yaml
...
└── я/
    └── word.yaml
```

Each Cyrillic letter has its own directory. Each word is stored in a separate YAML file named `{word}.yaml`.

## YAML Structure

### Required Fields
```yaml
- id: <unique_number>           # Unique identifier (integer)
  word: "слово"                  # Word in Cyrillic
  parent_id: null                # ID of parent word (for derivatives) or null
  type: "noun"                   # Part of speech
  transcription: "IPA"           # IPA transcription
  latin_2017: "text"             # Latin script (2017 standard)
  latin_2021: "text"             # Latin script (2021 standard)
  latin_my: "text"               # AnmiTaliDev's Latin proposal
  root_word: "root"              # Morphological root
  etymology: "source"            # Etymology source
  history: "detailed history"    # Detailed etymological history
  definitions:
    - meaning: "definition"      # Definition in Kazakh
      translation_ru: "перевод"  # Russian translation
      translation_en: "translation" # English translation
      examples:                  # Usage examples (optional but recommended)
        - kk: "Kazakh sentence"
          ru: "Русское предложение"
          en: "English sentence"
```

### Optional Fields
```yaml
  synonyms:                      # List of synonyms
    - word_id: <id>              # ID if word exists in dictionary
      word: "synonym"            # The synonym word
      note: "context note"       # Optional usage note

  antonyms:                      # List of antonyms
    - word_id: <id>
      word: "antonym"
```

### For Derivative Words
```yaml
  parent_id: <id>                # ID of root word
  relation: "type"               # Type of derivation: "profession", "place", "diminutive", etc.
```

## Latin Transcription Systems

### latin_my (AnmiTaliDev's Proposal)
Reference: `references/latin-proposal/character_mapping.md`

Key mappings:
- **Vowels**: а→a, ә→ä, е→e, і→ı, и→i, о→o, ө→ö, ұ→ū, ү→ü, у→u, ы→y
- **Consonants**: ж→j, ғ→ğ, қ→q, ң→ŋ, ш→ş, щ→š, ч→č, й→î
- **Special**: ь→' (apostrophe), ъ→(omitted)

**IMPORTANT**:
- Use **y** for Cyrillic **ы** (not ı)
- Use **ı** (dotless i) for Cyrillic **і**
- Example: жақсы → jaqsy (NOT jaqsı)

## Word Types (type field)
- `noun` - зат есім
- `verb` - етістік
- `adjective` - сын есім
- `adverb` - үстеу
- `pronoun` - есімдік
- `numeral` - сан есім
- `postposition` - септеулік шылау
- `conjunction` - жалғаулық
- `particle` - демеулік
- `interjection` - одағай

## Rules and Best Practices

### 1. File Organization
- Place each word in directory matching its FIRST Cyrillic letter
- One word per file
- File name must match the word: `кітап.yaml`, `жақсы.yaml`

### 2. IDs
- Use unique sequential IDs
- Check existing IDs before assigning new ones
- Never reuse IDs

### 3. Parent-Child Relationships
**CRITICAL RULE**: Only derivative words should reference parent words!

✅ **CORRECT**:
```yaml
# кітап.yaml - root word
- id: 1
  word: "кітап"
  parent_id: null
  # NO related_words field!

# кітапшы.yaml - derivative
- id: 4
  word: "кітапшы"
  parent_id: 1           # references кітап
  relation: "profession"
  root_word: "кітап"
```

❌ **WRONG** - Don't add related_words to root words:
```yaml
- id: 1
  word: "кітап"
  related_words:        # ❌ DON'T DO THIS!
    - word: "кітапшы"
```

### 4. Synonyms and Antonyms
- Always provide `word_id` if the word exists in the dictionary
- Use `null` for `word_id` if word doesn't exist yet
- Add contextual notes when needed

### 5. Examples
- Provide at least 1-2 examples per definition
- Include all three languages: kk, ru, en
- Use natural, common usage

### 6. Etymology
- Be accurate and cite sources when possible
- For Turkic cognates, mention related words in other Turkic languages
- For loanwords, specify source language and original form

### 7. Transcription Guidelines
- IPA: Use standard IPA notation
- latin_2017 & latin_2021: Follow official Kazakhstan standards
- latin_my: **Always check** `references/latin-proposal/character_mapping.md`

### 8. Quality Standards
- Double-check all transcriptions
- Verify etymologies with reliable sources
- Ensure consistency in formatting
- Add examples for better understanding

## Common Mistakes to Avoid

1. ❌ Mixing up **y** (ы) and **ı** (і) in latin_my
2. ❌ Adding `related_words` to root words
3. ❌ Forgetting to set `parent_id` for derivatives
4. ❌ Missing English translations
5. ❌ Incomplete etymology information
6. ❌ Wrong directory for word placement

## Workflow for Adding New Words

1. Check if word already exists
2. Determine appropriate directory (first letter)
3. Assign unique ID
4. Fill all required fields
5. Add examples and contextual information
6. If derivative: set `parent_id` and `relation`
7. Cross-reference synonyms/antonyms
8. Verify all transcriptions
9. Review for consistency

## Resources

- Latin proposal reference: `references/latin-proposal/`
- Existing words for reference: `dictionary/` subdirectories
- Character mapping: `references/latin-proposal/character_mapping.md`

## License
All contributions are released under CC0 (Public Domain).

---
© 2026 AnmiTaliDev <anmitali198@gmail.com>
