select contact_name, company_name, phone, first_name, last_name, title
from orders
join order_details using(order_id)
join products using(product_id)
join customers using(customer_id)
join employees using(employee_id)
where ship_country = 'USA';

-- never using natural join




