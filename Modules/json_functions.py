from model import ScrapedData

def save_text_to_json(data: ScrapedData, filename='scraped_data.json'):
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
