#!/usr/bin/python3
""" This script connects to a database and list its content based on a
given field"""
if __name__ == '__main__':
    import MySQLdb
    import sys
    databba = MySQLdb.connect(
                host='localhost',
                user=str(sys.argv[1]),
                password=str(sys.argv[1]),
                db=str(sys.argv[3]),
                port=3306,
                )
    consulta = databba.cursor()
    consulta.exec("""SELECT cities.id, cities.name, states.name
                    FROM cities, states
                    WHERE cities.state_id = states.id
                    ORDER BY cities.id ASC""")
    catchi = consulta.fetchall()
    if catchi:
        for element in catchi:
            print({}.format(catchi))
    consulta.close()
    databba.close()
