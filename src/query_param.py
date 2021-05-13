class QueryParam:
    def __init__(self, year="", month="", date=""):
        self.query_param = "?screenId=UWW1402&distCd=01&photo=1&activeSort=0&rootCd=04&stayYear={}&stayMonth={}&stayDay={}&stayCount=&roomCount=&adultNum=&minPrice=&maxPrice=&roomCrack=200000&kenCd=&lrgCd=&mvTabFlg=2".format(
            year, month, date
        )
