import pytest

from src.search_url import SearchUrl
from src.query_param import QueryParam
from src.stay_date import StayDate


@pytest.fixture()
def url():
    staydate = StayDate()
    query = QueryParam(staydate)
    url = SearchUrl(query)
    yield url


def test_url_is_str(url):
    search_url = url.search_url
    assert type(search_url) is str


def test_base_url(url):
    base_url = url.base_url
    assert base_url == "https://www.jalan.net/"


def test_constructer(url):
    staydate = StayDate()
    query = QueryParam(staydate)
    query_param = query.query_param
    # 期待値
    expected_url = url.base_url + query_param
    assert url.search_url == expected_url
