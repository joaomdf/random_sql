DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;
DROP TABLE IF EXISTS cohorts;
DROP SEQUENCE IF EXISTS cohorts_id_seq;

CREATE SEQUENCE IF NOT EXISTS cohorts_id_seq;
CREATE TABLE cohorts (
    id SERIAL PRIMARY KEY,
    name text,
    starting_date date
);

CREATE SEQUENCE IF NOT EXISTS students_id_seq;
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name text,
    cohort_id int,
    constraint fk_cohort foreign key(cohort_id)
        references cohorts(id)
        on delete cascade
);

INSERT INTO cohorts (name, starting_date) VALUES ('SoftDev', '2022-10-19');
INSERT INTO cohorts (name, starting_date) VALUES ('QualEng', '2022-10-19');
INSERT INTO cohorts (name, starting_date) VALUES ('DevOps', '2022-11-10');

INSERT INTO students (name, cohort_id) VALUES ('Sam', 1);
INSERT INTO students (name, cohort_id) VALUES ('Adam', 2);
INSERT INTO students (name, cohort_id) VALUES ('Ira', 1);
INSERT INTO students (name, cohort_id) VALUES ('Avi', 2);
INSERT INTO students (name, cohort_id) VALUES ('Sanam', 2);
INSERT INTO students (name, cohort_id) VALUES ('Trixie', 3);
INSERT INTO students (name, cohort_id) VALUES ('Katya', 3);