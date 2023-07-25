select country
from customers
union -- with deleting duplicates
select country
from employees;

select country
from customers
union all -- without deleting duplicates
select country
from employees;

select country
from customers
intersect
select country
from suppliers;

select country
from customers
except
select country
from suppliers;

select country
from customers
except all
select country
from suppliers;

select count(country)
from customers
where country = 'USA';

select count(country)
from suppliers
where country = 'USA';



