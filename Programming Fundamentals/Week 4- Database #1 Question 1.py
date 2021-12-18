import sqlite3
conn = sqlite3.connect('carowner.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Cars")
query = "CREATE TABLE Cars(CARNAME CHAR(20), OWNERNAME CHAR(20))"
cursor.execute(query)
conn.execute("INSERT INTO Cars (CARNAME,OWNERNAME) VALUES ('Audi', 'John'),('Tata', 'Adams'),('Mahindra', ' Baker'),('Honda', 'Clark'),('Maruti Suzuki', 'Davis'),('Toyota', 'Evans'),('Chevorlet', 'Frank'),('Mitsubishi', 'Ghosh'),('Ford', 'Hills'),('BMW', 'Irwin')")
print(conn.execute("SELECT * from CAROWNER").fetchall())
conn.close()
