import pytest

from src.query_param import QueryParam
from src.stay_date import StayDate


def test_query_parameter_is_str():
    staydate = StayDate()
    qp = QueryParam(staydate)
    query_param = qp.query_param
    assert type(query_param) is str


def test_empty_query_param():
    staydate = StayDate()
    qp = QueryParam(staydate)
    query_param = qp.query_param
    assert (
        query_param
        == "?screenId=UWW1402&distCd=01&photo=1&activeSort=0&rootCd=04&stayYear=&stayMonth=&stayDay=&stayCount=1&roomCount=1&adultNum=2&minPrice=0&maxPrice=&roomCrack=200000&kenCd=&lrgCd=&mvTabFlg=2"
    )


def test_query_param_20220520():
    staydate = StayDate(stayYear=2022, stayMonth=5, stayDay=20)
    qp = QueryParam(staydate=staydate)
    query_param = qp.query_param
    assert "stayYear=2022&stayMonth=5&stayDay=20" in query_param
