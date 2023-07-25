select company_name
from suppliers
where country in (select distinct country from customers);

select distinct suppliers.company_name
from suppliers
         join customers using (country);

select category_name, sum(units_in_stock)
from products
         join categories using (category_id)
group by category_name
order by sum(units_in_stock) desc
limit (select min(product_id) + 4 from products);

select avg(units_in_stock)
from products;

select product_name, units_in_stock
from products
where units_in_stock > (select avg(units_in_stock)
                        from products)
order by units_in_stock;

