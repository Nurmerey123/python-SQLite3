import sqlite3 as sq

with sq.connect("orders.db") as con:
    cur = con.cursor()

    cur.execute(""" CREATE TABLE IF NOT EXISTS person(
        person_id INTEGER PRIMARY KEY,
        id INTEGER NOT NULL
        name TEXT NOT NULL,
        age INTEGER NOT NULL  
    )""")

    cur.execute(""" SELECT   count(*) FROM person """)
    result = cur.fetchone()

    if result[0] == 0:
        cur.executemany(""" INSERT INTO person (id, name, age ) VALUES (00001, 'David', 18 ) """)
        con.commit()
        more_users = [('00002', 'Peter', '16'), ('00003', 'Bruce', '17')]

    cur.execute(""" DROP TABLE person """) # удаление таблицы

    cur.execute(""" UPDATE person SET name = 'Alex' WHERE name = 'John' """) #редактирование

    cur.execute(""" DELETE FROM person WHERE name = 'Alex' """) # удалить данные



