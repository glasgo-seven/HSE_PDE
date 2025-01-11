DROP TABLE IF EXISTS Vitrina_UserAnalytics;

-- This vitrina focuses on user-related metrics
-- such as registration trends and loyalty status distribution.
CREATE TABLE Vitrina_UserAnalytics (
	user_id				INT,
	first_name			VARCHAR(32),
	last_name			VARCHAR(32),
	email				VARCHAR(64),
	phone				VARCHAR(32),
	registration_date	TIMESTAMP,
	loyalty_status		VARCHAR(20),
	total_orders		INT,
	total_spent			DECIMAL(10, 2)
);
