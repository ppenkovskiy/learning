import psycopg2

conn = psycopg2.connect(dbname='postgres', user='postgres', password = '5035')

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS superheroes;')
cur.execute('DROP TABLE IF EXISTS traffic_light;')

conn.commit()

cur.execute('CREATE TABLE superheroes (hero_id serial PRIMARY KEY, hero_name varchar, strength int);')

cur.execute('INSERT INTO superheroes (hero_name, strength) VALUES (%s, %s)', ('name_1', 1000))

cur.execute("""
            INSERT INTO superheroes (hero_name, strength) 
            VALUES (%s, %s)
            """, ('name_2', 1001))

conn.commit()