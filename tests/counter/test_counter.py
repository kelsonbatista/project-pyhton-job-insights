from src.counter import count_ocurrences
from tests.counter.mocks import count_word_ocurrences


def test_counter():
    count = count_ocurrences("src/jobs.csv", "Javascript")
    result = count_word_ocurrences("src/jobs.csv", "Javascript")
    assert result != count
