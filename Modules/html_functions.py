import requests
from bs4 import BeautifulSoup
from model import ScrapedData
from Modules import html_functions

def fetch_html(url: str):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_html(html: str):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text(separator=' ', strip=True)
    return text

def scrape(url: str):
    html = fetch_html(url)
    text = parse_html(html)
    data = ScrapedData(url=url, text=text)
    return data