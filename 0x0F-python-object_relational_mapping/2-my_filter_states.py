#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    if len(argv) != 5:
        print("Usage: {} <username> <password> <database> <name>".format(argv[0]))
        exit(1)

    username, password, database, name = argv[1:]

    try:
        db_connect = MySQLdb.connect(
            host="localhost", port=3306, user=username,
            passwd=password, db=database
        )
        db_cursor = db_connect.cursor()

        db_cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY states.id ASC",
            (name,)
        )
        rows_selected = db_cursor.fetchall()

        for row in rows_selected:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(str(e)))

    finally:
        if db_cursor:
            db_cursor.close()
        if db_connect:
            db_connect.close()
