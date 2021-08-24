import argparse

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def lastversion():
    arg_parser = argparse.ArgumentParser(description="Enter A File Name")
    arg_parser.add_argument("source_file")
    arguments = arg_parser.parse_args()
    source = arguments.source_file
    global cur
    db_config = read_db_config()
    conn = None
    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)
        if conn.is_connected():
            print('Connection established.')
        else:
            print('Connection failed.')
    except Error as error:
        print(error)
    try:
        cur = conn.cursor()
        fd = open(source, 'r')
        sqlFile = fd.read()
        fd.close()
        sqlCommands = sqlFile.split(';')
        for command in sqlCommands:
            try:
                if command.strip() != '':
                    cur.execute(command)
                    print("Executed Successfully " + " "+'\n' + command)
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


if __name__ == '__main__':
    lastversion()
