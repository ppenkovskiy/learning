select * from orders
where freight >= 20 and freight <= 40;
-- the same with between including boundaries
select count(*)
from orders
where freight between 20 and 40;

select * from orders
where order_date BETWEEN '1998-03-30' and '1998-04-03'

