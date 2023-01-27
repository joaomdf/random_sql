from lib.cohort import Cohort

def test_cohort_instantiated():
    cohort = Cohort(1, 'MachDes', '2021-01-14')
    assert cohort.id == 1
    assert cohort.name == 'MachDes'
    assert cohort.starting_date == '2021-01-14'
    assert cohort.students == []

def test_cohort_equal():
    cohort1 = Cohort(1, 'MachDes', '2021-01-14')
    cohort2 = Cohort(1, 'MachDes', '2021-01-14')
    assert cohort1 == cohort2

def test_cohort_formatting():
    cohort = Cohort(1, 'MachDes', '2021-01-14')
    assert str(cohort) == 'Cohort(1, MachDes, 2021-01-14, [])'