#!/usr/bin/python3
""" takes in an argument and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument. """

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user="{}".format(sys.argv[1]),
                           passwd="{}".format(sys.argv[2]),
                           db="{}".format(sys.argv[3]),
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
    ORDER BY states.id ASC".format(sys.argv[4]))

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
