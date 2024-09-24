-- Create the table
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Position VARCHAR(50),
    Department VARCHAR(50),
    HireDate DATE
);

drop table Employees;

-- Insert values into the table
INSERT INTO Employees (EmployeeID, FirstName, LastName, Position, Department, HireDate) VALUES
(2, 'Amit', 'Sharma', 'Software Engineer', 'IT', '2022-01-15'),
(3, 'Priya', 'Mehta', 'Project Manager', 'Operations', '2023-04-20'),
(4, 'Raj', 'Patel', 'Business Analyst', 'Finance', '2021-06-30'),
(5, 'Sunita', 'Verma', 'HR Specialist', 'HR', '2019-08-12'),
(6, 'Vikram', 'Nair', 'Software Engineer', 'IT', '2021-03-18'),
(7, 'Anjali', 'Desai', 'HR Manager', 'HR', '2020-05-14'),
(8, 'Rohan', 'Kumar', 'Finance Manager', 'Finance', '2022-11-25'),
(9, 'Deepak', 'Singh', 'Operations Coordinator', 'Operations', '2023-07-02'),
(10, 'Neha', 'Gupta', 'Data Scientist', 'Finance', '2022-08-05');

--1
select * from Employees where Department = 'IT';

--2
select * from Employees where HireDate> '2022-01-01';

--3
select * from Employees where Department IN ('IT','Finance');

--4
select * from Employees where Position = 'Software Engineer' and HireDate>'2021-01-01';

--5
select * from Employees where LastName like 's%';

--6
select * from Employees where FirstName like '%n%';

--7
select count(*) from Employees;

--8
select min(HireDate) from Employees;
