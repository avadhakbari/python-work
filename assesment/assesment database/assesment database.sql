create database assissment;
use assissment;

create table nobel_win
(
	year int,
    subject varchar(50),
    winner varchar(100),
    country varchar(50),
    category varchar(50)
);

insert into nobel_win values
(1970, "physics", "hannes alfven", "sweden", "scientist"),
(1970, "physics", "louis neel", "france", "scientist"), 
(1970, "chemistry", "luis federico leloir", "france", "scientist"),
(1970, "phisiology", "ulf von euler", "sweden", "scientist"),
(1970, "phisiology", "bernard katz", "germany", "scientist"),
(1970, "literature", "aleksandr solzhenitsny", "russia", "linguist"),
(1970, "economics", "paul samuelson", "usa", "econimist"),
(1970, "phisiology", "julius axelrod", "usa", "scientist"),
(1971, "physics", "dennis gabor", "hungary", "scientist"),
(1971, "chemistry", "gerhard herzberg", "germany", "scientist"),
(1971, "peace", "willy brandt", "germany", "chanecllor"),
(1971, "literature", "pablo neruda", "chile", "linguisgt"),
(1971, "economics", "simon kuznets", "russia", "economist"),
(1978, "peace", "anwar al- sadat", "egypt", "president"),
(1978, "peace", "menachem begin", "isreal", "prime minister"),
(1978, "chemistry", "donald j. cram", "usa", "scientist"),
(1978, "chemistry", "jean- marie lehn", "france", "scientist"),
(1978, "physiology", "susumu tonegawa", "japan", "scientist"),
(1994, "economics", "reinhard selten", "germany", "economist"),
(1994, "peace", "yitzhak rabin", "israel", "prime minister"),
(1987, "physics", "johannes georg bednorz", "germany", "scientist"),
(1978, "literatire", "joseph brodsky", "russia", "linguist"),
(1978, "economics", "robert solow", "usa", "economist"),
(1994, "leterature", "kenzaburo oe", "japan", "linguist");

select * from nobel_win;


select year, subject, winner from nobel_win
where year = 1970;

select year, subject, winner, country from nobel_win
where subject = "chemistry" and year>= 1965 and year<=1975;

select year, subject, winner, country from nobel_win
where winner like "louis%";

select * from nobel_win
where winner not like "p%"
order by year desc;

select year, subject, winner,category from nobel_win
where year = 1970 and (subject = "chemistry" or subject = "economics")
order by subject asc;
