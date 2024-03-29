#!/usr/bin/python3
"""
Script that lists all states with a `name` starting with the letter `N`
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Connect to database
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' \
                 ORDER BY states.id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
