from src.stay_date import StayDate
from src.search_prefecture import SearchPrefecture
from src.stay_price import Price
from src.url_param import UrlParam
from src.search_url import SearchUrl


class ScrapingProgram:
    def __init__(
        self,
        stayYear="",
        stayMonth="",
        stayDay="",
        prefecture="",
        minPrice=0,
        maxPrice="",
    ):
        super().__init__()
        self.staydate = StayDate(stayYear, stayMonth, stayDay)
        self.prefecture = SearchPrefecture(prefecture)
        self.price = Price(minPrice, maxPrice)

        self.url_param = UrlParam(
            staydate=self.staydate, prefecture=self.prefecture, price=self.price
        )
        self.url = SearchUrl(query=self.url_param)
