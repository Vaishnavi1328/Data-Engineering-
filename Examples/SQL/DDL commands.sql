create database vaishudb;

create table Employee(
id int primary key,
name varchar(25),
mail varchar(25),
gender varchar(10));

create table GenderTbl(
gender varchar(10) primary key);

alter table Employee 
add constraint FK_Gender foreign key(gender)
references GenderTbl(gender);

drop table GenderTbl;

insert into GenderTbl values('female');
insert into GenderTbl values('Male');

select * from GenderTbl;

insert into Employee values(1,'vaishu','vaishu@gmail.com','female');
insert into Employee values(2,'surya','surya20@gmail.com','male');
insert into Employee values(3,'priya','suchi12@edu.in','female');

update Employee set mail = 'priya52@gmail.com' where id=3;

select * from Employee;

drop table employee;



