#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import sys

def fetch_verse(reference):
    """Fetches a Bible verse from BibleGateway.com given a reference."""
    url = f"https://www.biblegateway.com/passage/?search={reference}&version=NRSVCE"
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
    if len(sys.argv) > 1:
        # Command-line mode
        reference = ' '.join(sys.argv[1:])
    else:
        # Interactive mode
        reference = input("Enter the Bible verse reference (e.g., John 3:16): ")

    verse = fetch_verse(reference)
    if verse:
        print(f"Verse: {verse}")

if __name__ == "__main__":
    main()
