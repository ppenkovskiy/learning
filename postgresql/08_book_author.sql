DROP TABLE IF EXISTS book CASCADE;
DROP TABLE IF EXISTS author CASCADE;
DROP TABLE IF EXISTS book_author CASCADE;

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
    rating    real
);

CREATE TABLE book_author
(
    book_id int references book(book_id),
    author_id int references author(author_id),

    CONSTRAINT book_author_pkey PRIMARY KEY (book_id, author_id)  -- composite key
);

INSERT INTO book
VALUES (1, 'Book_1', '123123121'),
       (2, 'Book_2', '123123122'),
       (3, 'Book_3', '123123123'),
       (4, 'Book_4', '123123124'),
       (5, 'Book_5', '123123125');

INSERT INTO author
VALUES (1, 'Author_1', 4.5),
       (2, 'Author_2', 4.6),
       (3, 'Author_3', 4.7);

INSERT INTO book_author
values (1, 1),
       (2, 1),
       (3, 2),
       (4, 3),
       (5, 2)

