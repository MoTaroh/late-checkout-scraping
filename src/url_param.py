class UrlParam:
    def __init__(self, staydate, prefecture):  # TODO: 都道府県インスタンスを受け取る
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
        # TODO: 都道府県インスタンスから都道府県コードと地域コードを取得する
        self._kenCd = prefecture.prefecture_code  # 都道府県コード
        self._lrgCd = prefecture.region_code  # TODO: 地域コード（リスト型）
        self._mvTabFlg = "2"
        # TODO: 地域コードをループさせて、パスパラメータとクエリパラメータを生成
        self.url_param = []
        for region_code in self._lrgCd:
            path_param = f"{self._kenCd}/LRG_{region_code}/"
            query_param = f"?screenId={self._screenId}&distCd={self._distCd}&photo={self._photo}&activeSort={self._activeSort}&rootCd={self._rootCd}&stayYear={self._stayYear}&stayMonth={self._stayMonth}&stayDay={self._stayDay}&stayCount={self._stayCount}&roomCount={self._roomCount}&adultNum={self._adultNum}&minPrice={self._minPrice}&maxPrice={self._maxPrice}&roomCrack={self._roomCrack}&kenCd={self._kenCd}&lrgCd={region_code}&mvTabFlg={self._mvTabFlg}"
            url_param = path_param + query_param
            self.url_param.append(url_param)
        # パスパラメータ
        # self.path_param = ["pathparam"]
        # クエリパラメータ
        # self.query_param = [
        #     f"?screenId={self._screenId}&distCd={self._distCd}&photo={self._photo}&activeSort={self._activeSort}&rootCd={self._rootCd}&stayYear={self._stayYear}&stayMonth={self._stayMonth}&stayDay={self._stayDay}&stayCount={self._stayCount}&roomCount={self._roomCount}&adultNum={self._adultNum}&minPrice={self._minPrice}&maxPrice={self._maxPrice}&roomCrack={self._roomCrack}&kenCd={self._kenCd}&lrgCd={self._lrgCd}&mvTabFlg={self._mvTabFlg}"
        # ]
        # # TODO: ２つを合わせたURLパラメータを生成
        # self.url_param = [self.query_param]
