drop table if exists customer cascade;

create table customer
(
    customer_id serial,
    full_name text,
    status char default 'regular'
);

