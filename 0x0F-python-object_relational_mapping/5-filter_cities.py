#!/usr/bin/python3
""" This script connects to a database of cities and states and print all
which matches with the input received from the command line"""
if __name__ == '__main__':
    import MySQLdb
    import sys
    databba = MySQLdb.connect(
                host='localhost',
                user=str(sys.argv[1]),
                password=str(sys.argv[2]),
                db=str(sys.argv[3]),
                port=3306,
                )
    queso = str(sys.argv[4])
    consulta = databba.cursor()
    consulta.execute("""SELECT cities.name
                    FROM cities, states
                    WHERE %s = states.name AND states.id = cities.state_id
                    ORDER BY cities.id ASC""", [queso])
    catchi = consulta.fetchall()
    listi = list()
    if catchi:
        for element in catchi:
            listi.append(element[0])
    print(', '.join(listi))
    consulta.close()
    databba.close()
