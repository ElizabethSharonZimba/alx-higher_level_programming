#!/usr/bin/python3
"""
This script retrieves states from the hbtn_0e_0_usa database
based on the provided state name.
"""

import MySQLdb
import sys

def main():
    """
    Main function to execute the script.
    """
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

if __name__ == '__main__':
    main()

