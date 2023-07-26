select * from author;

update author
set full_name = 'Pavel', rating = 10
where author_id = 1;

select * from author;

delete from author
where rating = 10;

select * from author;

-- delete from author -- delete all lines in table;

truncate table author; -- delete lines from table without any logs

drop table book;

create table public.book
(
    book_id serial,
    title text not null,
    isbn character varying(32) not null,
    publisher_id integer not null,

    constraint pk_book_book_id primary key (book_id)
);

insert into book (title, isbn, publisher_id)
values ('title', 'isbn', 3)
returning book_id;

insert into book (title, isbn, publisher_id)
values ('title_3', 'isbn_3', 3)
returning *;

update author
set full_name = 'Walter'
where author_id = 2
returning *;

delete from author
where rating = 4
returning *;


