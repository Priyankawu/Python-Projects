import sqlite3

firstName = input("What is your first name?")
lastName = input("What is your last name?")
age = int(input("Enter your age: ")) #?? What is the int doing?


with sqlite3.connect('test_database.db') as connection:
    c=connection.cursor()
    command="CREATE TABLE IF NOT EXISTS People(firstName,lastName,Age)"
    c.execute(command)
    line = "INSERT INTO People VALUES ('"+firstName+"', '"+lastName+"', "+str(age)+")"
    c.execute(line)
    
