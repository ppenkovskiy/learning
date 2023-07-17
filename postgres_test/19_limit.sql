select product_name, unit_price
from products
where discontinued <> 1
order by unit_price desc
limit 5
