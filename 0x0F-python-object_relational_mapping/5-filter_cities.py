#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    
    cus = db.cursor()
    cus.execute("""SELECT cities.name FROM cities INNER JOIN states ON states.id= cities.states_id WHERE states.name=%s""", (sys.argv[4],))
    row = cus.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cus.close()
    db.close()