select products.product_name, suppliers.company_name, products.units_in_stock
from products
inner join suppliers
on products.supplier_id = suppliers.supplier_id
order by units_in_stock desc;

select categories.category_name, sum(units_in_stock)
from products
inner join categories on products.category_id = categories.category_id
group by category_name
order by sum(units_in_stock) desc
limit 5;

select category_name, round(sum(unit_price * units_in_stock))
from products
inner join categories on products.category_id = categories.category_id
where discontinued <> 1
group by category_name
having sum(unit_price * units_in_stock) > 5000
order by sum(unit_price * units_in_stock) desc;

select order_id, customer_id, first_name, last_name, title
from orders
inner join employees on orders.employee_id = employees.employee_id

select order_date, product_name, ship_country, products.unit_price, quantity, discount
from orders
inner join order_details on orders.order_id = order_details.order_id
inner join products on order_details.product_id = products.product_id;

select contact_name, company_name, phone, first_name, last_name, title,
       order_date, product_name, ship_country, products.unit_price, quantity, discount
from orders
join order_details on orders.order_id = order_details.order_id
join products on order_details.product_id = products.product_id
join customers on orders.customer_id = customers.customer_id
join employees on orders.employee_id = employees.employee_id
where ship_country = 'USA';


