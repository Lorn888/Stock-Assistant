DROP DATABASE IF EXISTS patrykdb;

CREATE DATABASE patrykdb;

USE patrykdb;

CREATE TABLE products (
  product_id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  price FLOAT NOT NULL,
  PRIMARY KEY(product_id)
);

CREATE TABLE couriers (
  courier_id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  phone VARCHAR(255) NOT NULL,
  PRIMARY KEY(courier_id)
);

CREATE TABLE order_statuses (
  status_id INT NOT NULL AUTO_INCREMENT,
  order_status VARCHAR(255) NOT NULL,
  PRIMARY KEY(status_id)
);

CREATE TABLE orders (
  order_id INT NOT NULL AUTO_INCREMENT,
  customer_name VARCHAR(255) NOT NULL,
  customer_address VARCHAR(255) NOT NULL,
  customer_phone VARCHAR(255) NOT NULL,
  courier INT NOT NULL,
  status INT NOT NULL,
  items VARCHAR(255) NOT NULL,
  PRIMARY KEY(order_id),
  FOREIGN KEY (courier) REFERENCES couriers(courier_id),
  FOREIGN KEY (status) REFERENCES order_statuses(status_id)
);

INSERT INTO products (name, price) 
VALUES ('coke-zero', 0.6),
       ('corona', 4.0),
       ('water', 1.0),
       ('sprite', 0.6);

INSERT INTO couriers (name, phone) 
VALUES ('Tomek', '0789887889'),
       ('Mike', '0789887889'),
       ('Sudesh', '0789887889'),
       ('Hammed', '0789887889');

INSERT INTO order_statuses (order_status)
VALUES ('PREPARING'),
       ('DISPATCHED'),
       ('DELIVERED');

INSERT INTO orders (customer_name, customer_address, customer_phone, courier, status, items) 
VALUES 
('Alice', '10 High Street, Walthamstow, London', '1234567890', 1, 1, '1,2'),
('Bob', '22 Forest Road, Walthamstow, London', '2345678901', 2, 2, '3,4'),
('Charlie', '15 Hoe Street, Walthamstow, London', '3456789012', 3, 3, '1,3'),
('David', '5 Church Hill, Walthamstow, London', '4567890123', 4, 3, '2,4');


SELECT * FROM order_statuses ORDER BY status_id ASC;
SELECT * FROM products ORDER BY product_id ASC;
SELECT * FROM couriers ORDER BY courier_id ASC;
SELECT * FROM orders ORDER BY order_id ASC;
