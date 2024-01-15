#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], password=sys.argv[2], db=sys.argv[3], port=3306)
    
    cus = db.cusor()
    match = sys.argv[4]
    cus.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    row = cus.fetchall()
    for row in rows:
        print(row)
        cus.close()
        db.close()