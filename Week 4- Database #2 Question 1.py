import sqlite3
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
query = """CREATE TABLE EMPLOYEE(
        Name CHAR(20), 
        ID INT,
        Salary INT,
        Department_id INT)"""
cursor.execute(query)
conn.execute("ALTER TABLE EMPLOYEE "
             "ADD City CHAR(20)")
conn.execute("INSERT INTO EMPLOYEE (Name,ID,Salary,Department_id,City)"
                 "VALUES ('David',101,40000,1,'Mumbai')")
conn.execute("INSERT INTO EMPLOYEE (Name,ID,Salary,Department_id,City)"
                 "VALUES ('Michael',102,20000,2,'New Delhi')")
conn.execute("INSERT INTO EMPLOYEE (Name,ID,Salary,Department_id,City)"
                 "VALUES ('Susan',103,25000,3,'Bangalore')")
conn.execute("INSERT INTO EMPLOYEE (Name,ID,Salary,Department_id,City)"
                 "VALUES ('James',104,28000,4,'Hyderabdad')")
conn.execute("INSERT INTO EMPLOYEE (Name,ID,Salary,Department_id,City)"
                 "VALUES ('Linda',105,42000,5,'Chennai')")
conn.commit()
print(conn.execute("SELECT * from EMPLOYEE").fetchall())
print(conn.execute("SELECT Name,ID,Salary from EMPLOYEE").fetchall())
n=input("Enter the first letter of employee name")
print(conn.execute("SELECT * from EMPLOYEE where upper(Name) LIKE'"+ n +"%'").fetchall())
id=input("Enter id of employee")
print(conn.execute("SELECT * from EMPLOYEE where ID='"+ id +"'").fetchall())
id=input("Enter id of employee to change employee name")
nn=input("Enter new employee name")
conn.execute("UPDATE EMPLOYEE SET Name= '"+ nn +"'where ID='"+ id +"'")
print(conn.execute("SELECT * from EMPLOYEE").fetchall())
conn.close()
