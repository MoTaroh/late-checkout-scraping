import datetime


class StayDate:
    def __init__(self, stayYear, stayMonth, stayDay):
        # 引数チェック
        staydate = datetime.date(stayYear, stayMonth, stayDay)
        if staydate < datetime.date.today():
            datetime.date.strftime
            raise ValueError("Your staydate is outdated.")

        self.stayYear = str(stayYear)
        self.stayMonth = str(stayMonth)
        self.stayDay = str(stayDay)
