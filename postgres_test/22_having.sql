select category_id, sum(unit_price * products.units_in_stock)
from products
