DROP TABLE IF EXISTS person CASCADE;
DROP TABLE IF EXISTS passport CASCADE;

CREATE TABLE person
(
    person_id  int PRIMARY KEY,
    first_name varchar(64) NOT NULL,
    last_name  varchar(64) NOT NULL
);

CREATE TABLE passport
(
    passport_id        int PRIMARY KEY,
    serial_number      int NOT NULL,
    fk_passport_person int REFERENCES person (person_id)
);

ALTER TABLE passport
    ADD COLUMN registration text NOT NULL;

INSERT INTO person
VALUES (1, 'John', 'Snow'),
       (2, 'Ned', 'Stark'),
       (3, 'Rob', 'Baratheon');

INSERT INTO passport
VALUES (1, 12312333, 3, 'Winterfell'),
       (2, 12312334, 2, 'Winterfell'),
       (3, 12312335, 1, 'Winterfell')


