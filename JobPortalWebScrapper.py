#Following code scrapes the website cv-library.co.uk for job posts to extract job_title, company name, salary, location and description
# Import necessary libraries
import csv
import requests
from bs4 import BeautifulSoup

# Function to generate the URL based on position and location
def get_url(position, location):
    template = 'https://www.cv-library.co.uk/{}-jobs-in-{}'
    url = template.format(position, location)
    return url

# Function to extract a single record from a job card
def get_record(card):
    """Extract single record"""
    # Extract job title, company name, salary, location, and description from the card
    job_title = card.find('h2', class_='job__title').a.get_text(strip=True) if card.find('h2', class_='job__title') else None
    company_name = card.find('a', class_='job__company-link').get_text(strip=True) if card.find('a', class_='job__company-link') else None
    salary = card.find('dd', class_='job__details-value salary').get_text(strip=True).replace('£', '') if card.find('dd', class_='job__details-value salary') else None
    location = card.find('dd', class_='job__details-value location').get_text(strip=True) if card.find('dd', class_='job__details-value location') else None
    description = card.find('p', class_='job__description').get_text(strip=True) if card.find('p', class_='job__description') else None

    # Skip the record if job title is None
    if job_title is None:
        return None

    # Return a tuple with the extracted information
    record = (job_title, company_name, salary, location, description)
    return record

# Main function to scrape job data
def main(position, location):
    records = []  # Initialize a list to store records
    url = get_url(position, location)  # Get the initial URL

    while True:
        # Make a request to the URL and create a BeautifulSoup object
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all job cards on the page
        cards = soup.find_all('li', class_='results__item')

        for card in cards:
            record = get_record(card)  # Extract record from each card

            # Append the record only if it's not None
            if record is not None:
                records.append(record)

        try:
            # Get the URL of the next page for pagination
            url = "https://www.cv-library.co.uk" + soup.find('a', {'aria-label': 'Next page'}).get('href')
            print(url)
        except AttributeError:
            break  # Break the loop if there is no next page link

    # Save job data to a CSV file
    with open('results.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Write header and records to the CSV file
        writer.writerow(['job_title', 'company_name', 'salary', 'location', 'description'])
        writer.writerows(records)

# Run main program with specified position and location
main('DataEngineer', 'London')
