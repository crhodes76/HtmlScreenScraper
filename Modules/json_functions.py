from model import ScrapedData
from urllib.parse import urlparse

def save_text_to_json(data: ScrapedData):
    # Extract the domain name from the URL
    parsed_url = urlparse(data.url)
    domain = parsed_url.netloc.split('.')[1]  # Get the main domain name
    filename = f'{domain}_data.json'
    
    print(f"Saving data to {filename}...")
    json_data = data.to_json(indent=4)
    with open(filename, 'w') as f:
        f.write(json_data)
    print(f"Data saved to {filename}")

def load_text_from_json(filename='scraped_data.json'):
    print(f"Loading data from {filename}...")
    with open(filename, 'r') as f:
        loaded_json_data = f.read()
    return ScrapedData.from_json(loaded_json_data)

def highlight_keyword(text: str, keyword: str):
    highlighted_text = text.replace(keyword, f"\033[1;31m{keyword}\033[0m")
    return highlighted_text

def search_and_highlight_keyword_in_json(filename='scraped_data.json', keyword=''):
    data = load_text_from_json(filename)
    print(f"Searching for keyword '{keyword}' in the text...")
    highlighted_text = highlight_keyword(data.text, keyword)
    print(f"URL: {data.url}")
    print(f"Text with highlighted keyword '{keyword}':")
    print(highlighted_text)
