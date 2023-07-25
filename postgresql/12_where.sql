SELECT company_name, contact_name, phone, country
FROM customers
WHERE country = 'USA';

SELECT *
FROM products
WHERE unit_price > 20;

select count(*)
from products
where unit_price > 20;


select *
from products
where discontinued = 1;


select * from customers
where city <> 'Berlin';
-- not equal - <>

select *
from orders
where order_date > '1998-03-01';

select *
from orders
where order_date >= '1998-03-01';

