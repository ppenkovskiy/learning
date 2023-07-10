DROP TABLE IF EXISTS book;

CREATE TABLE book
(
    book_id         integer PRIMARY KEY,
    title           text                                        NOT NULL,
    isbn            varchar(32)                                 NOT NULL,
    fk_publisher_id integer REFERENCES publisher (publisher_id) NOT NULL
);

INSERT INTO book
VALUES (1, 'Book_1', '123123123', 1),
       (2, 'Book_2', '123123124', 1),
       (3, 'Book_3', '123123123555', 2),
       (4, 'Book_3', '123123123555', 3),
       (5, 'Book_3', '123123123555', 3)

