DROP TABLE IF EXISTS
	Loyalty_statuses,
	Users,
	ProductCategories,
	Products,
	Order_statuses,
	Orders,
	OrderDetails
;

CREATE TABLE Loyalty_statuses (
	status_id	INT AUTO_INCREMENT PRIMARY KEY,
	status		VARCHAR(20)
);
CREATE TABLE Users (
	user_id				INT AUTO_INCREMENT PRIMARY KEY,
	first_name			VARCHAR(32),
	last_name			VARCHAR(32),
	email				VARCHAR(64),
	phone				VARCHAR(32),
	registration_date	TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	loyalty_status		INT
);

CREATE TABLE ProductCategories (
	category_id			INT AUTO_INCREMENT PRIMARY KEY,
	name				VARCHAR(32),
	parent_category_id	INT
);
CREATE TABLE Products (
	product_id		INT AUTO_INCREMENT PRIMARY KEY,
	name			VARCHAR(32),
	description		VARCHAR(256),
	category_id		INT,
	price			DECIMAL(10, 2),
	stock_quantity	INT,
	creation_date	TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Order_statuses (
	status_id		INT AUTO_INCREMENT PRIMARY KEY,
	status			VARCHAR(32)
);
CREATE TABLE Orders (
	order_id		INT AUTO_INCREMENT PRIMARY KEY,
	user_id			INT,
	order_date		TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	total_amount	DECIMAL(10, 2),
	status			INT,
	delivery_date	TIMESTAMP
);

CREATE TABLE OrderDetails (
	order_detail_id	INT AUTO_INCREMENT PRIMARY KEY,
	order_id		INT,
	product_id		INT,
	quantity		INT,
	price_per_unit	DECIMAL(10, 2),
	total_price		DECIMAL(10, 2)
);