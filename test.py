import argparse
import sqlite3
from sqlite3 import OperationalError
from mysql.connector import Error
import mysql.connector
from mysql.connector.errors import DatabaseError

try:
    conn = mysql.connector.connect(host='localhost', database='python_sql', user='root', password='admin')
    if conn.is_connected():
        print('Connected to MySQL database')
    else:
        print('Connection failed.')
except Error as e:
    print(e)
try:
    arg_parser = argparse.ArgumentParser(description="Enter A File Name")
    arg_parser.add_argument("source_file")
    arguments = arg_parser.parse_args()
    source = arguments.source_file
    #cur = conn.cursor()
    #file = open("Select.sql", 'r')
    #sql = " ".join(file.readlines())
    #cur.execute(sql)
    cur = conn.cursor()
    fd = open(source, 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')
    for command in sqlCommands:
        try:
            cur.execute(command)
        except Error as error:
            print(error)
except Error as error:
    print(error)
    conn.rollback()
try:
    for x in cur:
        print(x)
except Error as e:
    print(e)
conn.close()
