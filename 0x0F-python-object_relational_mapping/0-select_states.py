#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""


import MySQLdb
import sys


conn = MySQLdb.connect(host="localhost", port=3306,
                       user="{}".format(sys.argv[1]),
                       passwd="{}".format(sys.argv[2]),
                       db="{}".format(sys.argv[3]),
                       charset="utf8")

cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
