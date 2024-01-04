"""
This Python script extracts metadata from a Youtube web page, including the Video title, description,
and duration, and prints the information in a human-readable format.

The 'convdur' function takes a duration string in the format 'PTxMxS' (e.g., 'PT3M25S') and
returns a tuple containing minutes, seconds, and total duration in seconds.

The main part of the script prompts the user for a URL, fetches the HTML content from the web page,
parses it using BeautifulSoup, and then extracts and prints the Video title, description, and
duration information.

"""

def convdur(dur_str):
    min = None
    sec = None

    # Check if 'PT' is present in the duration string
    if 'PT' in dur_str:
        # Remove 'PT' from the duration string
        dur_str = dur_str.replace('PT', '')

        # Check if 'M' is present in the duration string
        if 'M' in dur_str:
            min = int(dur_str.split('M')[0])
            dur_str = dur_str.split('M')[1]

        # Check if 'S' is present in the duration string
        if 'S' in dur_str:
            sec = int(dur_str.split('S')[0])

    # Convert to total duration in seconds
    total_duration = min * 60 + sec
    return min, sec, total_duration

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# Prompt the user for a URL
url = input('Enter url: ')

# Fetch HTML content from the web page
html = urllib.request.urlopen(url).read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find Open Graph title, description, and duration meta tags
title_tag = soup.find('meta', property='og:title')
description_tag = soup.find('meta', property='og:description')
duration_tag = soup.find('meta', itemprop='duration')

# Print extracted metadata
print(title_tag.get('content'))
print(description_tag.get('content'))

# Extract and print duration information using the 'convdur' function
dur_str = duration_tag.get('content')
tup = convdur(dur_str)
print(tup[2], 'Seconds or', tup[0], 'Mins and', tup[1], 'Seconds')
