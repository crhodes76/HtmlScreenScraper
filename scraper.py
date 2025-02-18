import requests
from bs4 import BeautifulSoup
from model import ScrapedData

def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text(separator=' ', strip=True)
    return text

def scrape(url):
    html = fetch_html(url)
    text = parse_html(html)
    data = ScrapedData(url=url, text=text)
    return data

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    data = scrape(url)
    print(f"Scraped text from {data.url}:")
    print(data.text)
