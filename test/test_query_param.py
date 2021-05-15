import pytest

from src.query_param import QueryParam
from src.stay_date import StayDate


def test_query_parameter_is_str():
    qp = QueryParam()
    query_param = qp.query_param
    assert type(query_param) is str


def test_empty_query_param():
    qp = QueryParam()
    query_param = qp.query_param
    assert (
        query_param
        == "?screenId=UWW1402&distCd=01&photo=1&activeSort=0&rootCd=04&stayYear=&stayMonth=&stayDay=&stayCount=1&roomCount=1&adultNum=2&minPrice=0&maxPrice=&roomCrack=200000&kenCd=&lrgCd=&mvTabFlg=2"
    )


def test_query_param_20210520():
    qp = QueryParam(year=2021, month=5, date=20)
    query_param = qp.query_param
    assert "stayYear=2021&stayMonth=5&stayDay=20" in query_param


def test_query_param_20200101():
    qp = QueryParam(year=2020, month=1, date=1)
    query_param = qp.query_param
    assert "stayYear=2020&stayMonth=1&stayDay=1" in query_param
