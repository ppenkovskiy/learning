DROP TABLE IF EXISTS publisher;

CREATE TABLE publisher
(
    publisher_id integer PRIMARY KEY,
    org_name     varchar(128) NOT NULL,
    address      text
);

DROP TABLE IF EXISTS book;

CREATE TABLE book
(
    book_id integer PRIMARY KEY,
    title   text        NOT NULL,
    isbn    varchar(32) NOT NULL
)
