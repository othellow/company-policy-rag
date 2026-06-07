"""
Markdown-aware chunking with metadata support.

Each chunk contains:
- document
- section
- chunk_id
- content
"""

import re


def split_markdown_sections(text: str):
    """
    Split markdown content by headings.
    """

    pattern = r"(?=^#{1,6}\s)"

    sections = re.split(
        pattern,
        text,
        flags=re.MULTILINE,
    )

    return [
        section.strip()
        for section in sections
        if section.strip()
    ]


def extract_heading(section: str) -> str:
    """
    Extract the heading from a markdown section.

    Example:
        # Annual Leave

    Returns:
        Annual Leave
    """

    lines = section.splitlines()

    for line in lines:

        if line.startswith("#"):

            return (
                line.lstrip("#")
                .strip()
            )

    return "Unknown"


def generate_chunk_id(
    filename: str,
    heading: str,
) -> str:
    """
    Generate a deterministic chunk ID.

    Example:
        03-human-resources-policy.md
        Annual Leave

    Becomes:
        03-human-resources-policy_annual_leave
    """

    filename = (
        filename
        .replace(".md", "")
        .lower()
    )

    heading = (
        heading
        .lower()
        .replace(" ", "_")
        .replace("/", "_")
    )

    return f"{filename}_{heading}"


def chunk_documents(documents):
    """
    Chunk documents using markdown headings.

    Returns:
        [
            {
                "document": "...",
                "section": "...",
                "chunk_id": "...",
                "content": "..."
            }
        ]
    """

    chunks = []

    for doc in documents:

        sections = split_markdown_sections(
            doc["content"]
        )

        for section in sections:

            heading = extract_heading(
                section
            )

            chunks.append(
                {
                    "document": doc["filename"],
                    "section": heading,
                    "chunk_id": generate_chunk_id(
                        doc["filename"],
                        heading,
                    ),
                    "content": section,
                }
            )

    return chunks
