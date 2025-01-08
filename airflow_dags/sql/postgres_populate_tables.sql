truncate table
    Loyalty_statuses,
    Users,
    ProductCategories,
    Products,
    Order_statuses,
    Orders,
    OrderDetails
restart identity cascade;

insert into Loyalty_statuses
    (status)
values
    ('Platinum'),
    ('Gold'),
    ('Silver'),
    ('Bronze')
;

insert into Users
values
    (default, 'Andrew', 'Tate', 'alphawolf@yahoo.com', '+1(000)111-22-33', '01.01.2020', 1),
    (default, 'Bobby', 'Taffer', 'bobobob@yahoo.com', '+1(000)222-333-44', '02.02.2021', 2),
    (default, 'Candice', 'Nuts', 'full_moulth@yahoo.com', '+1(000)333-44-55', '03.03.2022', 3),
    (default, 'Donna', 'Prima', 'lovemaxim@yahoo.com', '+1(000)444-55-66', '04.04.2023', 4),
    (default, 'Evan', 'Criss', 'thebsetavanger@yahoo.com', '+1(000)555-66-77', '05.05.2024', null)
;

insert into ProductCategories
values
    (default, 'Food', null),
    (default, 'Cola', 1),
    (default, 'Resources', null),
    (default, 'Paint', 3),
    (default, 'Steel', 3)
;

insert into Products
values
    (default, 'Cheese', 'This is cheese.', 1, 12.99, 22, '01.01.1999'),
    (default, 'Coca-Cola', 'Plain cola.', 2, 2.99, 2, '01.01.1999'),
    (default, 'Dobry Pepsi', 'Fake pepis.', 2, 2.49, 122, '01.01.1999'),
    (default, 'Pink Paint', 'This is a pink paint.', 4, 12.99, 22, '01.01.1999'),
    (default, 'Steel Rod #1', 'This is cool steel rod.', 5, 112.99, 22, '01.01.1999'),
    (default, 'Steel Rod #101', 'This is event cooler steel rod.', 5, 122.99, 22, '01.01.1999')
;

insert into Order_statuses
values
    (default, 'Draft'),
    (default, 'Pending'),
    (default, 'Payed'),
    (default, 'Delivery'),
    (default, 'Complete')
;

insert into Orders
values
    (default, 1, '10.10.2020', 2, 4, '12.10.2020'),
    (default, 2, '10.10.2020', 4, 1, '12.10.2020')
;

insert into OrderDetails
values
    (default, 1, 1, 2, 22.11, 44.22),
    (default, 2, 6, 1000, 12.11, 1211.0)
;
