select * from orders
where ship_country in ('Austria', 'France', 'Spain');

select * from orders
order by required_date desc, shipped_date asc;

select min(unit_price)
from products
where units_in_stock > 30;

select avg(shipped_date - order_date)
from orders
where ship_country = 'USA';

select sum(units_in_stock * unit_price)
from products
where discontinued <> 1;

