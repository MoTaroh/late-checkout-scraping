import pytest

from src.stay_date import StayDate


def test_staydate():
    staydate = StayDate(stayYear=2022, stayMonth=5, stayDay=20)
    assert staydate.stayYear == "2022"
    assert staydate.stayMonth == "5"
    assert staydate.stayDay == "20"


def test_staydate_is_outdated():
    with pytest.raises(ValueError):
        staydate = StayDate(stayYear=1990, stayMonth=5, stayDay=20)


def test_staydate_is_empty():
    staydate = StayDate()
    assert staydate.stayYear == ""
    assert staydate.stayMonth == ""
    assert staydate.stayDay == ""
