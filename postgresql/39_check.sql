drop table if exists book;

create table book
(
    book_id int,
    title text not null,
    isbn varchar(32) not null,
    publisher_id int,

    constraint pk_book_book_id primary key (book_id)
);

alter table book
add column price decimal constraint chk_book_price check (price >= 0);

insert into book
values
(1, 't1', 'isbn1', 1, 100);




