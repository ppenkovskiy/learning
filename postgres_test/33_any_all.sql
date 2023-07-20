select distinct company_name
from customers
join orders using (customer_id)
join order_details using (order_id)
where quantity > 40;

select customer_id
from orders
join order_details using (order_id)
where quantity > 40;

select distinct company_name
from customers
where customer_id in (select customer_id
                      from orders
                      join order_details using (order_id)
                      where quantity > 40);

select distinct company_name
from customers
where customer_id = any(select customer_id
                      from orders
                      join order_details using (order_id)
                      where quantity > 40);

select avg(quantity)
from order_details;

select distinct product_name, quantity
from products
join order_details using(product_id)
where quantity > (select avg(quantity)
                  from order_details)
order by quantity;

select avg(quantity)
from order_details
group by product_id
order by avg(quantity);

select distinct product_name, quantity
from products
join order_details using(product_id)
where quantity > all(select avg(quantity)
                     from order_details
                     group by product_id)
order by quantity;




