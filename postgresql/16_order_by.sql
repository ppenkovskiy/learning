select distinct country
from customers
order by country asc;

select distinct country
from customers
order by country desc;

select distinct country, city
from customers
order by country desc, city asc;

select distinct country, city
from customers
order by country desc, city desc;

select ship_city, order_date
from orders
where ship_city = 'London'
order by order_date;

select min(order_date)
from orders
where ship_city = 'London';

select avg(unit_price)
from products
where discontinued <> 1;

select sum(units_in_stock)
from products
where discontinued <> 1


