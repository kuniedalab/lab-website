#!/usr/bin/env python3
"""
BibTeX to HugoBlox publication converter
Usage: python bib2hugoblox.py input.bib output_dir
"""

import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode
import os
import sys
import re
from pathlib import Path


def clean_text(text):
    """Remove LaTeX markup and clean text."""
    if not text:
        return ""
    text = text.replace("\\&", "&")
    text = text.replace("\\%", "%")
    text = text.replace("\\$", "$")
    # Remove curly braces used for case protection
    text = re.sub(r'\{([^{}]*)\}', r'\1', text)
    text = text.strip()
    return text


def parse_authors(author_str):
    """Parse BibTeX author string into list of 'Firstname Lastname' strings."""
    if not author_str:
        return []
    authors = []
    for author in author_str.split(" and "):
        author = clean_text(author.strip())
        if "," in author:
            parts = author.split(",", 1)
            lastname = parts[0].strip()
            firstname = parts[1].strip()
            authors.append(f"{firstname} {lastname}")
        else:
            authors.append(author)
    return authors


def get_publication_type(entry_type):
    """Map BibTeX entry type to CSL publication type."""
    mapping = {
        "article": "article-journal",
        "inproceedings": "paper-conference",
        "proceedings": "paper-conference",
        "book": "book",
        "incollection": "chapter",
        "phdthesis": "thesis",
        "mastersthesis": "thesis",
        "techreport": "report",
        "misc": "article",
        "preprint": "article",
    }
    return mapping.get(entry_type.lower(), "article-journal")


def parse_pages(pages_str):
    """Normalize page range."""
    if not pages_str:
        return ""
    return re.sub(r'-+', '-', pages_str.strip())


def make_slug(entry):
    """Create a folder slug from the BibTeX key."""
    key = entry.get("ID", "unknown")
    return re.sub(r'[^a-z0-9-]', '-', key.lower())


def entry_to_hugo(entry):
    """Convert a BibTeX entry to HugoBlox frontmatter."""
    title = clean_text(entry.get("title", ""))
    authors = parse_authors(entry.get("author", ""))
    year = entry.get("year", "")
    month = entry.get("month", "")
    journal = clean_text(entry.get("journal", entry.get("booktitle", "")))
    volume = entry.get("volume", "")
    number = entry.get("number", "")
    pages = parse_pages(entry.get("pages", ""))
    doi = entry.get("doi", "")
    abstract = clean_text(entry.get("abstract", ""))
    pmid = entry.get("pmid", "")
    pub_type = get_publication_type(entry.get("ENTRYTYPE", "article"))

    # Build date
    month_map = {
        "jan": "01", "feb": "02", "mar": "03", "apr": "04",
        "may": "05", "jun": "06", "jul": "07", "aug": "08",
        "sep": "09", "oct": "10", "nov": "11", "dec": "12",
    }
    month_num = month_map.get(month.lower()[:3], "01") if month else "01"
    date = f"{year}-{month_num}-01" if year else "2000-01-01"

    # Build publication string
    pub_parts = []
    if journal:
        pub_parts.append(f"*{journal}*")
    if volume:
        vol_str = f"**{volume}**"
        if number:
            vol_str += f"({number})"
        pub_parts.append(vol_str)
    if pages:
        pub_parts.append(pages)
    publication_str = ", ".join(pub_parts)

    # Build YAML
    lines = []
    lines.append("---")
    lines.append(f"title: \"{title}\"")
    lines.append("authors:")
    for author in authors:
        lines.append(f"  - {author}")
    lines.append(f"date: {date}")
    lines.append("publication_types:")
    lines.append(f"  - \"{pub_type}\"")
    if publication_str:
        lines.append(f"publication: \"{publication_str}\"")
    if doi:
        lines.append(f"doi: \"{doi}\"")
    if abstract:
        abstract_escaped = abstract.replace('"', '\\"')
        lines.append(f"abstract: \"{abstract_escaped}\"")
    if pmid:
        lines.append(f"# pmid: {pmid}")
    lines.append("draft: false")
    lines.append("featured: false")
    lines.append("---")

    return "\n".join(lines)


def convert(bib_file, output_dir):
    """Main conversion function."""
    parser = BibTexParser()
    parser.customization = convert_to_unicode
    parser.ignore_nonstandard_types = False
    parser.homogenise_fields = False

    with open(bib_file, encoding="utf-8") as f:
        content = f.read()
    # Replace bare month abbreviations with quoted strings
    content = re.sub(
        r'(\bmonth\s*=\s*)(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\b',
        r'\1{\2}',
        content,
        flags=re.IGNORECASE
    )
    import io
    bib_database = bibtexparser.loads(content, parser=parser)

    print(f"Found {len(bib_database.entries)} entries")

    for entry in bib_database.entries:
        slug = make_slug(entry)
        folder = Path(output_dir) / slug
        folder.mkdir(parents=True, exist_ok=True)

        content = entry_to_hugo(entry)
        out_file = folder / "index.md"
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(content)
            f.write("\n")

        print(f"  Created: {slug}/index.md")

    print(f"\nDone! {len(bib_database.entries)} files created in '{output_dir}'")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python bib2hugoblox.py input.bib output_dir")
        sys.exit(1)

    bib_file = sys.argv[1]
    output_dir = sys.argv[2]
    convert(bib_file, output_dir)