DROP TABLE IF EXISTS comments;
DROP SEQUENCE IF EXISTS comments_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text
);

CREATE SEQUENCE IF NOT EXISTS comments_id_seq;
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    content text,
    author text,
    post_id int,
    constraint fk_post foreign key(post_id)
        references posts(id)
        on delete cascade
);


INSERT INTO posts (title, content) VALUES ('Top 10 anime betrayals', 'I only watched DB and Death Note. Ask a weeb.');
INSERT INTO posts (title, content) VALUES ('How to teach your fish to fish?', 'Nature over nurture.');
INSERT INTO posts (title, content) VALUES ('The plague in Deadwood?', 'A prime example of journalistic integrity!');

INSERT INTO comments (content, author, post_id) VALUES ('Something about incels...', 'that_one_alpha_nonsense_guy', 1);
INSERT INTO comments (content, author, post_id) VALUES ('Something transphobic...', 'MadPetersonFan420', 1);
INSERT INTO comments (content, author, post_id) VALUES ('My goldfish finally learned to breath underwater, thank you!', 'hellicopter_fish_parent',2);
INSERT INTO comments (content, author, post_id) VALUES ('Instructions unclear, fish going to therapy now.', 'blazed_and_confused', 2);
INSERT INTO comments (content, author, post_id) VALUES ('Bleep you, you limp bleeped mother bleeper!', 'calamity_jane', 3);
INSERT INTO comments (content, author, post_id) VALUES ('Let us not appear as twins.', 'al_swedgin', 3);