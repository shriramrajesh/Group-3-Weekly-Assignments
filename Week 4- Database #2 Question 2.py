import sqlite3
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
query = "CREATE TABLE EMPLOYEE(Name CHAR(20), ID INT,Salary INT,Department_id INT)"
cursor.execute(query)
conn.execute("ALTER TABLE EMPLOYEE ADD City CHAR(20)")
conn.execute("INSERT INTO EMPLOYEE (Name,ID,Salary,Department_id,City) VALUES ('David',101,40000,1,'Mumbai'),('Michael',102,20000,2,'New Delhi'),('Susan',103,25000,3,'Bangalore'),('James',104,28000,4,'Hyderabdad'),('Linda',105,42000,5,'Chennai')")

cursor.execute("DROP TABLE IF EXISTS DEPARTMENT")
query = "CREATE TABLE DEPARTMENT(Department_id INT,Department_name CHAR(20))"
conn.execute(query)
conn.execute("INSERT INTO DEPARTMENT (Department_id,Department_name) VALUES (1,'Business Development'),(2,'Sales'),(3,'Architecture'),(4,'Operations'),(5,'Customer Support')")
print(conn.execute("SELECT * FROM DEPARTMENT").fetchall())
a='y'
while(a=='y'):
    id=input("Enter Department ID")
    print(conn.execute("Select Name,ID,Salary,EMPLOYEE.Department_id,Department_name,City from EMPLOYEE,DEPARTMENT where EMPLOYEE.Department_id== '"+ id +"' and DEPARTMENT.Department_id== '"+ id +"'" ).fetchall())
    a=input("Would you like to try again? Press y for yes and any other key for no")
conn.commit()
conn.close()
