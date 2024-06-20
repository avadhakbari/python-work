use task1;

create table person
(
	first_name varchar(20),
    last_name varchar(20),
    address varchar(20),
    city varchar(20),
    age int
);

insert into person values
('Micky','Mouse','123 Fantasty way', 'anaheim',73),
('Bat','Man','321 cavern ave', 'gotham', 54),
('Wonder', 'Woman', '987 truth way', 'paradies', 39),
('Donald', 'Duck', '555 quack street', 'mallard', 65),
('Bugs', 'Bunny', '567 carrot strret', 'rascal', 58),
('Wiley', 'Coyote', '999 acame way', 'canyon', 61),
('Cat', 'Woman', '234 purffect street', 'hairball', 32),
('Tweety', 'Bird', '543', 'itotltaw', 28);

select * from person;