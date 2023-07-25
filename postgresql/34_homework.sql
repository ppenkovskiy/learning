select avg(quantity)
from order_details
group by product_id
order by avg(quantity);

select product_name, units_in_stock
from products
where units_in_stock < all (select avg(quantity)
                            from order_details
                            group by product_id)
order by units_in_stock desc;

select distinct product_name
from products
         join order_details using (product_id)
where quantity = 10;






