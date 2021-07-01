class Price:
    def __init__(self, minPrice=0, maxPrice=""):
        self.minPrice = minPrice
        self.maxPrice = maxPrice

        if self.maxPrice == "":
            # 最小値の正の整数バリデーション
            self.isPositive(self.minPrice)
            self.isInteger(self.minPrice)
        else:
            # それぞれの正の整数バリデーション
            self.isPositive(self.minPrice)
            self.isPositive(self.maxPrice)
            self.isInteger(self.minPrice)
            self.isInteger(self.maxPrice)
            # 最大料金 >= 最小料金のバリデーション
            self.maxPrice_is_greater_than_minPrice()

    def isPositive(self, price):
        if price < 0:
            raise ValueError("StayPrice must be positive value.")

    def maxPrice_is_greater_than_minPrice(self):
        if self.minPrice > self.maxPrice:
            raise ValueError("minPrice is greater than maxPrice.")

    def isInteger(self, price):
        if isinstance(price, int):
            pass
        else:
            raise ValueError("StayPrice must be integer.")
