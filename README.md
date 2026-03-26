# Kazakh Dictionary (Қазақ Сөздігі)

[![License: CC0](https://img.shields.io/badge/License-CC0-blue.svg)](LICENSE)
[![Language: Kazakh](https://img.shields.io/badge/Language-Kazakh-green.svg)]()

This repository contains a comprehensive, open-source Kazakh-Russian-English linguistic database. The project focuses on etymological documentation, morphological analysis, and the implementation of various Latin transcription standards.

## Project Objectives

The primary goal of this initiative is to create a structured, machine-readable resource for the Kazakh language that:
1. Document word origins (etymology) and historical development.
2. Maps morphological relationships between root words and their derivatives.
3. Provides accurate phonetic transcriptions (IPA) and multiple Latin script implementations.
4. Serves as a public domain (CC0) foundation for linguistic research, educational tools, and software development.

## Technical Specifications

Data is stored in standardized YAML files, ensuring ease of parsing and human readability. Each entry includes:
- **Trilingual Definitions**: Full support for Kazakh, Russian, and English.
- **Phonetics**: International Phonetic Alphabet (IPA) transcriptions.
- **Transcription Systems**: Support for the 2017 and 2021 official standards, as well as the AnmiTaliDev Latin proposal.
- **Semantic Relations**: Comprehensive mapping of synonyms and antonyms.
- **Contextual Data**: Real-world usage examples for every definition.

## Data Structure

Entries are organized hierarchically within the `dictionary/` directory, sorted by the initial Cyrillic character of the headword.

### YAML Schema Example

```yaml
- id: 1
  word: "кітап"
  parent_id: null
  type: "noun"
  transcription: "kɪˈtɑp"
  writing_systems:
    latin_2017: "kitap"
    latin_2021: "kitap"
    latin_my: "kıtap"
  root_word: "кітап"
  etymology: "Arabic origin"
  history: "Derived from Arabic 'kitab' (کتاب)..."
  definitions:
    - meaning: "Басылып шыққан әдеби, ғылыми немесе оқу туындысы"
      translation_ru: "Книга"
      translation_en: "Book"
      examples:
        - kk: "Бұл кітап өте қызықты."
          ru: "Эта книга очень интересная."
          en: "This book is very interesting."
```

## Contribution Guidelines

Contributions are governed by strict quality standards to maintain the integrity of the database.

### Submission Process
1. Review the technical specifications in [CONTRIBUTING.md](CONTRIBUTING.md).
2. For AI-assisted contributions, consult the mandatory instructions in [AGENTS.md](AGENTS.md).
3. Ensure all fields (including English translations and IPA) are completed.
4. Submit changes via a Pull Request.

**Note**: The `LIST.md` file is managed automatically via GitHub Actions. Manual modifications to this file will be overwritten.

## License and Terms of Use

This project is dedicated to the public domain under the [CC0 1.0 Universal License](LICENSE). 
- No copyright protection is claimed.
- You may copy, modify, distribute, and perform the work, even for commercial purposes, without asking permission.
- Attribution is not required but is appreciated for the continued growth of the project.

## Contact and Support

- **Maintainer**: AnmiTaliDev
- **Communication**: anmitali198@gmail.com
- **Technical Issues**: [GitHub Issue Tracker](https://github.com/AnmiTaliDev/kazakh-dictionary/issues)

---

**Қазақ тілі мәңгі жасай берсін!**
