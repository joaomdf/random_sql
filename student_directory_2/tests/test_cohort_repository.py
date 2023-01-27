from datetime import date
from lib.cohort import Cohort
from lib.student import Student
from lib.cohort_repository import CohortRepository

def test_all_cohorts(db_connection):
    db_connection.seed('seeds/student_records_2.sql')
    repo = CohortRepository(db_connection)
    cohorts = repo.all()
    assert cohorts == [
        Cohort(1, 'SoftDev', date(2022,10,19)),
        Cohort(2, 'QualEng', date(2022,10,19)),
        Cohort(3, 'DevOps', date(2022,11,10))
        ]

def test_find_cohort(db_connection):
    db_connection.seed('seeds/student_records_2.sql')
    repo = CohortRepository(db_connection)
    assert repo.find(1) == Cohort(1, 'SoftDev', date(2022,10,19))

def test_find_with_cohort_students(db_connection):
    db_connection.seed('seeds/student_records_2.sql')
    repo = CohortRepository(db_connection)
    assert repo.find_with_students(2) == Cohort(2, 'QualEng', date(2022,10,19), [Student(2, 'Adam', 2), Student(4, 'Avi', 2), Student(5, 'Sanam', 2)])