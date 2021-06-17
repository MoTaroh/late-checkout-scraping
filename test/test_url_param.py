import pytest

from src.url_param import UrlParam
from src.stay_date import StayDate
from src.search_prefecture import SearchPrefecture


# def test_path_param_is_str():
#     staydate = StayDate()
#     up = UrlParam(staydate)
#     assert type(up.path_param) is str


def test_url_param_is_list():
    staydate = StayDate()
    pref = SearchPrefecture("大阪")
    up = UrlParam(staydate, pref)
    assert type(up.url_param) is list


# def test_url_param_contains_path_query():
#     assert


# def test_query_parameter_is_list():
#     staydate = StayDate()
#     up = UrlParam(staydate)
#     query_param = up.query_param
#     assert type(query_param) is list


# def test_empty_query_param():
#     staydate = StayDate()
#     up = UrlParam(staydate)
#     query_param = up.query_param
#     assert (
#         query_param[0]
#         == "?screenId=UWW1402&distCd=01&photo=1&activeSort=0&rootCd=04&stayYear=&stayMonth=&stayDay=&stayCount=1&roomCount=1&adultNum=2&minPrice=0&maxPrice=&roomCrack=200000&kenCd=&lrgCd=&mvTabFlg=2"
#     )


# def test_query_param_20220520():
#     staydate = StayDate(stayYear=2022, stayMonth=5, stayDay=20)
#     up = UrlParam(staydate=staydate)
#     query_param = up.query_param
#     assert "stayYear=2022&stayMonth=5&stayDay=20" in query_param[0]
