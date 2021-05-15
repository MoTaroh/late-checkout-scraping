import pytest

from src.stay_date import StayDate


def test_staydate():
    staydate = StayDate(stayYear=2021, stayMonth=5, stayDay=20)
    assert staydate.stayYear == "2021"
    assert staydate.stayMonth == "5"
    assert staydate.stayDay == "20"
