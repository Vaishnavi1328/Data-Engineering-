-- ""Joins exercise""
--Calculate the total amount spent by each customer.
SELECT o.customer_id,
SUM(p.price * o.quantity) AS total_spent
FROM Orders o
JOIN Products p ON o.product_id = p.product_id
GROUP BY o.customer_id;

--Find customers who have spent more than $1,000 in total.
SELECT o.customer_id,
SUM(p.price * o.quantity) AS total_spent
FROM Orders o
JOIN Products p ON o.product_id = p.product_id
GROUP BY o.customer_id
HAVING SUM(p.price * o.quantity) > 1000;

---Find Product Categories with more Than 5 Products
SELECT category,
COUNT(product_id) AS product_count
FROM Products
GROUP BY category
HAVING COUNT(product_id) > 5;

--Calculate the total number of products for each category and supplier combination.
SELECT category,supplier,
COUNT(product_id) AS total_products
FROM Products
GROUP BY category, supplier
ORDER BY category, supplier;


--Summarize total sales by product and customer, and also provide an overall total.

-- Total Sales by Product and Customer
SELECT o.customer_id,p.product_id,p.product_name,
SUM(o.quantity * p.price) AS total_sales
FROM Orders o
JOIN Products p ON o.product_id = p.product_id
GROUP BY o.customer_id, p.product_id, p.product_name
ORDER BY o.customer_id, p.product_id;

-- Overall Total Sales
SELECT SUM(o.quantity * p.price) AS overall_total_sales
FROM Orders o
JOIN Products p ON o.product_id = p.product_id;