import pymysql


class SchoolDB:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='1234',
        )
        self.c = self.connection.cursor()
        self.c.execute("CREATE DATABASE IF NOT EXISTS School")
        self.c.execute("USE School")
        self.connection.commit()

    def create_tables(self):
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS teachers (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50),
                surname VARCHAR(50),
                salary INT,
                experience INT,
                branch VARCHAR(50)
            )
        """)
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50),
                surname VARCHAR(50),
                monthly_payment INT,
                course_duration INT,
                branch VARCHAR(50)
            )
        """)
        self.connection.commit()

    def insert_teachers(self):
        self.c.execute("SELECT COUNT(*) as cnt FROM teachers")
        if self.c.fetchone()['cnt'] == 0:
            self.c.execute("INSERT INTO teachers (name, surname, salary, experience, branch) VALUES ('Ali', 'Karimov', 5000000, 10, 'Yunusobod')")
            self.c.execute("INSERT INTO teachers (name, surname, salary, experience, branch) VALUES ('Bobur', 'Rahimov', 4500000, 7, 'Chilonzor')")
            self.c.execute("INSERT INTO teachers (name, surname, salary, experience, branch) VALUES ('Sardor', 'Toshmatov', 6000000, 15, 'Mirzo Ulugbek')")
            self.c.execute("INSERT INTO teachers (name, surname, salary, experience, branch) VALUES ('Jasur', 'Yusupov', 3800000, 3, 'Yunusobod')")
            self.c.execute("INSERT INTO teachers (name, surname, salary, experience, branch) VALUES ('Sherzod', 'Mirzayev', 7000000, 20, 'Shayxontohur')")
            self.c.execute("INSERT INTO teachers (name, surname, salary, experience, branch) VALUES ('Dilshod', 'Nazarov', 4200000, 5, 'Mirzo Ulugbek')")
            self.c.execute("INSERT INTO teachers (name, surname, salary, experience, branch) VALUES ('Firdavs', 'Xasanov', 5500000, 12, 'Chilonzor')")
            self.connection.commit()

    def insert_students(self):
        self.c.execute("SELECT COUNT(*) as cnt FROM students")
        if self.c.fetchone()['cnt'] == 0:
            self.c.execute("INSERT INTO students (name, surname, monthly_payment, course_duration, branch) VALUES ('Kamola', 'Ergasheva', 800000, 6, 'Yunusobod')")
            self.c.execute("INSERT INTO students (name, surname, monthly_payment, course_duration, branch) VALUES ('Zulfiya', 'Karimova', 600000, 4, 'Chilonzor')")
            self.c.execute("INSERT INTO students (name, surname, monthly_payment, course_duration, branch) VALUES ('Otabek', 'Toshmatov', 1000000, 8, 'Mirzo Ulugbek')")
            self.c.execute("INSERT INTO students (name, surname, monthly_payment, course_duration, branch) VALUES ('Malika', 'Rahimova', 750000, 5, 'Yunusobod')")
            self.c.execute("INSERT INTO students (name, surname, monthly_payment, course_duration, branch) VALUES ('Sanjar', 'Ergashev', 900000, 6, 'Shayxontohur')")
            self.c.execute("INSERT INTO students (name, surname, monthly_payment, course_duration, branch) VALUES ('Nilufar', 'Karimova', 650000, 3, 'Chilonzor')")
            self.c.execute("INSERT INTO students (name, surname, monthly_payment, course_duration, branch) VALUES ('Humoyun', 'Yusupov', 1100000, 9, 'Mirzo Ulugbek')")
            self.connection.commit()

    def sort_tTB(self):
        self.c.execute("SELECT * FROM teachers ORDER BY salary ASC")
        result = self.c.fetchall()
        for i in result:
            print(i)

    def experienceTB(self):
        self.c.execute("SELECT * FROM teachers ORDER BY salary ASC, experience DESC")
        result = self.c.fetchall()
        for i in result:
            print(i)

    def maxteacherTB(self):
        self.c.execute("SELECT MAX(salary) as max_sal FROM teachers")
        max_salary = self.c.fetchone()['max_sal']
        new_salary = max_salary - 500000
        self.c.execute(f"UPDATE teachers SET salary = {new_salary} WHERE salary = {max_salary}")
        self.connection.commit()
        print("maosh kamaytirildi:", max_salary, new_salary)

    def exp_tchilonzor(self):
        self.c.execute("SELECT MAX(experience) as max_exp FROM teachers")
        max_exp = self.c.fetchone()['max_exp']
        self.c.execute(f"UPDATE teachers SET branch = 'Chilonzor' WHERE experience = {max_exp}")
        self.connection.commit()

    def sort_lastTB(self):
        self.c.execute("SELECT * FROM students ORDER BY surname ASC")
        result = self.c.fetchall()
        for i in result:
            print(i)

    def sort_monthTB(self):
        self.c.execute("SELECT * FROM students ORDER BY monthly_payment DESC")
        result = self.c.fetchall()
        for i in result:
            print(i)

    def sum_studentTB(self):
        self.c.execute("SELECT SUM(monthly_payment * course_duration) as total FROM students")
        total = self.c.fetchone()['total']
        print(total)

    def maxs_dubayTB(self):
        self.c.execute("SELECT MAX(monthly_payment * course_duration) as max_total FROM students")
        max_total = self.c.fetchone()['max_total']
        self.c.execute(f"UPDATE students SET branch = 'Dubay' WHERE monthly_payment * course_duration = {max_total}")
        self.connection.commit()


    def list_branchTB(self):
        self.c.execute("""
            SELECT t.name, t.surname, s.name, s.surname, t.branch
            FROM teachers t
            INNER JOIN students s ON t.branch = s.branch
        """)
        result = self.c.fetchall()
        for i in result:
            print(i)

    def samenameTB(self):
        self.c.execute("""
            SELECT s1.name, s1.branch
            FROM students s1
            INNER JOIN students s2 ON s1.name = s2.name AND s1.id != s2.id
        """)
        result = self.c.fetchall()
        print("Ismi bir xil oquvchilar:")
        if result:
            for i in result:
                print(i)


    def samelastTB(self):
        self.c.execute("""
            SELECT s1.surname, s1.monthly_payment
            FROM students s1
            INNER JOIN students s2 ON s1.surname = s2.surname AND s1.id != s2.id
        """)
        result = self.c.fetchall()
        print("Familiyadosh oquvchilar:")
        if result:
            for i in result:
                print(i)



db = SchoolDB()
db.create_tables()
db.insert_teachers()
db.insert_students()

db.sort_tTB()
db.experienceTB()
db.maxteacherTB()
db.exp_tchilonzor()
db.sort_lastTB()
db.sort_monthTB()
db.sum_studentTB()
db.maxs_dubayTB()
db.list_branchTB()
db.samenameTB()
db.samelastTB()
