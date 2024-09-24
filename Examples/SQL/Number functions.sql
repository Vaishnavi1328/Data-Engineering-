use companydb;
CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    price int
);
INSERT INTO Products (product_id, product_name, price) VALUES
(1, 'Laptop', 800.00),
(2, 'Smartphone', 500.00),
(3, 'Tablet', 300.00),
(4, 'Headphones', 50.00),
(5, 'Monitor', 150.00);
CREATE TABLE Orders (
    order_id INT,
    product_id INT,
    quantity INT,
    order_date DATE
);
INSERT INTO Orders (order_id, product_id, quantity, order_date) VALUES
(1, 1, 2, '2024-08-01'),
(2, 2, 1, '2024-08-02'),
(3, 3, 1, '2024-08-03'),
(4, 1, 4, '2024-08-04'),
(5, 4, 2, '2024-08-05'),
(6, 5, 2, '2024-08-06'),
(7, 6, 1, '2024-08-07');

select product_name,price,price%5 as modulo_price from Products;

select abs(min(price)-max(price)) as differnce from Products;

select product_name,price,round(rand()*100,2) from Products;

--15%dicount on price and show in ceiling and floor

select product_name,price,round(price*0.85,2) as DiscountedPrice,ceiling(price*0.85),floor(price*0.85) from Products;