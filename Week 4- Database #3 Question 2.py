import sqlite3
conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor() 
print(conn.execute("select count(*) from Teams").fetchall())                                                                         
print(conn.execute("select distinct Season from Teams").fetchall())                                                                 
print(conn.execute("select min(StadiumCapacity),max(StadiumCapacity) from Teams").fetchall())                                        
print(conn.execute("select sum(KaderHome) from Teams where Season= 2014").fetchall())                                                 
print(conn.execute("select avg(FTHG) from Matches where HomeTeam='Man United'").fetchall())  
