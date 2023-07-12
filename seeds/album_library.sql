DROP TABLE if exists albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title text,
    release_year int,
    artist_id int
);

INSERT INTO albums (title, release_year, artist_id) VALUES ('Album one', 2023, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Album two', 2000, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Album three', 2011, 2);

