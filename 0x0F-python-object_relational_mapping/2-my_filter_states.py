#!/usr/bin/python3
""" This module connects to a database and lists the matching
rows given some inputs"""
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
    inpu = str(sys.argv[4])
    cura = db.cursor()
    cura.execute("""SELECT *
                 FROM states
                 WHERE states.name LIKE BINARY "{}"
                 ORDER BY states.id ASC
                 """.format(inpu))
    catchi = cura.fetchall()
    if catchi:
        for it in catchi:
            print("{}".format(it))
    cura.close()
    db.close()
