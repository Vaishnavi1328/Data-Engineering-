CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    PhoneNumber VARCHAR(15)
);
INSERT INTO Customers (CustomerID, FirstName, LastName, Email, PhoneNumber) VALUES
(1, 'priya', 'Sharma', 'amit.sharma@example.com', '9876543210'),
(2, 'rohit', 'mehta', 'priya.mehta@example.com', '8765432109'),
(3, 'neha', 'kumar', 'rohit.kumar@example.com', '7654321098'),
(4, 'siddharth', 'verma', 'neha.verma@example.com', '6543210987'),
(5, 'asha', 'Singh', 'siddharth.singh@example.com', '5432109876'),
(6, 'atha', 'rao', 'atha.rao@example.com', '4321098765');

--lefttrim,righttrim,lowercase
UPDATE Customers 
SET FirstName = LTRIM(RTRIM(LOWER(FirstName))),
	LastName = LTRIM(RTRIM(LOWER(LastName)));

--pattern matching
SELECT * 
FROM Customers
WHERE FirstName LIKE 'A%';

SELECT *
FROM Customers
WHERE PhoneNumber LIKE '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]';

SELECT *
FROM Customers
WHERE LastName LIKE '___';--LastName with 3 characters


CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderAmount DECIMAL(10, 2),
    OrderDate DATE
);
 
INSERT INTO Orders (OrderID, CustomerID, OrderAmount, OrderDate)
VALUES 
(1, 1, 500.00, '2024-01-15'),
(2, 2, 700.00, '2024-01-16'),
(3, 1, 300.00, '2024-01-17'),
(4, 3, 1200.00, '2024-02-01'),
(5, 2, 900.00, '2024-02-03');

SELECT DISTINCT o1.CustomerID
FROM Orders o1
WHERE(
	SELECT COUNT(*)
	FROM Orders o2
	WHERE o2.CustomerID = o1.CustomerID
) >1;