import sqlite3

firstName= input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
personData = (firstName, lastName, age)
peopleValues = (('Ron','Obvious',42),('Luigi','Vercotti',43),('Arthur','Belling',28))

with sqlite3.connect('database.ch_6.db') as connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS People(firstName,lastName,age")
    cursor.execute("INSERT INTO People VALUES(?,?,?)",personData)
    cursor.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?",(99,'Priya','Thak'))
    cursor.executemany("INSERT INTO People VALUES(?,?,?)",peopleValues)
    
    
