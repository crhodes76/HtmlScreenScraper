from Modules import html_functions as hf

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    data = hf.scrape(url)
    print(f"Scraped text from {data.url}:")
    print(data.text)
