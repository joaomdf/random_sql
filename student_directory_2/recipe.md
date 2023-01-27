As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' starting dates.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.

Nouns:
students, student name, cohort name, cohort starting date, student cohort

RECORD      PROPERTIES
students    student_name, student_cohort
cohorts     cohort_name, cohort_starting_date

dabatase_name => student_directory_two_db

Table cohorts
id: SERIAL
name: text
starting_date: date

Table students
id: SERIAL
name: text
cohort: text



Can one student have more than one cohort? No
Can one cohort have more than one student? Yes

A cohort has many students
students belongs to cohort
The foreign key is on the students table
