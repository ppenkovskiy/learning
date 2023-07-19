create table employee (
    employee_id int primary key,
    first_name varchar (255) not null,
    last_name varchar (255) not null,
    manager_id int,
    foreign key (manager_id) references employee (employee_id)
);

insert into employee (employee_id, first_name, last_name, manager_id)
values (1, 'fn_1', 'ln_1', null),
        (2, 'fn_2', 'ln_2', 1),
        (3, 'fn_1', 'ln_1', 1),
        (4, 'fn_1', 'ln_1', 2),
        (5, 'fn_1', 'ln_1', 2),
        (6, 'fn_1', 'ln_1', 3),
        (7, 'fn_1', 'ln_1', 3),
        (8, 'fn_1', 'ln_1', 3)

select e.first_name || ' ' || e.last_name as employee, -- || - union operator
       m.first_name || ' ' || e.last_name as manager
from employee e
left join employee m on m.employee_id = e.manager_id
order by manager;

drop table employee

