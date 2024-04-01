#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import sys

def fetch_verse(reference, version):
    """Fetches a Bible verse from BibleGateway.com given a reference and version."""
    url = f"https://www.biblegateway.com/passage/?search={reference}&version={version}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching the verse.")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    verse_content = soup.find(class_="passage-text")
    if verse_content:
        return verse_content.text.strip()
    else:
        print("Verse not found.")
        return None

def main():
    if len(sys.argv) > 2:
        # Command-line mode
        reference = ' '.join(sys.argv[1:])
        version = ' '.join(sys.argv[2:])
    else:
        # Interactive mode
        reference = input("Enter the Bible verse reference (e.g., John 3:16)")
        version = input("Enter the version (default: NRSVCE)")
        if not version:
            version = "NRSVCE"

    verse = fetch_verse(reference, version)
    if verse:
        print(f"Verse: {verse}")

if __name__ == "__main__":
    main()
