CREATE TABLE genre (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE author (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE book(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    price INT,
    amount INT,
    a_id INT,
    g_id INT,
    FOREIGN KEY (a_id) REFERENCES author(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (g_id) REFERENCES genre(id) ON DELETE CASCADE ON UPDATE CASCADE
);


INSERT INTO genre VALUES(1, "ertak"), (2, "tarixiy"), (3, "badiiy"), (4, "detektiv");

INSERT INTO author VALUES
    (1, "Xudoyberdi To'xtaboyev"), 
    (2, "Adolfe Hitler"), 
    (3, "Alisher Navoiy"), 
    (4, "Ahad Qayum");

INSERT INTO book(name, price, amount, a_id, g_id)
    VALUES
    ("Shaytanat", 100000, 4, 2, 3),
    ("Ikki eshik orasi", 150000, 2, 2, 2),
    ("Devona", 70000, 4, 4, 3),
    ("Do'st ortirish", 60000, 10, 1, 1),
    ("Jannatiy odamlar", 150000, 2, 3, 4),
    ("Binafsha shulasi", 150000, 29, 1, 2),
    ("Al - kimyogar", 150000, 14, 3, 1),
    ("Buzrukning kuzi", 150000, 5, 3, 3),
    ("Mehrobdan chayon", 150000, 2, 2, 4),
    ("Dunyoning ishlari", 150000, 90, 4, 2);




    ----------------------------------
    --1-masala
SELECT g.name AS janr FROM genre g JOIN book b ON b.g_id = g.id JOIN author a ON a.id = b.a_id WHERE a.name = 'Alisher Navoiy';

--2-masala
SELECT a.name AS muallif, g.name AS janr FROM author a JOIN book b ON b.a_id = a.id JOIN genre g ON g.id = b.g_id;

--3-masala

--Buni qilolmadm chalkashib qoldim sababi janrlari boyicha nechtadan kitob yozgan deganiga

--4-masala
SELECT g.name AS janr, COUNT(*) AS kitob_soni FROM genre g JOIN book b ON b.g_id = g.id GROUP BY g.name ORDER BY kitob_soni DESC LIMIT 1;

--5-masala

-- bu ga ham chalkashib qoldim

--6-masala
SELECT a.name AS muallif, SUM(b.amount) AS sotilgan FROM author a JOIN book b ON b.a_id = a.id GROUP BY a.name ORDER BY sotilgan DESC LIMIT 1;