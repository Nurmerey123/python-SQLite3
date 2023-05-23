import sqlite3 as sq

with sq.connect("employee.db") as con:
    cur = con.cursor()

    cur.execute(""" CREATE TABLE IF NOT EXISTS person(
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL,
        job TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL
    ) """)

    cur.execute(""" SELECT count(*) FROM person """)
    result = cur.fetchone()

    if result[0] == 0:
        cur.execute("""INSERT INTO person (firstname, lastname, job, email, age) VALUES (?, ?, ?, ?, ?)""",
                    ('Mahmoud','David', 'boss', 'mahmouddavid@gmail.com', 40))
        con.commit()
    cur.execute("""INSERT INTO person (firstname, lastname, job, email, age) VALUES (?, ?, ?, ?, ?)""",
                    ('maks','jeff', 'draiver', 'JeffMaks@gmail.com', 26))
    con.commit()
    print("hello")
    fskjpseu