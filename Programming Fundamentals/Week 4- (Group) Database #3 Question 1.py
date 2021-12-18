import sqlite3
conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()                                                                                                              
print(conn.execute("select HomeTeam,AwayTeam from Matches where Season=2015 and FTHG=5").fetchall())                                
print(conn.execute("select * from Matches where HomeTeam= 'Arsenal' and FTR='A'").fetchall())                                       
print(conn.execute("select * from Matches where AwayTeam= 'Bayern Munich' and Season>=2012 and Season<=2015 and FTHG>2").fetchall())  
print(conn.execute("select * from Matches where upper(HomeTeam) LIKE 'A%' and upper(AwayTeam) LIKE 'M%'").fetchall())
