import pytest
from src.stay_price import Price


class TestPrice:
    def test_最大料金が最小料金よりも小さければエラー(self):
        with pytest.raises(ValueError):
            self.price = Price(minPrice=10000, maxPrice=9000)

    def test_宿泊料金が0円未満であればエラー(self):
        with pytest.raises(ValueError):
            self.price = Price(minPrice=-1)

    def test_宿泊料金が小数であればエラー(self):
        with pytest.raises(ValueError):
            self.price = Price(minPrice=0.1)
