drop table if exists publisher cascade;
drop table if exists book_author cascade;
drop table if exists book cascade;

create table publisher
(
    publisher_id int,
    publisher_name varchar(128) not null,
    address text,

    constraint pk_publisher_publisher_id primary key(publisher_id)
);

create table book
(
    book_id int,
    title text not null,
    isbn varchar(32) not null,
    publisher_id int,

    constraint pk_book_book_id primary key(book_id)
);

insert into publisher
values
(1, 'p1', 'a1'),
(2, 'p2', 'a2'),
(3, 'p3', 'a3'),
(4, 'p4', 'a4');

select * from publisher;

insert into book
values
(1, 't1', 'isbn1', 100);

select * from book;

truncate table book;

alter table book
add constraint fk_books_publisher foreign key (publisher_id) references publisher(publisher_id);

insert into book
values
(1, 't1', 'isbn1', 4);

select * from book;

alter table book
drop constraint fk_books_publisher;

