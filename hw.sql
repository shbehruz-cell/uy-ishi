CREATE DATABASE pc;
USE pc
CREATE TABLE computer()

CREATE TABLE computers (id INT,brand VARCHAR(50),model VARCHAR(100),cpu VARCHAR(100),frequency FLOAT,ram INT,os VARCHAR(50),price INT);

INSERT INTO computers VALUES
(1,'Apple', 'MacBook Pro 16', 'Intel Core i7', 2.6, 16, 'macOS', 2500),
(2,'Apple', 'MacBook Air M1', 'M1', 3.2, 8, 'macOS', 1800),
(3,'Apple', 'iMac 27', 'M1', 3.2, 8, 'macOS', 2800),
(4,'ASUS', 'ZenBook 13', 'Intel Core i7', 2.8, 8, 'Windows 10', 1200),
(5,'ASUS', 'VivoBook 15', 'AMD Ryzen 5', 3.5, 4, 'Windows 10', 600),
(6,'ASUS', 'ROG Gaming', 'Intel Core i7', 3.1, 16, 'Windows 10', 2200),
(7,'Dell', 'XPS 13', 'Intel Core i5', 2.4, 8, 'Windows 10', 1000),
(8,'Dell', 'Inspiron 15', 'AMD Ryzen 5', 3.6, 8, 'Windows 10', 700),
(9,'Dell', 'Precision 5550', 'Intel Core i7', 2.9, 32, 'Windows 10', 3500),
(10,'Lenovo', 'ThinkPad X1', 'Intel Core i7', 2.9, 16, 'Ubuntu 20.04', 1500),
(11,'Lenovo', 'IdeaPad 5', 'AMD Ryzen 7', 3.8, 8, 'Windows 10', 900),
(12,'Lenovo', 'Legion 5', 'AMD Ryzen 7', 3.9, 16, 'Windows 10', 1800),
(13,'HP', 'Pavilion 15', 'AMD Ryzen 7', 3.8, 16, 'Windows 10', 2000),
(14,'HP', 'Envy x360', 'Intel Core i5', 2.5, 8, 'Windows 10', 950),
(15,'HP', 'ZBook Fury', 'Intel Core i7', 3.0, 32, 'Windows 10', 3000),
(16,'MSI', 'Modern 14', 'Intel Core i5', 2.4, 8, 'Windows 10', 850),
(17,'MSI', 'GE76 Raider', 'Intel Core i7', 3.1, 16, 'Windows 10', 2400),
(18,'Acer', 'Swift 3', 'AMD Ryzen 5', 3.5, 8, 'Windows 10', 700),
(19,'Acer', 'Nitro 5', 'AMD Ryzen 7', 3.8, 16, 'Windows 10', 1600),
(19,'Sony', 'VAIO', 'Intel Core i5', 2.5, 8, 'Windows 10', 1100),
(20,'Sony', 'VAIO Pro', 'Intel Core i7', 2.7, 16, 'Windows 10', 2100);




--1-masala
SELECT * FROM computers ORDER BY price DESC LIMIT 1;

  ------------------------------------

--2-masala
SELECT * FROM computers ORDER BY price LIMIT 1;


-----------------------------------

--3-masala
SELECT frequency FROM computers WHERE price BETWEEN 400 AND 1000 AND cpu LIKE '%Intel%';


-------------------------------------------------------

--4-masala
SELECT model FROM computers WHERE brand = 'Apple';


------------------------------------------------

--5-masala

--bunisiga chalkashib qoldim