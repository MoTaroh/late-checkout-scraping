import pytest

from src.query_param import QueryParam


def test_query_parameter_is_str():
    qp = QueryParam()
    query_param = qp.query_param
    assert type(query_param) is str


def test_query_param_20210520():
    qp = QueryParam(year=2021, month=5, date=20)
    query_param = qp.query_param
    assert query_param == "stayYear=2021&stayMonth=5&stayDay=20"


def test_query_param_20200101():
    qp = QueryParam(year=2020, month=1, date=1)
    query_param = qp.query_param
    assert query_param == "stayYear=2020&stayMonth=1&stayDay=1"
