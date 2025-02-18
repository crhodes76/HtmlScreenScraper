from Modules import html_functions as hf
from model import ScrapedData
from Modules import json_functions as jf

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    data = hf.scrape(url)
    print(f"Scraped text from {data.url}:")
    print(f"The data scraped {data.text}")

    # Save the scraped data to JSON
    jf.save_text_to_json(data)

    # Load the data from JSON
    loaded_data = jf.load_text_from_json()
    print(f"Loaded data from {loaded_data.url}:")
    print(f"The data loaded {loaded_data.text}")

    # Search for a keyword and highlight it in the output
    keyword = input("Enter the keyword to search: ")
    jf.search_and_highlight_keyword_in_json(keyword=keyword)



