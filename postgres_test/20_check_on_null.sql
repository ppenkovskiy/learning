select ship_city, ship_region, ship_country
from orders
where ship_region is null;

select ship_city, ship_region, ship_country
from orders
where ship_region is not null;

