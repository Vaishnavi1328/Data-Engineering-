-- ""Stored Procedure""
--Insert operation
CREATE PROCEDURE InsertProduct
    @product_id INT,
    @product_name NVARCHAR(255),
    @price DECIMAL(10, 2),
    @category NVARCHAR(255),
    @supplier NVARCHAR(255)
AS
BEGIN
    INSERT INTO Products (product_id, product_name, price, category, supplier)
    VALUES (@product_id, @product_name, @price, @category, @supplier);
END;

--update operation
CREATE PROCEDURE UpdateProduct
    @product_id INT,
    @price DECIMAL(10, 2),
    @category NVARCHAR(255)
AS
BEGIN
    UPDATE Products
    SET price = @price,
        category = @category
    WHERE product_id = @product_id;
END;

--delete operation
CREATE PROCEDURE DeleteProduct
    @product_id INT
AS
BEGIN
    DELETE FROM Products
    WHERE product_id = @product_id;
END;
