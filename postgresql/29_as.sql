select count(*) as employees_count
from employees;

select count(distinct country) as country
from employees;

select category_id, sum(units_in_stock) as units_in_stock
from products
group by category_id
order by units_in_stock desc
limit 5;

select category_id, sum(unit_price * units_in_stock) as total_price
from products
where discontinued <> 1
group by category_id
having sum(unit_price * units_in_stock) > 5000
order by total_price desc