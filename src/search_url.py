class SearchUrl:
    def __init__(self, query):
        self.base_url = "https://www.jalan.net/"
        self.search_url = []
        print(query.url_param)
        for up in query.url_param:
            url = self.base_url + up
            self.search_url.append(url)
