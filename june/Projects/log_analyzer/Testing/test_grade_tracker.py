import pytest
from grade_tracker import GradeTracker


# A fixture to provide a clean tracker instance for every test
@pytest.fixture
def empty_tracker():
    return GradeTracker("Lourdes")


def test_add_grade(empty_tracker):
    empty_tracker.add_grade(85)
    assert 85 in empty_tracker.grades
    assert len(empty_tracker.grades) == 1


def test_calculate_average(empty_tracker):
    empty_tracker.add_grade(75)
    assert empty_tracker.is_passing() is True


def test_invalid_grade_raises_exception(empty_tracker):
    # This checks that our code safely creashes when given bad data
    with pytest.raises(ValueError):
        empty_tracker.add_grade(-5)
