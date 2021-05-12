import pytest

from src.url import Url


def test_url_is_str():
    url = Url()
    search_url = url.search_url
    assert type(search_url) is str


def test_base_url():
    url = Url()
    base_url = url.base_url
    assert base_url == "https://www.jalan.net/"


def test_contact_url():
    arg = "hello"
    url = Url()
    # 引数を入れたら結合してくれる
    url.generate_url(arg)
    search_url = url.search_url
    # 期待値
    expected_url = url.base_url + arg
    assert search_url == expected_url
