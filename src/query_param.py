class QueryParam:
    def __init__(self, year="", month="", date=""):
        self.query_param = "stayYear={}&stayMonth={}&stayDay={}".format(
            year, month, date
        )
