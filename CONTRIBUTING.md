# Contributing to Kazakh Dictionary Project

Рақмет! Thank you for your interest in contributing to the Kazakh Language Heritage Project!

## 🌍 About This Project

This is an open-source Kazakh-Russian-English dictionary released under CC0 (Public Domain). Our goal is to preserve and document the Kazakh language with:
- Etymology and historical context
- Multiple Latin transcription systems
- Morphological roots and word relationships
- Usage examples in three languages

## 📋 Ways to Contribute

1. **Add new words** - Expand the dictionary
2. **Improve existing entries** - Add examples, fix errors, enhance etymologies
3. **Verify transcriptions** - Ensure accuracy of IPA and Latin scripts
4. **Translate** - Add or improve Russian/English translations
5. **Review** - Check submissions for accuracy

## 🗂️ Project Structure

```
kazakh-dictionary/
├── dictionary/
│   ├── а/
│   │   └── word.yaml
│   ├── ә/
│   ├── б/
│   └── ... (one directory per Cyrillic letter)
├── references/
│   └── latin-proposal/    (AnmiTaliDev's Latin transcription system)
├── CLAUDE.md              (AI assistant instructions)
├── GEMINI.md              (AI assistant instructions)
├── LIST.md                (A list of all words in the dictionary)
└── CONTRIBUTING.md        (this file)
```

## 📝 Entry Format

Each word is stored in a separate YAML file. Here's the complete structure:

```yaml
- id: 1                           # Unique number
  word: "кітап"                   # Word in Cyrillic
  parent_id: null                 # For derivatives: ID of root word
  type: "noun"                    # Part of speech
  transcription: "kɪˈtɑp"        # IPA phonetic transcription
  latin_2017: "kitap"            # 2017 Latin standard
  latin_2021: "kitap"            # 2021 Latin standard
  latin_my: "kıtap"              # AnmiTaliDev's proposal
  root_word: "кітап"             # Morphological root
  etymology: "Араб тілінен"      # Brief etymology
  history: "Detailed history..."  # Extended etymological info
  definitions:
    - meaning: "Басылым туындысы"
      translation_ru: "Книга"
      translation_en: "Book"
      examples:                   # At least 1-2 examples recommended
        - kk: "Мен кітап оқып жатырмын."
          ru: "Я читаю книгу."
          en: "I am reading a book."
  synonyms:                       # Optional
    - word_id: 5                  # ID if word exists
      word: "шығарма"
      note: "Для литературы"     # Optional context
  antonyms:                       # Optional
    - word_id: 10
      word: "opposite_word"
```

## 🔤 Parts of Speech (type)

- `noun` - зат есім (имя существительное)
- `verb` - етістік (глагол)
- `adjective` - сын есім (имя прилагательное)
- `adverb` - үстеу (наречие)
- `pronoun` - есімдік (местоимение)
- `numeral` - сан есім (числительное)
- `postposition` - септеулік шылау (послелог)
- `conjunction` - жалғаулық (союз)
- `particle` - демеулік (частица)
- `interjection` - одағай (междометие)

## 📖 Latin Transcription Systems

### latin_my (AnmiTaliDev's Proposal)

**Important mappings** (see `references/latin-proposal/character_mapping.md` for full table):

| Cyrillic | Latin | Example |
|----------|-------|---------|
| а | a | алма → alma |
| ә | ä | әке → äke |
| ы | y | жақсы → jaqsy |
| і | ı | кітап → kıtap |
| ғ | ğ | ғалым → ğalym |
| қ | q | қазақ → qazaq |
| ң | ŋ | таң → taŋ |
| ө | ö | өз → öz |
| ұ | ū | ұл → ūl |
| ү | ü | үй → üy |
| ж | j | жаз → jaz |
| ш | ş | шеш → şeş |
| щ | š | борщ → borš |
| ч | č | чай → čaî |

**Common mistake**: Don't confuse **y** (for ы) with **ı** (for і)!
- Correct: жақсы → jaqsy
- Wrong: жақсы → jaqsı

## 🔗 Word Relationships

### Root Words
Base words have `parent_id: null` and NO `related_words` field.

```yaml
- id: 1
  word: "кітап"
  parent_id: null
  # Don't add related_words here!
```

### Derivative Words
Derivatives reference their root word via `parent_id`:

