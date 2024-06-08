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

CREATE TABLE orders (
  order_id INT NOT NULL AUTO_INCREMENT,
  customer_name VARCHAR(255) NOT NULL,
  customer_phone VARCHAR(255) NOT NULL,
  courier VARCHAR(255) NOT NULL,
  status VARCHAR(255) NOT NULL,
  items VARCHAR(255) NOT NULL,
  PRIMARY KEY(order_id)
);

-- Insert data into the products table
INSERT INTO products (name, price) 
VALUES ('coke-zero', '0.6'),
       ('corona', '4.0'),
       ('water', '1.0'),
       ('sprite', '0.6');

-- Insert data into the couriers table
INSERT INTO couriers (name, phone) 
VALUES ('Tomek', '0789887889'),
       ('Mike', '0789887889'),
       ('Sudesh', '0789887889'),
       ('Hammed', '0789887889');

-- Insert data into the orders table
INSERT INTO orders (customer_name, customer_phone, courier, status, items) 
VALUES  ('John', '1234567890', 'Tomek', 'PENDING', 'coke-zero,corona'),
        ('Jane', '2345678901', 'Mike', 'PREPARING', 'water,sprite'),
        ('Mike', '3456789012', 'Sudesh', 'DISPATCHED', 'coke-zero,water'),
        ('Emily', '4567890123', 'Hammed', 'DELIVERED', 'corona,sprite');


-- Select all records from the products table
SELECT * FROM products ORDER BY product_id ASC;

-- Select all records from the couriers table
SELECT * FROM couriers ORDER BY courier_id ASC;

SELECT * FROM orders ORDER BY order_id ASC;