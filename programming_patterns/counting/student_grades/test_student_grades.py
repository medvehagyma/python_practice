import pytest
from student_grades import countGrades


# test basic use

def test_happyPath () :

    grades = [2, 4, 5, 3, 4, 4, 3, 4]

    assert countGrades (grades) == 5



def test_emptyList () :

    grades = []

    assert countGrades (grades) == 0



def test_allUnderThreshold () :

    grades = [1, 2, 1, 3, 2]

    assert countGrades (grades) == 0


def test_allAboveThreshold () :

    grades = [4, 4, 5, 5, 4, 5]

    assert countGrades (grades) == 6