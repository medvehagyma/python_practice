import pytest
from visitors import calcVisitors

def test_happyPath () :
    visitors = [37, 17, 24, 26, 51, 62, 21]
    assert calcVisitors (visitors) == 238

def test_emptyList () :
    visitors = []
    assert calcVisitors (visitors) == 0

def test_oneEntry () :
    visitors = [37]
    assert calcVisitors (visitors) == 37

def test_allZeros () :
    visitors = [0, 0, 0, 0, 0, 0, 0]
    assert calcVisitors (visitors) == 0

def test_orderIndependence () :
    visitors = [24, 17, 37, 62, 26, 21, 51]
    assert calcVisitors (visitors) == 238
