DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS accounts;
DROP SEQUENCE IF EXISTS accounts_id_seq;

CREATE SEQUENCE IF NOT EXISTS accounts_id_seq;
CREATE TABLE accounts(
    id SERIAL PRIMARY KEY,
    email text,
    username text
);

INSERT INTO accounts (email, username) VALUES ('me@thingy', 'me');
INSERT INTO accounts (email, username) VALUES ('you@whatchamacallit', 'you');
INSERT INTO accounts (email, username) VALUES ('them@musknetworks', 'them');

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts(
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    views int,
    account_id int,
    CONSTRAINT fk_account FOREIGN KEY(account_id)
        REFERENCES accounts(id)
        ON DELETE CASCADE
);

INSERT INTO posts (title, content, views, account_id) VALUES ('My title', 'My content', 45, 1);
INSERT INTO posts (title, content, views, account_id) VALUES ('My title 2: Electric Boogaloo', 'Sequel shit', 2000, 1);
INSERT INTO posts (title, content, views, account_id) VALUES ('Your title', 'Your content', 2, 2);
INSERT INTO posts (title, content, views, account_id) VALUES ('Your title 2: Electric Boogaloo', 'Sequel shit plagiarism', 35, 2);
INSERT INTO posts (title, content, views, account_id) VALUES ('Megalomaniac title', 'I am great and all that', 5000, 3);
