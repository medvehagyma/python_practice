import pytest
from ages import olderThan28


def test_happyPath () :
    persons = [{"name": "Falesz", "age": 29},
               {"name": "Encsi", "age": 26}, 
               {"name": "Virág", "age": 27}, 
               {"name": "Anna", "age": 39}]

    assert olderThan28(persons) == True


def test_emptyList () :
    persons = []
    assert olderThan28(persons) == False


def test_allUnder28 () :
    persons = [{"name": "Falesz", "age": 19},
               {"name": "Encsi", "age": 16}, 
               {"name": "Virág", "age": 17}, 
               {"name": "Anna", "age": 19}]

    assert olderThan28(persons) == False