select * from products
where unit_price > 25 and units_in_stock > 40;

select *
from customers
where city = 'Berlin' or city = 'London' or city = 'San Francisco';

select *
from orders
where shipped_date > '1998-04-30' and (freight < 75 or freight > 150);

