select *
from customers
where country = 'Mexico' or country = 'Germany' or country = 'USA';

select * from customers
where country in ('Mexico', 'Germany', 'USA');

select * from customers
where country not in ('Mexico', 'Germany', 'USA')

