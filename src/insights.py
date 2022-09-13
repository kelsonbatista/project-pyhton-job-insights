from src.jobs import read
# from rich import print


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs = read(path)
    jobs_type = [job["job_type"] for job in jobs]
    # for job in jobs:
    # jobs_type.append(job["job_type"])
    # return list(jobs_set)
    # print(jobs_set)
    # return job
    return list(set(jobs_type))

# print(get_unique_job_types('src/jobs.csv'))


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    # jobs_list = [job for job in jobs if job["job_type"] == job_type]
    # for job in jobs:
    #     if job["job_type"] == job_type:
    #         jobs_list.append(job)
    # return jobs_list
    return [job for job in jobs if job["job_type"] == job_type]

# print(filter_by_job_type(read('src/jobs.csv'), "CONTRACTOR"))


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    jobs = read(path)
    jobs_industry = [job["industry"] for job in jobs]
    return list(filter(None, set(jobs_industry)))

# print(get_unique_industries('src/jobs.csv'))


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    pass


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    pass


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    try:
        if "min_salary" not in job or "max_salary" not in job:
            raise ValueError("Salary doesn't exists")
        elif job["min_salary"] > job["max_salary"]:
            raise ValueError("Min salary cannot be greater than max salary")
        elif int(job["min_salary"]) <= salary <= int(job["max_salary"]):
            return True
        return False
    except TypeError:
        raise ValueError("Salary is not a valid integer")


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return [job for job in jobs if matches_salary_range(job, salary)]
