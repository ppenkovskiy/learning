select * from author;

update author
set full_name = 'name_0', rating = 5
where author_id = 1;

select * from author
order by author_id;

delete from author
where rating < 4.5;

select * from author
order by author_id;

delete from author;

select * from author;

truncate table author;

drop table if exists book;

create table public.book
(
    book_id serial,
    title text not null,
    isbn character varying(32) not null,
    publisher_id integer not null,

    -- primary key(id),
    constraint pk_book_book_id primary key (book_id)
);

insert into book (title, isbn, publisher_id)
values ('title', 'isbn', 3)
returning book_id;

insert into author
values (1, 'name_1', 9),
       (2, 'name_2', 8),
       (3, 'name_3', 7),
       (4, 'name_4', 4),
       (5, 'name_5', 3);

update author
set full_name = 'default_name', rating = 10
where author_id = 1
returning *;






