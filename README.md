# Kazakh Dictionary / Қазақ Сөздігі / Казахский Словарь

[![License: CC0](https://img.shields.io/badge/License-CC0-blue.svg)](LICENSE)
[![Language: Kazakh](https://img.shields.io/badge/Language-Kazakh-green.svg)]()
[![Status: Active](https://img.shields.io/badge/Status-Active-success.svg)]()

Open-source Kazakh-Russian-English dictionary with etymology, morphological analysis, and multiple Latin transcription systems.

## 🎯 Project Goals

- **Preserve** Kazakh language heritage through detailed etymological documentation
- **Document** morphological roots and word relationships
- **Support** multiple Latin transcription systems including [AnmiTaliDev's proposal](https://github.com/AnmiTaliDev/new-kazakh-latin-proposal)
- **Provide** free, open-access linguistic resources for researchers, learners, and developers
- **Build** a community-driven knowledge base under CC0 (Public Domain)

## 📚 Features

- ✅ **Trilingual**: Kazakh, Russian, and English
- ✅ **Etymology**: Detailed word origins and historical context
- ✅ **IPA Transcription**: Accurate phonetic notation
- ✅ **Multiple Latin Scripts**: 2017, 2021, and AnmiTaliDev's proposal
- ✅ **Morphological Analysis**: Root words and derivatives
- ✅ **Usage Examples**: Real-world sentence examples
- ✅ **Synonyms & Antonyms**: Semantic relationships
- ✅ **CC0 License**: Completely free and unrestricted

## 📖 Example Entry

```yaml
- id: 1
  word: "кітап"
  parent_id: null
  type: "noun"
  transcription: "kɪˈtɑp"
  latin_2017: "kitap"
  latin_2021: "kitap"
  latin_my: "kıtap"
  root_word: "кітап"
  etymology: "Араб тілінен"
  history: "Арабтың 'kitab' (کتاب) сөзінен шыққан..."
  definitions:
    - meaning: "Басылып шыққан әдеби, ғылыми немесе оқу туындысы"
      translation_ru: "Книга"
      translation_en: "Book"
      examples:
        - kk: "Мен кітапханадан жаңа кітап алдым."
          ru: "Я взял новую книгу из библиотеки."
          en: "I took a new book from the library."
  synonyms:
    - word_id: null
      word: "шығарма"
      note: "Для художественной литературы"
```

## 🗂️ Project Structure

```
kazakh-dictionary/
├── dictionary/          # Dictionary entries organized by first letter
│   ├── а/              # Words starting with 'а'
│   ├── ә/              # Words starting with 'ә'
│   ├── б/              # Words starting with 'б'
│   └── .../            # ... all Kazakh Cyrillic letters
├── references/
│   └── latin-proposal/ # AnmiTaliDev's Latin transcription system
├── CLAUDE.md           # Instructions for Claude AI
├── GEMINI.md           # Instructions for Gemini AI
├── CONTRIBUTING.md     # Contribution guidelines
└── README.md           # This file
```

## 🚀 Getting Started

### Browse the Dictionary

Entries are organized by the first Cyrillic letter of each word:
- Navigate to `dictionary/{letter}/` to find words
- Each word has its own YAML file: `{word}.yaml`

### Using the Data

```python
import yaml

# Load a word
with open('dictionary/к/кітап.yaml', 'r', encoding='utf-8') as f:
    word = yaml.safe_load(f)
    print(f"{word[0]['word']} = {word[0]['translation_en']}")
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for:
- How to add new words
- YAML format specifications
- Quality guidelines
- Submission process

### Quick Start for Contributors

1. Fork this repository
2. Add/edit YAML files in appropriate `dictionary/{letter}/` directory
3. Follow the format in [CONTRIBUTING.md](CONTRIBUTING.md)
4. Submit a Pull Request

### AI Assistance

Using AI to help? Check our AI-specific guidelines:
- [CLAUDE.md](CLAUDE.md) - For Claude AI
- [GEMINI.md](GEMINI.md) - For Google Gemini

## 📋 Current Statistics

- **Words**: 113 entries (growing!)
- **Languages**: 3 (Kazakh, Russian, English)
- **Latin Systems**: 3 (2017, 2021, AnmiTaliDev)
- **Contributors**: Open to all!

## 🔤 Latin Transcription Systems

### AnmiTaliDev's Proposal (latin_my)

This project includes support for [AnmiTaliDev's Latin transcription proposal](https://github.com/AnmiTaliDev/new-kazakh-latin-proposal), featuring:
- Unique representation for every Cyrillic letter
- Diacritics for accurate phonetic distinction
- Support for all Kazakh sounds

Key features:
- `ı` (dotless i) for **і**
- `y` for **ы**
- `ä` for **ә**
- `ğ` for **ғ**
- `ŋ` for **ң**
- And more (see `references/latin-proposal/`)

## 📄 License

This project is released under [CC0 1.0 Universal (Public Domain)](LICENSE).

**You are free to:**
- ✅ Use for any purpose
- ✅ Modify and redistribute
- ✅ Use commercially
- ✅ No attribution required (but appreciated!)

## 🌟 Acknowledgments

- **AnmiTaliDev** - Project creator and maintainer
- [New Kazakh Latin Proposal](https://github.com/AnmiTaliDev/new-kazakh-latin-proposal) - Latin transcription system
- All contributors who help expand this dictionary

## 📞 Contact

- **Maintainer**: AnmiTaliDev
- **Email**: anmitali198@gmail.com
- **Issues**: [GitHub Issues](https://github.com/AnmiTaliDev/kazakh-dictionary/issues)

## 🗺️ Roadmap

- [ ] Expand dictionary to 1,000+ words
- [ ] Add audio pronunciations
- [ ] Create web interface
- [ ] Develop API for programmatic access
- [ ] Mobile app integration
- [ ] Advanced search and filtering

---

**Қазақ тілі мәңгі жасай берсін!** 🇰🇿

*Long live the Kazakh language!*
