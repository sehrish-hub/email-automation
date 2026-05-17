import requests
from bs4 import BeautifulSoup

def extract_job_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Simple generic extraction (real sites may vary)
    title = soup.title.text if soup.title else "Job Position"
    company = "Company"

    return title, company