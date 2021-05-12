import pytest

from src.url import Url


def test_generate_url():
    urlclass = Url()
    url = urlclass.url
    assert type(url) is str
