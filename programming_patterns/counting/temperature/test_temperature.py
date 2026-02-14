import pytest
from temperature import cntHotterThan28 


# run the tester with the following command:
# py -m pytest test_temperature.py


# testing basic use

def test_happyPath () :

    temperatures = [23, 26.3, 29, 36, 37.6, 39]

    assert cntHotterThan28 (temperatures) == 4



def test_emptyList () :

    temperatures = []

    assert cntHotterThan28 (temperatures) == 0



def test_tresholdValueCounted () :

    temperatures = [23, 26.3, 28, 29, 36, 37.6, 39]

    assert cntHotterThan28 (temperatures) == 4
