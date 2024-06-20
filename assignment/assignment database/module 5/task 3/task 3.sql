use task1;

create table employee 
(
	e_id int primary key,
    first_name varchar(20),
    last_name varchar(20),
    salary int,
    joining_date date,
    department varchar(20)
);

insert into employee values 
(1, 'john', 'abraham', 1000000, '2013-01-01', 'banking'),
(2, 'mitchel', 'clarke', 800000, '2013-01-01', 'insurance'),
(3, 'roy', 'thimas', 700000, '2013-02-01', 'banking'),
(4, 'tom', 'jose', 600000, '2013-02-01', 'insurance'),
(5, 'jerry', 'pinto', 650000, '2013-02-01', 'insurance'),
(6, 'philip', 'mathew', 750000, '2013-01-01', 'services'), 
(7, 'testname1', '123', 650000, '2013-01-01', 'services'),
(8, 'testname2', 'lname%', 600000, '2013-02-01', 'insurance');


create table incentive
(
	e_ref_id int,
    incentive_date date,
    incentive_amount int
);

insert into incentive values
(1,'2013-02-01', 5000),
(2, '2013-02-01', 3000),
(3, '2013-02-01', 4000),
(1, '2013-01-01', 4500),
(2, '2013-01-01', 3500);




select * from employee
where first_name = "tom";

select first_name, joining_date, salary 
from employee;

select * from employee
order by first_name asc;

select * from employee
order by salary desc;

select * from employee
where first_name like 'j%';

select * , max(salary)from employee
group by department
order by salary asc;

SELECT e.first_name, i.incentive_amount 
FROM employee e 
JOIN incentive i ON e.e_id = i.e_ref_id 
WHERE i.incentive_amount > 3000;


