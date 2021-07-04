import pytest

from src.search_prefecture import SearchPrefecture


class TestSearchPrefecture:
    def setup_method(self, method):
        self.pref = SearchPrefecture("大阪")

    def test_大阪の都道府県コード(self):
        assert self.pref.prefecture_code == "270000"

    def test_大阪の地域コード(self):
        osaka_region_code = [
            "271400",
            "271700",
            "272000",
            "272300",
            "272600",
            "272900",
            "273200",
        ]

        for index, region in enumerate(self.pref.region):
            assert region["region_code"] == osaka_region_code[index]
