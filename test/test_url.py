import pytest

from src.url import Url


def test_url_is_str():
    url = Url()
    search_url = url.search_url
    assert type(search_url) is str
