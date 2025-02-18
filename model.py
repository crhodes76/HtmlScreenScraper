import json

class ScrapedData:
    def __init__(self, url: str, text: str):
        self.url = url
        self.text = text

    def to_dict(self):
        return {
            'url': self.url,
            'text': self.text
        }

    @classmethod
    def from_dict(cls, data_dict):
        return cls(url=data_dict['url'], text=data_dict['text'])

    def to_json(self, indent=None):
        return json.dumps(self.to_dict(), indent=indent)

    @classmethod
    def from_json(cls, json_str):
        data_dict = json.loads(json_str)
        return cls.from_dict(data_dict)
