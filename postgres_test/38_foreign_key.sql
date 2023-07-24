drop table if exists publisher;
drop table if exists book_author;
drop table if exists book;

create table publisher
(
    publisher_id int,
    publisher_name varchar(128) not null,
    address text,
    constraint pk_publisher_publisher_id primary key(publisher_id)
)





