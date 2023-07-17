select ship_country, count(*)
from orders
where freight > 50
group by ship_country
order by count(*) desc;

select category_id, sum(units_in_stock)
from products
group by category_id
order by sum(units_in_stock)