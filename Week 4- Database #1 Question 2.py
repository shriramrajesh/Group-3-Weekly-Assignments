import sqlite3
conn1 = sqlite3.connect('hospitaldoctor.db')
cursor1 = conn1.cursor()
cursor1.execute("DROP TABLE IF EXISTS HOSPITAL")
query1 = """CREATE TABLE HOSPITAL(
        Hospital_Id INT PRIMARY KEY,
        Hospital_Name CHAR(20), 
        Bed_Count INT)"""
cursor1.execute(query1)
conn1.execute("INSERT or IGNORE INTO HOSPITAL (Hospital_Id,Hospital_Name,Bed_Count) "
                 "VALUES (1,'Mayo Clinic',200)")
conn1.execute("INSERT or IGNORE INTO HOSPITAL (Hospital_Id,Hospital_Name,Bed_Count) "
                 "VALUES (2,'Cleveland Clinic',400)")
conn1.execute("INSERT INTO HOSPITAL (Hospital_Id,Hospital_Name,Bed_Count) "
                 "VALUES (3,'John Hopkins',1000)")
conn1.execute("INSERT INTO HOSPITAL (Hospital_Id,Hospital_Name,Bed_Count) "
                 "VALUES (4,'UCLA Medical Center',1500)")
conn1.commit()
cursor1 = conn1.execute("SELECT * from HOSPITAL")
print(cursor1.fetchall())
conn = sqlite3.connect('hospitaldoctor.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS DOCTOR")
query = """CREATE TABLE DOCTOR(
        Doctor_Id INT PRIMARY KEY,
        Doctor_Name CHAR(20), 
        Hospital_Id INT REFERENCES HOSPITAL (Hospital_Id),
        Joining_Date DATE FORMAT 'yyyy-mm-dd',
        Speciality CHAR(20), 
        Salary INT,
        Experience NULL )"""
cursor.execute(query)
conn.execute("INSERT INTO DOCTOR (Doctor_Id,Doctor_Name,Hospital_Id,Joining_Date,Speciality,Salary,Experience) "
                 "VALUES (101,'David',1,2005-02-10,'Pediatric',40000,NULL)")
conn.execute("INSERT INTO DOCTOR (Doctor_Id,Doctor_Name,Hospital_Id,Joining_Date,Speciality,Salary,Experience) "
                 "VALUES (102,'Michael',1,2018-07-23,'Oncologist',20000,NULL)")
conn.execute("INSERT INTO DOCTOR (Doctor_Id,Doctor_Name,Hospital_Id,Joining_Date,Speciality,Salary,Experience) "
                 "VALUES (103,'Susan',2,2016-05-19,'Garnacologist',25000,NULL)")
conn.execute("INSERT INTO DOCTOR (Doctor_Id,Doctor_Name,Hospital_Id,Joining_Date,Speciality,Salary,Experience) "
                 "VALUES (104,'Robert',2,2017-12-28,'Pediatric',28000,NULL)")
conn.execute("INSERT INTO DOCTOR (Doctor_Id,Doctor_Name,Hospital_Id,Joining_Date,Speciality,Salary,Experience) "
                 "VALUES (105,'Linda',3,2004-06-04,'Garnacologist',42000,NULL)")
conn.execute("INSERT INTO DOCTOR (Doctor_Id,Doctor_Name,Hospital_Id,Joining_Date,Speciality,Salary,Experience) "
                 "VALUES (106,'William',3,2012-09-11,'Dermatologist',30000,NULL)")
conn.execute("INSERT INTO DOCTOR (Doctor_Id,Doctor_Name,Hospital_Id,Joining_Date,Speciality,Salary,Experience) "
                 "VALUES (107,'Richard',4,2014-08-21,'Garnacologist',32000,NULL)")
conn.execute("INSERT INTO DOCTOR (Doctor_Id,Doctor_Name,Hospital_Id,Joining_Date,Speciality,Salary,Experience) "
                 "VALUES (108,'Karen',4,2011-10-17,'Radiologist',30000,NULL)")
conn.commit()
cursor = conn.execute("SELECT * from DOCTOR")
print(cursor.fetchall())
sp=input("Enter Speciality")
sa=(input("Enter Salary"))
cursor2 = conn.execute("SELECT * from DOCTOR where Speciality= '"+ sp + "' and Salary>= '"+ sa + "'")
cursor3 = conn.execute("SELECT Doctor_Id,Doctor_Name,DOCTOR.Hospital_Id,Joining_Date,Speciality,Salary,Experience,Hospital_Name from DOCTOR,HOSPITAL where HOSPITAL.Hospital_Id=DOCTOR.Hospital_Id")
print(cursor2.fetchall())
print(cursor3.fetchall())
conn1.close()
conn.close()
