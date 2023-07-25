select *
from orders
where ship_country like 'U%';

select order_id, customer_id, freight, ship_country
from orders
where ship_country like 'N%'
order by freight desc
limit 10;

select first_name, last_name, home_phone, region
from employees
where region is null;

select count(*)
from customers
where region is not null;

select country, count(*)
from suppliers
group by country
order by count(*);

SELECT ship_country, SUM(freight)
FROM orders
WHERE ship_region IS NOT NULL
GROUP BY ship_country
HAVING SUM(freight) > 2750
ORDER BY sum(freight) DESC;

select country
from customers
union -- union is working like distinct
select country
from suppliers
order by country;

select country
from customers
intersect
select country
from suppliers
intersect
select country
from employees;

select country
from customers
intersect
select country
from suppliers
except
select country
from employees;