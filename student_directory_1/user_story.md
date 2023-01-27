As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.

Nouns
student_names, student_cohorts

Record             Properties
student_records    student_name, student_cohort


id:SERIAL
student_name:text
student_cohort:text

CREATE TABLE student_records (
    id SERIAL PRIMARY KEY,
    student_name text,
    student_cohort text
);

psql -h 127.0.0.1 student_records < students_records.sql