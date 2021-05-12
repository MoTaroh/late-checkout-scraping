class Url:
    def __init__(self):
        self.base_url = "https://www.jalan.net/"
        self.search_url = "https://hogehoge"

    def generate_url(self, query):
        self.search_url = self.base_url + query
