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
    cur.execute("SELECT cities.name FROM cities LEFT JOIN states\
    ON states.id = cities.state_id WHERE states.name = %s", [sys.argv[4]])

    query_rows = cur.fetchall()
    print(", ".join([row[0] for row in query_rows]))
    cur.close()
    conn.close()
