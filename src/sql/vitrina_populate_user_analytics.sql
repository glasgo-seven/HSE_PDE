TRUNCATE TABLE Vitrina_UserAnalytics;

-- This vitrina focuses on user-related metrics
-- such as registration trends and loyalty status distribution.
INSERT INTO Vitrina_UserAnalytics (
	user_id,
	first_name,
	last_name,
	email,
	phone,
	registration_date,
	loyalty_status,
	total_orders,
	total_spent
)
SELECT 
	Users.user_id,
	Users.first_name,
	Users.last_name,
	Users.email,
	Users.phone,
	Users.registration_date,
	Loyalty_statuses.status		AS loyalty_status,
	COUNT(Orders.order_id)		AS total_orders,
	SUM(Orders.total_amount)	AS total_spent
FROM Users
JOIN Loyalty_statuses ON Users.loyalty_status = Loyalty_statuses.status_id
LEFT JOIN Orders ON Users.user_id = Orders.user_id
GROUP BY Users.user_id;
