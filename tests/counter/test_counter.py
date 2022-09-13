from src.counter import count_ocurrences


def test_counter():
    path = 'src/jobs.csv'
    count = count_ocurrences(path, "javascript")
    assert count == 122
