import pytest

from src.url import Url


@pytest.fixture()
def url():
    query = "hello"
    url = Url(query)
    yield url


def test_url_is_str(url):
    search_url = url.search_url
    assert type(search_url) is str


def test_base_url(url):
    base_url = url.base_url
    assert base_url == "https://www.jalan.net/"


def test_constructer(url):
    arg = "hello"
    # 期待値
    expected_url = url.base_url + arg
    assert url.search_url == expected_url
