select company_name, product_name
from suppliers
left join products on suppliers.supplier_id = products.supplier_id;

select company_name, order_id
from customers
left join orders on orders.customer_id = customers.customer_id
where order_id is null;
-- the same
select company_name, order_id
from orders
right join customers on orders.customer_id = customers.customer_id
where order_id is null;

select count(*)
from employees
left join orders on orders.employee_id = employees.employee_id
where order_id is null;

