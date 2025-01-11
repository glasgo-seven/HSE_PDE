TRUNCATE TABLE Vitrina_ProductPerfomance;

-- This vitrina focuses on  product sales performance,
-- including total sales, average price, and stock levels.
INSERT INTO Vitrina_ProductPerfomance (
	product_id,
	product_name,
	category_name,
	total_sold_quantity,
	total_revenue,
	average_price,
	current_stock
)
SELECT 
	Products.product_id,
	Products.name						AS product_name,
	ProductCategories.name				AS category_name,
	SUM(OrderDetails.quantity)			AS total_sold_quantity,
	SUM(OrderDetails.total_price)		AS total_revenue,
	AVG(OrderDetails.price_per_unit)	AS average_price,
	Products.stock_quantity				AS current_stock
FROM Products
JOIN ProductCategories ON Products.category_id = ProductCategories.category_id
JOIN OrderDetails ON Products.product_id = OrderDetails.product_id
GROUP BY Products.product_id;
