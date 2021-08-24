import sqlite3

try:
    # if there is no data base with this name it will created
    # Please Enter the database name
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")


    sql_file = open("../Select.sql")
    sql_as_string = sql_file.read()
    cursor.executescript(sql_as_string)

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")