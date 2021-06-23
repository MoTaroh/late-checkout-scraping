import pytest

from src.search_prefecture import SearchPrefecture


def test_大阪の都道府県コード():
    pref = SearchPrefecture("大阪")
    assert pref.prefecture_code == "270000"


def test_大阪の地域コード():
    pref = SearchPrefecture("大阪")
    osaka_region_code = [
        "271400",
        "271700",
        "272000",
        "272300",
        "272600",
        "272900",
        "273200",
    ]

    for index, region in enumerate(pref.region):
        assert region["region_code"] == osaka_region_code[index]
