class SearchPrefecture:
    def __init__(self, prefecture):
        self.prefecture = prefecture

        # TODO: 引数の都道府県名をもとに、都道府県DBから都道府県コードと地域コードを取得する処理
        self.prefecture_code = "270000"
        self.region = [
            {"region_name": "大阪北部（茨木・高槻・箕面・伊丹空港）", "region_code": "271400"},
            {"region_name": "新大阪・江坂・十三・塚本", "region_code": "271700"},
            {"region_name": "大阪駅・梅田駅・福島・淀屋橋・本町", "region_code": "272000"},
            {"region_name": "大阪ベイエリア", "region_code": "272300"},
            {"region_name": "大阪城・京橋・市内東部", "region_code": "272600"},
            {"region_name": "心斎橋・なんば・四ツ橋", "region_code": "272900"},
            {"region_name": "上本町・天王寺・市内南部", "region_code": "273200"},
        ]
