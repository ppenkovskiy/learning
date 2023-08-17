import psycopg2
from psycopg2.extras import RealDictCursor, execute_values

conn = psycopg2.connect(dbname='postgres', user='postgres', password='5035')

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS superheroes;')
cur.execute('DROP TABLE IF EXISTS traffic_light;')

conn.commit()

cur.execute('CREATE TABLE superheroes (hero_id serial PRIMARY KEY, hero_name varchar, strength int);')

cur.execute('INSERT INTO superheroes (hero_name, strength) VALUES (%s, %s)', ('name_1', 1000))
cur.execute("INSERT INTO superheroes (hero_name, strength) VALUES (%s, %s)", ('name_2', 1001))
cur.execute("INSERT INTO superheroes (hero_name, strength) VALUES (%s, %s)", ('name_3', 999))

conn.commit()

cur.execute("CREATE TABLE traffic_light (light_id serial PRIMARY KEY, light text);")

cur.execute("INSERT INTO traffic_light(light) VALUES (%s)", ('red',))

cur.execute('SELECT * from superheroes')

one_line = cur.fetchone()
print(one_line)

all_lines = cur.fetchall()
print(all_lines)

conn.commit()

cur.close()
conn.close()

with psycopg2.connect(dbname='postgres', user='postgres', password='5035') as conn:
    with conn.cursor(cursor_factory=RealDictCursor) as curs:
        execute_values(curs, 'INSERT INTO traffic_light (light) VALUES %s', [('green',), ('red',), ('yellow',)])

        curs.execute('SELECT * FROM traffic_light')
        records = curs.fetchall()
        print(records)
        print(records[0]['light'])


conn = psycopg2.connect(dbname='postgres', user='postgres', password='5035')
with conn:
    with conn.cursor() as curs:
        curs.execute("""
                    UPDATE superheroes 
                    SET strength = %s
                    WHERE hero_name = %s
                    """, (90, 'name_1'))

with conn:
    with conn.cursor() as curs:
        curs.execute("""
                    SELECT * FROM superheroes
                    """)
        print(curs.fetchall())

conn.close()

