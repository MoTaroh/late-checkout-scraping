from src.stay_price import Price
from src.stay_date import StayDate
from src.search_prefecture import SearchPrefecture
from src.url_param import UrlParam
from src.search_url import SearchUrl
from src.scraping_program import ScrapingProgram


class TestScrapingProgram:
    def setup_method(self, method):
        self.scraping_program = ScrapingProgram(
            prefecture="大阪", minPrice=0, maxPrice=10000
        )

    def test_じゃらんURLを含むリスト(self):
        assert "https://www.jalan.net/" in self.scraping_program.url.search_url[0]
