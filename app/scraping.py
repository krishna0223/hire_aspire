# app/scraping.py

import requests
from bs4 import BeautifulSoup
from .models import JobPosting

def scrape_jobs():
    """Scrape jobs from an example website."""
    url = 'https://example.com/jobs'  # Replace with the actual URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example scraping logic - change based on actual site structure
    job_listings = soup.find_all('div', class_='job-listing')

    for job in job_listings:
        title = job.find('h2').text
        company = job.find('span', class_='company').text
        location = job.find('span', class_='location').text
        description = job.find('p', class_='description').text

        # Save to database
        JobPosting.objects.create(
            title=title,
            company_name=company,
            location=location,
            description=description
        )
