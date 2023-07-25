SELECT * FROM customers;

SELECT contact_name, city
FROM customers;

SELECT order_id, shipped_date - order_date
FROM orders;

SELECT DISTINCT city FROM customers;

SELECT count(customer_id) FROM customers;
-- or
SELECT count(*) FROM customers;

SELECT count(DISTINCT country) FROM customers