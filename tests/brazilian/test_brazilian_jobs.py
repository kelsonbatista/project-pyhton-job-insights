from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = 'tests/mocks/brazilians_jobs.csv'
    result = {'salary': '2000', 'title': 'Maquinista', 'type': 'trainee'}
    assert result in read_brazilian_file(path)
