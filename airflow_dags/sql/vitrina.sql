DROP TABLE IF EXISTS Vitrina;

CREATE TABLE Vitrina AS
SELECT
    Users.user_id,
    CONCAT(Users.first_name, ' ', Users.last_name) AS full_name,
    Users.email,
    Users.phone,
    Users.loyalty_status,
    Orders.order_id,
    Orders.order_date,
    Orders.total_amount AS order_total,
    Products.product_id,
    Products.name AS product_name,
    ProductCategories.name AS category_name,
    OrderDetails.quantity,
    OrderDetails.price_per_unit,
    OrderDetails.quantity * OrderDetails.price_per_unit AS total_price_per_product,
    Orders.status AS order_status
FROM
    Orders
JOIN
    Users ON Orders.user_id = Users.user_id
JOIN
    OrderDetails ON Orders.order_id = OrderDetails.order_id
JOIN
    Products ON OrderDetails.product_id = Products.product_id
JOIN
    ProductCategories ON Products.category_id = ProductCategories.category_id;
