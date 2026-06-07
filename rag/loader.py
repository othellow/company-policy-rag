"""
Document loading utilities.

Supports:
- Markdown
- TXT
- HTML
- PDF (future)
"""

from pathlib import Path
import re


def load_markdown_file(file_path: str) -> str:
    """
    Load markdown file content.
    """

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def clean_text(text: str) -> str:
    """
    Basic text cleaning.
    """

    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()


def load_all_markdown(directory: str):
    """
    Load all markdown files from a directory.
    """

    documents = []

    for path in Path(directory).glob("*.md"):

        documents.append(
            {
                "filename": path.name,
                "content": clean_text(
                    load_markdown_file(path)
                ),
            }
        )

    return documents