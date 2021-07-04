import pytest

from src.url_param import UrlParam
from src.stay_date import StayDate
from src.search_prefecture import SearchPrefecture
from src.stay_price import Price

# def test_path_param_is_str():
#     staydate = StayDate()
#     up = UrlParam(staydate)
#     assert type(up.path_param) is str


class TestUrlParam:
    def setup_method(self, method):
        self.staydate = StayDate()
        self.pref = SearchPrefecture("大阪")
        self.price = Price(minPrice=0, maxPrice=10000)
        self.up = UrlParam(self.staydate, self.pref, self.price)

    def test_url_param_is_list(self):
        assert type(self.up.url_param) is list

    def test_大阪のパラメータ内の地域コード(self):
        assert "270000/LRG_271400/" in self.up.url_param[0]
        assert "270000/LRG_271700/" in self.up.url_param[1]
        assert "270000/LRG_272000/" in self.up.url_param[2]
        assert "270000/LRG_272300/" in self.up.url_param[3]
        assert "270000/LRG_272600/" in self.up.url_param[4]
        assert "270000/LRG_272900/" in self.up.url_param[5]
        assert "270000/LRG_273200/" in self.up.url_param[6]

    def test_最大料金10000(self):
        assert "maxPrice=10000" in self.up.url_param[0]


# def test_url_param_contains_path_query():
#     assert


# def test_query_parameter_is_list():
#     staydate = StayDate()
#     up = UrlParam(staydate)
#     query_param = up.query_param
#     assert type(query_param) is list


# def test_empty_query_param():
#     staydate = StayDate()
#     up = UrlParam(staydate)
#     query_param = up.query_param
#     assert (
#         query_param[0]
#         == "?screenId=UWW1402&distCd=01&photo=1&activeSort=0&rootCd=04&stayYear=&stayMonth=&stayDay=&stayCount=1&roomCount=1&adultNum=2&minPrice=0&maxPrice=&roomCrack=200000&kenCd=&lrgCd=&mvTabFlg=2"
#     )


# def test_query_param_20220520():
#     staydate = StayDate(stayYear=2022, stayMonth=5, stayDay=20)
#     up = UrlParam(staydate=staydate)
#     query_param = up.query_param
#     assert "stayYear=2022&stayMonth=5&stayDay=20" in query_param[0]
