DROP TABLE IF EXISTS Vitrina_ProductPerfomance;

-- This vitrina focuses on  product sales performance,
-- including total sales, average price, and stock levels.
CREATE TABLE Vitrina_ProductPerfomance (
	product_id			INT,
	product_name		VARCHAR(32),
	category_name		VARCHAR(32),
	total_sold_quantity	INT,
	total_revenue		DECIMAL(10, 2),
	average_price		DECIMAL(10, 2),
	current_stock		INT
);
