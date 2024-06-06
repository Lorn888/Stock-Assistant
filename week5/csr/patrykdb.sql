DROP DATABASE IF EXISTS patrykdb;

CREATE DATABASE patrykdb;

USE patrykdb;

CREATE TABLE products (
  product_id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  price VARCHAR(255) NOT NULL,
  PRIMARY KEY(product_id)
);

CREATE TABLE couriers (
  courier_id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  phone VARCHAR(255) NOT NULL,
  PRIMARY KEY(courier_id)
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

-- Select all records from the products table
SELECT * FROM products ORDER BY product_id ASC;

-- Select all records from the couriers table
SELECT * FROM couriers ORDER BY courier_id ASC;
