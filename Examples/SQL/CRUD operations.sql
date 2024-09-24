--create
create table Employees(
EmployeeId int primary key,
FirstName varchar(50),
LastName varchar(50),
Position varchar(50),
Department varchar(50),
HireDate date);

--insert
INSERT INTO Employees (EmployeeId, FirstName, LastName, Position, Department, HireDate)
VALUES 
(1, 'Priya', 'Bose', 'Data Engineer', 'Development', '2024-10-24'),
(2, 'John', 'Doe', 'Software Engineer', 'Development', '2024-08-01'),
(3, 'Jane', 'Smith', 'Product Manager', 'Product', '2024-07-15'),
(4, 'Alice', 'Johnson', 'UX Designer', 'Design', '2024-09-10'),
(5, 'Bob', 'Brown', 'QA Analyst', 'Quality Assurance', '2024-06-20');

--read
select * from Employees;

--update
update Employees set HireDate = '2024-09-22' where EmployeeId=1;

--delete
delete from Employees where EmployeeId = 3;


