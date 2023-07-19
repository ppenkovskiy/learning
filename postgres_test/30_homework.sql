select c.company_name, CONCAT(e.first_name, ' ', e.last_name)
from orders as o
join customers as c using(customer_id)
join employees as e using(employee_id)
join shippers as s on o.ship_via = s.shipper_id
where c.city = 'London' and e.city = 'London' and s.company_name = 'Speedy Express';

select product_name, units_in_stock, contact_name, phone
from products
join categories using(category_id)
join suppliers using(supplier_id)
where category_name in ('Beverages', 'Seafood') and units_in_stock < 20
order by units_in_stock

select company_name, order_id
from customers
left join orders using(customer_id)
where order_id is null
order by contact_name;

select company_name, order_id
from orders
right join customers c on orders.customer_id = c.customer_id
where order_id is null;

