import pytest
from being_late import countMin


# test basic use

def test_happyPath () :
    minutes = [4, 6, 0, 13, 16, 0, 3, 0, 8, 17]
    assert countMin (minutes) == 2

def test_emptyList () :
    minutes = []
    assert countMin (minutes) == 0

def test_allUnderThreshold () :
    minutes = [4, 6, 0, 13, 14, 0, 3, 0, 8, 12]
    assert countMin (minutes) == 0


def test_allAboveThreshold () :
    minutes = [24, 16, 20, 23, 16, 20, 23, 20, 18, 17]
    assert countMin (minutes) == 10

def test_tresholdValuePresent () :
    minutes = [4, 6, 0, 13, 15, 16, 0, 3, 0, 8, 17]
    assert countMin (minutes) == 2