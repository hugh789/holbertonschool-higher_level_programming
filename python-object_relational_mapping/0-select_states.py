#!/usr/bin/python3
""" Nameless module for running SQL """


if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    c = db.cursor()
    c.execute("""SELECT * FROM states ORDER BY id ASC""")
    rows = c.fetchall()

    for row in rows:
        print("({0}, '{1}')".format(row[0], row[1]))

        # print("(%s, " % row[0], end = "")
        # print("%s)" % row[1])