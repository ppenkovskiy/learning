create table teacher
(
    teacher_id serial,
    first_name varchar,
    last_name varchar,
    birthday date,
    phone varchar,
    title varchar
);

alter table teacher
add column middle_name varchar;

alter table teacher
drop column middle_name;

alter table teacher
rename column birthday to birth_date;

alter table teacher
alter column phone set data type varchar(32);

insert into teacher (first_name, last_name, birth_date, phone, title)
values ('fn1', 'ln1', '1993-01-01', '123123', 't1'),
       ('fn1', 'ln1', '1993-01-01', '123123', 't1'),
       ('fn1', 'ln1', '1993-01-01', '123123', 't1');

select * from teacher;

truncate table teacher restart identity; -- restart column # 1

select * from teacher;
