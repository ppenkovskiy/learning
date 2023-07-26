drop table if exists book;

create table book
(
    book_id int not null,
    title text not null,
    isbn varchar(32) not null,
    publisher_id int not null,

    constraint pk_book_book_id primary key (book_id)
);

select * from book;

create sequence if not exists book_book_id_seq
start with 1 owned by book.book_id;

alter table book
alter column book_id set default nextval('book_book_id_seq');

insert into book(title, isbn, publisher_id)
values('title', 'isbn', 1);

select * from book;

drop table if exists book;

create table book
(
    book_id int not null,
    title text not null,
    isbn varchar(32) not null,
    publisher_id int not null,

    constraint pk_book_book_id primary key (book_id)
);

select * from book;

drop table if exists book;

create table book
(
    book_id int generated always as identity not null,
    title text not null,
    isbn varchar(32) not null,
    publisher_id int not null,

    constraint pk_book_book_id primary key (book_id)
);

-- insert into book
-- values(10, 'title', 'isbn', 1); -- raises exception

insert into book(title, isbn, publisher_id)
values('title_1', 'isbn_1', 1);

select * from book;

