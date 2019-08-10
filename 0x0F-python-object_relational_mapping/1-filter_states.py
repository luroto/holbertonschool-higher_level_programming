#!/usr/bin/python3
""" This module connects a database and prints a database"""
import sys
import MySQLdb
if __name__ == '__main__':
    db = MySQLdb.connect(
            host="localhost",
            user=str(sys.argv[1]),
            password=str(sys.argv[2]),
            db=str(sys.argv[3]),
            port=3306,
        )
    cura = db.cursor()
    cura.execute("SELECT * FROM states WHERE states.name LIKE 'N%' ORDER BY states.id ASC")
    catchi = cura.fetchall()
    if catchi:
        for it in catchi:
            print("{}".format(it))
