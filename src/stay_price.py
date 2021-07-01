class Price:
    def __init__(self, minPrice="", maxPrice=""):
        self.minPrice = minPrice
        self.maxPrice = maxPrice

        if self.minPrice > self.maxPrice:
            raise ValueError("minPrice is greater than maxPrice.")
