DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS author;

CREATE TABLE book
(
    book_id int PRIMARY KEY,
    title   text NOT NULL,
    isbn    text NOT NULL
);

CREATE TABLE author
(
    author_id int PRIMARY KEY,
    full_name text NOT NULL,
    rating real
);

CREATE TABLE book_author
(


)