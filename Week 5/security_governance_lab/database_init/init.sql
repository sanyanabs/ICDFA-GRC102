USE customer_data;

CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    ssn VARCHAR(11),
    dob DATE,
    address VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(2),
    zip VARCHAR(10),
    email VARCHAR(100),
    phone VARCHAR(20),
    credit_card VARCHAR(19)
);

INSERT INTO customers
    (first_name, last_name, ssn, dob, address, city, state, zip, email, phone, credit_card)
VALUES
    ('Test', 'User01', '000-00-0001', '1990-01-01',
     'LAB-ADDRESS-01', 'LAB-CITY', 'XX', '00000',
     'test.user01@lab.invalid', '0000000001', '0000000000000001'),

    ('Test', 'User02', '000-00-0002', '1991-02-02',
     'LAB-ADDRESS-02', 'LAB-CITY', 'XX', '00000',
     'test.user02@lab.invalid', '0000000002', '0000000000000002'),

    ('Test', 'User03', '000-00-0003', '1992-03-03',
     'LAB-ADDRESS-03', 'LAB-CITY', 'XX', '00000',
     'test.user03@lab.invalid', '0000000003', '0000000000000003');
