import sqlite3

connection = sqlite3.connect("C:/Users/legol/Desktop/Roster.db")

c = connection.cursor()

c.execute("CREATE TABLE IF EXISTS Roster(Name TEXT, Species TEXT, IQ INT)")

peopleValues = (('Jean-Baptiste Zorg', 'Human', 122), ('Korban Dallas', 'Meat Popsicle', 100), ("Ak'not", "Mangalore", -5))

c.executemany("INSERT INTO Roster VALUES(?,?,?)", peopleValues)

peopleValues = (('Jean-Baptiste Zorg', 'Human', 122), ('Korban Dallas', 'Meat Popsicle', 100), ("Ak'not", "Mangalore", -5))
c.executemany("INSERT INTO Roster VALUES(?,?,?)", peopleValues)

c.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?",
          ('Human', 'Korban Dallas', 100))

c.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")

for row in c.fetchall():
    print(row)
