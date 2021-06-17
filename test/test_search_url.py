import pytest

from src.search_url import SearchUrl
from src.url_param import UrlParam
from src.stay_date import StayDate
from src.search_prefecture import SearchPrefecture


@pytest.fixture()
def url():
    staydate = StayDate()
    pref = SearchPrefecture("大阪")
    up = UrlParam(staydate, pref)
    url = SearchUrl(up)
    yield url


def test_url_is_list(url):
    search_url = url.search_url
    assert type(search_url) is list


def test_base_url(url):
    base_url = url.base_url
    assert base_url == "https://www.jalan.net/"


def test_url_contains_osaka111(url):
    for each_url in url.search_url:
        assert "osaka111" in each_url


def test_url_contains_regioncode(url):
    region_code = "region_code_1"
    assert region_code in url.search_url[0]


# def test_constructer(url):
#     staydate = StayDate()
#     up = UrlParam(staydate)
#     url_param = up.url_param
#     # 期待値
#     expected_url = url.base_url + query_param[0]
#     assert url.search_url == expected_url