```yaml
- id: 4
  word: "кітапшы"
  parent_id: 1              # Points to "кітап"
  relation: "profession"    # Type of derivation
  root_word: "кітап"
```

**Common relation types**:
- `profession` - кітап → кітапшы
- `place` - кітап → кітапхана
- `diminutive` - үй → үйшік
- `adjective` - noun → adj form
- `verbal_noun` - verb → noun form

## ✅ Submission Checklist

Before submitting your contribution:

- [ ] Word placed in correct directory (by first Cyrillic letter)
- [ ] File named correctly: `{word}.yaml`
- [ ] Unique ID assigned (check existing IDs!)
- [ ] All required fields filled
- [ ] IPA transcription verified
- [ ] All three Latin transcriptions provided
- [ ] `latin_my` follows AnmiTaliDev's system correctly
- [ ] Etymology researched and cited
- [ ] At least 1 example per definition
- [ ] English translation included
- [ ] For derivatives: `parent_id` and `relation` set
- [ ] Synonyms/antonyms cross-referenced with IDs
- [ ] Added the new word to LIST.md

## 🚀 How to Submit

### Option 1: GitHub Pull Request (Recommended)

1. Fork the repository
2. Create a new branch: `git checkout -b add-word-{word}`
3. Add your YAML file(s)
4. Commit: `git commit -m "Add word: {word}"`
5. Push: `git push origin add-word-{word}`
6. Create Pull Request on GitHub

### Option 2: GitHub Issue

If you're not comfortable with Git:

1. Go to [Issues](https://github.com/AnmiTaliDev/kazakh-dictionary/issues)
2. Create new issue with label "new-word"
3. Paste your YAML content
4. Someone will review and add it

### Option 3: Direct Contact

Email your contributions to: anmitali198@gmail.com

## 🔍 Quality Standards

### Etymology
- Cite sources when possible
- Mention cognates in related languages (Turkish, Uzbek, Tatar, etc.)
- For loanwords, specify original language and form
- Include historical context when available

### Examples
- Use natural, common usage
- Provide context that clarifies meaning
- Include all three languages (kk, ru, en)
- Aim for 1-3 examples per definition

### Accuracy
- Verify IPA transcription
- Double-check all transcriptions
- Ensure translations are accurate
- Cross-reference etymologies

## 📚 Resources

- [IPA Transcription Guide](https://en.wikipedia.org/wiki/Help:IPA/Kazakh)
- [AnmiTaliDev's Latin Proposal](https://github.com/AnmiTaliDev/new-kazakh-latin-proposal)
- [Qazaq Tili](https://kk.wikipedia.org) - Kazakh Wikipedia
- [Sozdik.kz](https://sozdik.kz) - Online dictionary

## 🤝 Community Guidelines

- Be respectful and constructive
- Focus on accuracy and completeness
- Cite sources for etymologies
- Welcome corrections and improvements
- Maintain CC0 spirit - knowledge should be free

## ❓ Questions?

- Open an [issue](https://github.com/AnmiTaliDev/kazakh-dictionary/issues)
- Email: anmitali198@gmail.com
- Check existing entries for examples

## 📄 License

By contributing, you agree to release your contributions under CC0 (Public Domain). This means:
- No copyright restrictions
- Free for anyone to use
- No attribution required (but appreciated!)

---

## Example: Adding a New Word

Let's add the word "сөз" (word, speech):

1. **Create file**: `dictionary/с/сөз.yaml`

2. **Fill content**:
```yaml
- id: 7
  word: "сөз"
  parent_id: null
  type: "noun"
  transcription: "søz"
  latin_2017: "söz"
  latin_2021: "söz"
  latin_my: "söz"
  root_word: "сөз"
  etymology: "Түркі тілдерінің ортақ қоры"
  history: "Көне түркі тілінен 'söz' түрінде келген. Барлық түркі тілдерінде бар."
  definitions:
    - meaning: "Ойды жеткізетін тіл бірлігі"
      translation_ru: "Слово"
      translation_en: "Word"
      examples:
        - kk: "Бір сөзбен айтсам..."
          ru: "Одним словом..."
          en: "In a word..."
```

3. **Submit via Pull Request or Issue**

4. **Wait for review**

---

Рақмет сіздерге! Спасибо вам! Thank you for contributing! 🇰🇿
