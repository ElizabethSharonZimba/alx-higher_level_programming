#!/usr/bin/python3
"""Script to list all states from a MySQL database"""

import MySQLdb
from sys import argv

def list_states(username, password, database):
    """Connect to the database and retrieve all states"""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

if __name__ == '__main__':
    if len(argv) == 4:
        list_states(argv[1], argv[2], argv[3])
