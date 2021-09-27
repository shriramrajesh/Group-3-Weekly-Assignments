import sqlite3
conn = sqlite3.connect('carowner.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Cars")
query = """CREATE TABLE Cars(
        CARNAME CHAR(20), 
        OWNERNAME CHAR(20))"""
cursor.execute(query)
conn.execute("INSERT INTO Cars (CARNAME,OWNERNAME) "
                 "VALUES ('Audi', 'John')")
conn.execute("INSERT INTO Cars (CARNAME,OWNERNAME) "
                 "VALUES ('Tata', 'Adams')")
conn.execute("INSERT INTO Cars (CARNAME,OWNERNAME) "
                 "VALUES ('Mahindra', ' Baker')")
conn.execute("INSERT INTO Cars (CARNAME,OWNERNAME) "
                 "VALUES ('Honda', 'Clark')")
conn.execute("INSERT INTO Cars (CARNAME,OWNERNAME) "
                 "VALUES ('Maruti Suzuki', 'Davis')")
conn.execute("INSERT INTO Cars (CARNAME,OWNERNAME) "
                 "VALUES ('Toyota', 'Evans')")
conn.execute("INSERT INTO Cars (CARNAME,OWNERNAME) "
                 "VALUES ('Chevorlet', 'Frank')")
conn.execute("INSERT INTO Cars (CARNAME,OWNERNAME) "
                 "VALUES ('Mitsubishi', 'Ghosh')")
conn.execute("INSERT INTO Cars (CARNAME,OWNERNAME) "
                 "VALUES ('Ford', 'Hills')")
conn.execute("INSERT INTO Cars (CARNAME,OWNERNAME) "
                 "VALUES ('BMW', 'Irwin')")
conn.commit()
cursor = conn.execute("SELECT * from CAROWNER")
print(cursor.fetchall())
conn.close()
