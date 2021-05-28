class SearchUrl:
    def __init__(self, query):
        self.base_url = "https://www.jalan.net/"
        self.search_url = self.base_url + query.query_param
