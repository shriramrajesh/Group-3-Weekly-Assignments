import sqlite3
conn = sqlite3.connect('hospitaldoctor.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS HOSPITAL")
query = "CREATE TABLE HOSPITAL(Hospital_Id INT PRIMARY KEY,Hospital_Name CHAR(20),Bed_Count INT)"
cursor.execute(query)
conn.execute("INSERT INTO HOSPITAL (Hospital_Id,Hospital_Name,Bed_Count) VALUES (1,'Mayo Clinic',200),(2,'Cleveland Clinic',400),(3,'John Hopkins',1000),(4,'UCLA Medical Center',1500)")
print(conn.execute("SELECT * from HOSPITAL").fetchall())
conn = sqlite3.connect('hospitaldoctor.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS DOCTOR")
query = "CREATE TABLE DOCTOR(Doctor_Id INT PRIMARY KEY,Doctor_Name CHAR(20), Hospital_Id INT REFERENCES HOSPITAL (Hospital_Id),Joining_Date DATE FORMAT 'yyyy-mm-dd',Speciality CHAR(20), Salary INT,Experience NULL )"
cursor.execute(query)
conn.execute("INSERT INTO DOCTOR (Doctor_Id,Doctor_Name,Hospital_Id,Joining_Date,Speciality,Salary,Experience) VALUES (101,'David',1,2005-02-10,'Pediatric',40000,NULL),(102,'Michael',1,2018-07-23,'Oncologist',20000,NULL),(103,'Susan',2,2016-05-19,'Garnacologist',25000,NULL),(104,'Robert',2,2017-12-28,'Pediatric',28000,NULL),(105,'Linda',3,2004-06-04,'Garnacologist',42000,NULL),(106,'William',3,2012-09-11,'Dermatologist',30000,NULL),(107,'Richard',4,2014-08-21,'Garnacologist',32000,NULL),(108,'Karen',4,2011-10-17,'Radiologist',30000,NULL)")
def display_details():
    print(conn.execute("SELECT * from DOCTOR").fetchall())
def speciality_salary(sp,sa):
    print(conn.execute("SELECT * from DOCTOR where Speciality= '"+ sp + "' and Salary>= '"+ sa + "'").fetchall())
def hospital_id():
    print(conn.execute("SELECT Doctor_Id,Doctor_Name,DOCTOR.Hospital_Id,Joining_Date,Speciality,Salary,Experience,Hospital_Name from DOCTOR,HOSPITAL where HOSPITAL.Hospital_Id=DOCTOR.Hospital_Id").fetchall())
display_details()
a='y'
while(a=='y'):
    sp=input("Enter Speciality")
    sa=(input("Enter Salary"))
    speciality_salary(sp, sa)
    a=input("Would you like to try again? Press y for yes and any other key for no")
conn.close()
