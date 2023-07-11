select * from customers;

select contact_name, city
from customers;

select order_id, shipped_date - order_date
from orders;

select  distinct city from customers;

select count(customer_id) from customers;

select count(distinct country) from customers