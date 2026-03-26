import os
from pathlib import Path

import yaml


def get_all_words():
    dictionary_path = Path("dictionary")
    words = []

    for letter_dir in dictionary_path.iterdir():
        if letter_dir.is_dir():
            for yaml_file in letter_dir.glob("*.yaml"):
                try:
                    with open(yaml_file, "r", encoding="utf-8") as f:
                        data = yaml.safe_load(f)
                        if isinstance(data, list) and len(data) > 0:
                            words.append(data[0]["word"])
                except Exception as e:
                    print(f"Error reading {yaml_file}: {e}")

    # Simple sort. For true Kazakh sorting, a custom key would be needed.
    return sorted(words)


def update_list_md(words):
    content = "# Word List\n\n"
    content += f"**Total words**: {len(words)}\n\n"

    for word in words:
        content += f"- {word}\n"

    with open("LIST.md", "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    all_words = get_all_words()
    update_list_md(all_words)
    print(f"Updated LIST.md with {len(all_words)} words.")
