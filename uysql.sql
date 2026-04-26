--1-masala

SELECT category , sum(quantity) FROM sales GROUP BY category;



-------------------------------------------------------
--2-masala

SELECT category, SUM(price * quantity) FROM sales GROUP BY category;

-----------------------------------------
--3-masala
SELECT category , AVG(price)  FROM sales GROUP BY category;

-------------------------------------
--4-masala

SELECT sale_date, SUM(price * quantity)FROM sales GROUP BY sale_date;

---------------------------------------------
--5-masala

SELECT SUM(price * quantity) FROM sales WHERE category = 'Electronics';

--6-masala

SELECT category, SUM(price * quantity) FROM sales GROUP BY category HAVING SUM(price * quantity) > 2000;

--7-masala

SELECT category, AVG(price) FROM sales GROUP BY category HAVING AVG(price) > 100;

--8-masala

SELECT SUM(quantity) FROM sales WHERE sale_date = '2025-01-01';

--9-masala

SELECT category, SUM(quantity) FROM sales GROUP BY category ORDER BY SUM(quantity) DESC LIMIT 1;

--10-masala
-- 10. 3 martadan ko‘p sotilgan (quantity > 3) mahsulotlar bo‘yicha kategoriyalar kesimida jami tushumni chiqaring. KESIMIDA DEGANIGA TUSHINMADIM