DROP TABLE if EXISTS artists;
DROP SEQUENCE if EXISTS artist_id_seq;

CREATE SEQUENCE if not EXISTS artists_id_seq;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name text,
    genre text
);

INSERT INTO artists (name, genre) VALUES ('ABBA', 'pop');
INSERT INTO artists (name, genre) VALUES ('Pixies', 'rock');
INSERT INTO artists (name, genre) VALUES ('Taylor Swift', 'pop');
INSERT INTO artists (name, genre) VALUES ('Nina Simone', 'r&b');
