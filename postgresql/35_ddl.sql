create table student
(
    student_id serial,
    first_name varchar,
    last_name varchar,
    birthdate date,
    phone varchar
);

create table cathedra
(
    cathedra_id serial,
    cathedra_name varchar,
    dean varchar
);

alter table student
add column middle_name varchar;

alter table student
add column rating float;

alter table student
add column enrolled date;

alter table student
drop column middle_name;

alter table cathedra
rename to chair;

alter table chair
rename cathedra_name to chair_name;

alter table chair
rename cathedra_id to chair_id;

alter table student
alter column first_name set data type varchar(64);
alter table student
alter column last_name set data type varchar(64);
alter table student
alter column phone set data type varchar(32);

create table faculty
(
    faculty_id serial,
    faculty_name varchar
);

insert into faculty (faculty_name)
values ('faculty_1'),
       ('faculty_2'),
       ('faculty_3');

select * from faculty;

truncate table faculty; -- delete all data from table

select * from faculty;

drop table faculty;