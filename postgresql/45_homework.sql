DROP TABLE IF EXISTS exam;

CREATE TABLE exam
(
    exam_id   SERIAL UNIQUE NOT NULL,
    exam_name VARCHAR(256),
    exam_date DATE
);

ALTER TABLE exam
    DROP CONSTRAINT exam_exam_id_key; -- removing unique constraint

ALTER TABLE exam
    ADD PRIMARY KEY (exam_id);

drop table if exists person cascade ;
drop table if exists book;

CREATE TABLE person
(
    person_id  INT         NOT NULL,
    first_name VARCHAR(64) NOT NULL,
    last_name  VARCHAR(64) NOT NULL,

    CONSTRAINT pk_person_person_id primary key (person_id)
);

drop table if exists passport cascade;

CREATE TABLE passport
(
    passport_id   INT,
    serial_number INT  NOT NULL,
    registration  TEXT NOT NULL,
    person_id     INT  NOT NULL,

    CONSTRAINT pk_passport_passport_id PRIMARY KEY (passport_id),
    CONSTRAINT fk_passport_person FOREIGN KEY (person_id) REFERENCES person (person_id)
);

drop table if exists student;

create table student
(
    student_id serial,
    full_name varchar,
    grade int default 1
);

insert into student
values (1, 'Vasia');

select * from student;

alter table student
alter column grade drop default;

alter table products
add constraint chk_products_price check (unit_price > 0);

select max(product_id) from products;

create sequence if not exists products_product_id_seq
start with 78 owned by products.product_id;

alter table products
alter column product_id set default nextval(products_product_id_seq);







