import pytest

from src.search_url import SearchUrl
from src.url_param import UrlParam
from src.stay_date import StayDate
from src.search_prefecture import SearchPrefecture


class TestSearchUrl:
    def setup_method(self, method):
        self.staydate = StayDate()
        self.pref = SearchPrefecture("大阪")
        self.up = UrlParam(self.staydate, self.pref)
        self.url = SearchUrl(self.up)

    def test_url_is_list(self):
        search_url = self.url.search_url
        assert type(search_url) is list

    def test_base_url(self):
        base_url = self.url.base_url
        assert base_url == "https://www.jalan.net/"


# def test_constructer(url):
#     staydate = StayDate()
#     up = UrlParam(staydate)
#     url_param = up.url_param
#     # 期待値
#     expected_url = url.base_url + query_param[0]
#     assert url.search_url == expected_url
