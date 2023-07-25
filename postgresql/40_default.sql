drop table if exists customer cascade;

create table customer
(
    customer_id serial,
    full_name   text,
    status      char default 'r',

    constraint pk_customer_customer_id primary key (customer_id),
    constraint chk_customer_status check (status = 'r' or status ='p')
);

insert into customer (full_name)
values ('name');

select * from customer;

