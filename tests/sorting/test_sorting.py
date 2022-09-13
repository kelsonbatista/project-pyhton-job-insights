from src.sorting import sort_by
# from src.jobs import read

jobs = [{
    'title': 'Full stack end developer',
    'min_salary': '4000',
    'max_salary': '8000'
}, {
    'title': 'Back end developer',
    'min_salary': '',
    'max_salary': '3000'
}, {
    'title': 'Front end developer',
    'min_salary': '1000',
    'max_salary': ''
}]

sort_max_salary = [{
    'title': 'Full stack end developer',
    'min_salary': '4000',
    'max_salary': '8000'
}, {
    'title': 'Back end developer',
    'min_salary': '',
    'max_salary': '3000'
}, {
    'title': 'Front end developer',
    'min_salary': '1000',
    'max_salary': ''
}]

sort_min_salary = [{
    'title': 'Front end developer',
    'min_salary': '1000',
    'max_salary': ''
}, {
    'title': 'Full stack end developer',
    'min_salary': '4000',
    'max_salary': '8000'
}, {
    'title': 'Back end developer',
    'min_salary': '',
    'max_salary': '3000'
}]


def test_sort_by_criteria():
    # path = 'tests/mocks/jobs_with_salaries.csv'
    # jobs = read(path)

    sort_by(jobs, "max_salary")
    assert jobs == sort_max_salary
    sort_by(jobs, "min_salary")
    assert jobs == sort_min_salary
