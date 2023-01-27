DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    average_cooking_time VARCHAR(255),
    rating INT,
    CHECK (rating >= 1),
    CHECK (rating <= 5)
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Francesinha', '60 min', 5);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Butter Chicken', '90 min', 5);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Dried Ass Chicken', 'Who knows, who cares', 1);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Stir-fry', '30 min', 4);