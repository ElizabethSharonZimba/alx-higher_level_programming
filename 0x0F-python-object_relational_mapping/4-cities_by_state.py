#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
This time the script is safe from
MySQL injections!
"""

import MySQLdb
import sys

if __name__ == '__main__':
    args = sys.argv
    if len(args) < 5:
        print("Usage: {} username password db_name state_name".format(args[0]))
        exit(1)

    username = args[1]
    password = args[2]
    database = args[3]
    state_name = args[4]

    try:
        db = MySQLdb.connect(host='localhost', user=username,
                             passwd=password, db=database,
                             port=3306)
        cur = db.cursor()

        cur.execute("SELECT * FROM states WHERE name=%s", (state_name,))
        rows = cur.fetchall()

        if rows:
            for row in rows:
                print(row)
        else:
            print("No states found with the name '{}'".format(state_name))

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(str(e)))

    except Exception as e:
        print("An unexpected error occurred:", str(e))

    finally:
        if cur:
            cur.close()
        if db:
            db.close()

