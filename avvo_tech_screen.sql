create table dim_salesperson
(
  id integer not null,
  name varchar(20),
  age smallint,
  salary integer
);

create table dim_customer
(
  id integer not null,
  name varchar(20),
  city varchar(20),
  industry_type char(1)
);

create table orders
(
  number integer not null,
  order_date date not null,
  cust_id integer not null,
  salesperson_id integer not null,
  amount integer
);

insert into dim_salesperson(id, name, age, salary)
  values(1, 'Abe', 61, 140000),
        (2, 'Bob', 34, 44000),
        (5, 'Chris', 34, 40000),
        (7, 'Dan', 41, 52000),
        (8, 'Ken', 57, 115000),
        (11, 'Joe', 38, 38000)
   ;
insert into dim_customer(id, name, city, industry_type)
  values(4, 'Samsonic', 'pleasant', 'J'),
        (6, 'Panasung', 'oaktown', 'J'),
        (7, 'Samony', 'jackson', 'B'),
        (9, 'Orange', 'jackson', 'B')
   ;
insert into orders(number, order_date, cust_id, Salesperson_id, amount)
  values(10, to_date('08/02/1996', 'mm/dd/yyyy'), 4, 2, 2400),
        (20, to_date('01/30/1999', 'mm/dd/yyyy'), 4, 8, 1800),
        (30, to_date('07/14/1995', 'mm/dd/yyyy'), 9, 1, 460),
        (40, to_date('01/29/1998', 'mm/dd/yyyy'), 7, 2, 540),
        (50, to_date('02/03/1998', 'mm/dd/yyyy'), 6, 7, 600),
        (60, to_date('03/02/1998', 'mm/dd/yyyy'), 6, 7, 720),
        (70, to_date('05/06/1998', 'mm/dd/yyyy'), 9, 7, 150)
   ;