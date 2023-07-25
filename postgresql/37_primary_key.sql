drop table chair;

create table chair
(
    chair_id   serial primary key,
    -- primary key is used on only 1 column in table
    -- primary key guarantee that you can't paste duplicate with the same chair_id
    -- also primary key guarantee that you can't paste Null as a chair_id
    chair_name varchar,
    dean       varchar
);

insert into chair
values (1, 'name', 'dean');

select *
from chair;

insert into chair
values (2, 'name2', 'dean2');

select *
from chair;

drop table chair;

create table chair
(
    chair_id   serial unique not null,
    -- primary key is used on only 1 column in table
    -- unique not null can be used on a multiple columns in table unlike primary key
    chair_name varchar,
    dean       varchar
);

drop table chair;

create table chair
(
    chair_id   serial,
    chair_name varchar,
    dean       varchar
);

alter table chair
add primary key(chair_id);









