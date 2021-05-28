class QueryParam:
    def __init__(self, staydate):
        self._stayYear = staydate.stayYear
        self._stayMonth = staydate.stayMonth
        self._stayDay = staydate.stayDay
        self._stayCount = "1"
        self._roomCount = "1"
        self._adultNum = "2"
        self._minPrice = "0"
        self._maxPrice = ""
        # 用途不明の固定値
        self._screenId = "UWW1402"
        self._distCd = "01"
        self._photo = "1"
        self._activeSort = "0"
        self._rootCd = "04"
        self._roomCrack = "200000"
        self._kenCd = ""
        self._lrgCd = ""
        self._mvTabFlg = "2"
        # クエリパラメータ
        self.query_param = f"?screenId={self._screenId}&distCd={self._distCd}&photo={self._photo}&activeSort={self._activeSort}&rootCd={self._rootCd}&stayYear={self._stayYear}&stayMonth={self._stayMonth}&stayDay={self._stayDay}&stayCount={self._stayCount}&roomCount={self._roomCount}&adultNum={self._adultNum}&minPrice={self._minPrice}&maxPrice={self._maxPrice}&roomCrack={self._roomCrack}&kenCd={self._kenCd}&lrgCd={self._lrgCd}&mvTabFlg={self._mvTabFlg}"
