DROP DATABASE IF EXISTS patrykdb;

CREATE DATABASE patrykdb;

USE patrykdb;

CREATE TABLE `order` (
  order_id INT NOT NULL AUTO_INCREMENT,
  customer_name VARCHAR(255) NOT NULL,
  customer_address VARCHAR(255) NOT NULL,
  customer_phone VARCHAR(255) NOT NULL,  -- Added customer_phone column
  courier VARCHAR(255) NOT NULL,
  `status` VARCHAR(255) NOT NULL,
  items VARCHAR(255),  
  PRIMARY KEY(order_id)
);

INSERT INTO `order` (customer_name, customer_address, customer_phone, courier, `status`, items) 
VALUES 
('John', 'Unit 2, 12 Main Street, LONDON, WH1 2ER', '0789887334', '2', 'PREPARING', '1,3,4'),
('Jane', 'Flat 5, 34 Market Road, LONDON, NW3 6GH', '0798765432', '1', 'DISPATCHED', '2,5'),
('Mike', 'House 9, 78 High Street, MANCHESTER, MN4 5KL', '0712345678', '3', 'DELIVERED', '3'),
('Emily', 'Apt 4, 56 Broadway, LEEDS, LD2 7YU', '0734567890', '2', 'PENDING', '2,4,6');

SELECT * FROM `order` ORDER BY order_id ASC;
