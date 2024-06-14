DROP DATABASE IF EXISTS patrykdb;

CREATE DATABASE patrykdb;

USE patrykdb;

-- Table to store product information
CREATE TABLE products (
  product_id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  price FLOAT NOT NULL,
  quantity INT NOT NULL,
  PRIMARY KEY(product_id)
);

-- Table to store courier information
CREATE TABLE couriers (
  courier_id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  phone VARCHAR(255) NOT NULL,
  PRIMARY KEY(courier_id)
);

-- Table to store possible order statuses
CREATE TABLE order_statuses (
  status_id INT NOT NULL AUTO_INCREMENT,
  order_status VARCHAR(255) NOT NULL,
  PRIMARY KEY(status_id)
);

-- Table to store customer information
CREATE TABLE customer_details (
  customer_id INT NOT NULL AUTO_INCREMENT,
  customer_name VARCHAR(255) NOT NULL,
  customer_address VARCHAR(255) NOT NULL,
  customer_phone VARCHAR(255) NOT NULL,
  PRIMARY KEY(customer_id)
);

-- Table to store order information
CREATE TABLE orders (
  order_id INT NOT NULL AUTO_INCREMENT,
  customer_id INT NOT NULL,
  courier INT NOT NULL,  
  status INT NOT NULL,  
  PRIMARY KEY(order_id),
  FOREIGN KEY (customer_id) REFERENCES customer_details(customer_id),
  FOREIGN KEY (courier) REFERENCES couriers(courier_id), 
  FOREIGN KEY (status) REFERENCES order_statuses(status_id) 

-- Table to store ordered items
CREATE TABLE items (  
  order_item_id INT NOT NULL AUTO_INCREMENT,
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  PRIMARY KEY(order_item_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert sample data into products table
INSERT INTO products (name, price, quantity) 
VALUES 
('coke-zero', 0.6, 100),
('corona', 4.0, 50),
('water', 1.0, 200),
('sprite', 0.6, 150);

-- Insert sample data into couriers table
INSERT INTO couriers (name, phone) 
VALUES 
('Tomek', '0789887889'),
('Mike', '0789887889'),
('Sudesh', '0789887889'),
('Hammed', '0789887889');

-- Insert sample data into order_statuses table
INSERT INTO order_statuses (order_status)
VALUES 
('PREPARING'),
('DISPATCHED'),
('DELIVERED');

-- Insert sample data into customer_details table
INSERT INTO customer_details (customer_name, customer_address, customer_phone) 
VALUES 
('Alice', '10 High Street, Walthamstow, London', '1234567890'),
('Bob', '22 Forest Road, Walthamstow, London', '2345678901'),
('Charlie', '15 Hoe Street, Walthamstow, London', '3456789012'),
('David', '5 Church Hill, Walthamstow, London', '4567890123');

-- Insert sample data into orders table
INSERT INTO orders (customer_id, courier, status)  
VALUES 
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 3);

-- Insert sample data into items table  -- Updated to match new table name
INSERT INTO items (order_id, product_id, quantity)
VALUES
(1, 1, 2),
(1, 2, 1),
(2, 3, 4),
(2, 4, 3),
(3, 1, 1),
(3, 3, 2),
(4, 2, 1),
(4, 4, 2);

SELECT * FROM order_statuses ORDER BY status_id ASC;
SELECT * FROM products ORDER BY product_id ASC;
SELECT * FROM couriers ORDER BY courier_id ASC;
SELECT * FROM customer_details ORDER BY customer_id ASC;
SELECT * FROM orders ORDER BY order_id ASC;
SELECT * FROM items ORDER BY order_item_id ASC;
