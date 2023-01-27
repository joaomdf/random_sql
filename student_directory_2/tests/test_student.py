from lib.student import Student

def test_student_instantiated():
    student = Student(1, 'Ryan', 1)
    assert student.id == 1
    assert student.name == 'Ryan'
    assert student.cohort_id == 1

def test_student_equal():
    student1 = Student(1, 'Ryan', 1)
    student2 = Student(1, 'Ryan', 1)
    assert student1 == student2

def test_student_formatting():
    student = Student(1, 'Ryan', 1)
    assert str(student) == 'Student(1, Ryan, 1)'