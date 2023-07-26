drop table if exists author;
drop table if exists best_author;

create table author
(
    author_id int not null,
    full_name varchar(32) not null,
    rating int not null
);

insert into author
values (1, 'name_1', 9),
       (2, 'name_2', 8),
       (3, 'name_3', 7),
       (4, 'name_4', 4),
       (5, 'name_5', 3);

select * from author;

select * into best_author -- autocreating table
from author
where rating > 5;

select * from best_author;

insert into best_author
select * from author
where rating < 5;

select * from best_author;

