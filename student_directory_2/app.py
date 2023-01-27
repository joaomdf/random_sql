from lib.cohort_repository import CohortRepository
from lib.database_connection import DatabaseConnection

connection = DatabaseConnection()
connection.connect()
connection.seed("seeds/student_records_2.sql")

repo = CohortRepository(connection )

cohort = repo.find_with_students(2)
print(f"Cohort\nName: {cohort.name}  ID: {cohort.id}\n\nStudents:")
for student in cohort.students:
    print(f"Name: {student.name}  ID: {student.id}")