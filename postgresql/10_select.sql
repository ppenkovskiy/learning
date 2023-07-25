select product_id, product_name, unit_price
from products;


select product_id, product_name, unit_price * units_in_stock as price_units
from products;

select distinct country
from employees;

select distinct city
from employees;

select distinct city, country
from employees;

select count(distinct country)
from employees