use task1;

create table salseperson
(
	sno int primary key,
    sname varchar(20),
    city varchar(20),
    comm float
);

insert into salseperson values
(1001, 'peel', 'london', 0.12),
(1002, 'serres', 'san jose', 0.13),
(1004, 'motika', 'london', 0.11),
(1007, 'rafkin', 'barcelona', 0.15),
(1003, 'axelrod', 'new york', 0.1);

create table customer 
(
	cnm int primary key,
    cname varchar(20),
    city varchar(20),
    ratting int,
    sno int,
    foreign key (sno) references  salseperson(sno)
);

insert into customer values
(201, 'hoffman', 'london', 100, 1001),
(202, 'giovanne', 'roe', 200, 1003),
(203, 'liu', 'san jose', 300, 1002),
(204, 'grass', 	'barcelona', 100, 1002),
(206, 'clemens', 'london', 300, 1007),
(207, 'pereira', 'roe', 100, 1004);


select * from salseperson;

select * from customer;


SELECT s.sno, s.sname, SUM(c.ratting) AS total_order_amount
FROM salseperson s
JOIN customer c ON s.sno = c.sno
GROUP BY s.sno, s.sname
HAVING SUM(c.ratting) > 1000;

select sname,city
from salseperson
where city = 'london' and comm >= 0.12;

select * from salseperson
where city in ('barcelona', 'london');

select * from salseperson
where comm between 0.10 and 0.12;

select *
from customer
where ratting <= 100 OR city = 'roe';





