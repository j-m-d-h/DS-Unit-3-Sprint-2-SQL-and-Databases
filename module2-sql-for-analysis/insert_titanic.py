import psycopg2
import pandas as pd
import sqlite3


dbname = 'jwkdqjjp'
user = 'jwkdqjjp'
password = 'sqQzJxPWtQ6McpS0SHLRympoGnwvmOJt'
host = 'rajje.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

sl_conn = sqlite3.connect('titanic.sqlite3')

df = pd.read_csv('titanic.csv')

df.Name = df.Name.str.replace("'", "`")

df.to_sql(name='titanic', con=sl_conn, if_exists='replace')

sl_curs = sl_conn.cursor()

sl_curs.execute('SELECT * FROM titanic').fetchall()

create_table_titanic = """
    CREATE TABLE titanic(
    Survived INT,
    Pclass INT,
    Name VARCHAR,
    Sex VARCHAR(10),
    Age FLOAT,
    Siblings_Spouses_Aboard INT,
    Parents_Children_Aboard INT,
    Fare FLOAT
    )"""

#pg_curs.execute(create_table_titanic)

select_all_tables = """
    SELECT *
    FROM pg_catalog.pg_tables
    WHERE schemaname != 'pg_catalog'
    AND schemaname != 'information_schema';
"""

pg_curs.execute(select_all_tables)
pg_curs.fetchall()


titanic_db = sl_curs.execute('SELECT * FROM titanic;').fetchall()


for row in titanic_db:
    insert_rows = """
        INSERT INTO titanic (
        Survived,
        Pclass,
        Name,
        Sex,
        Age,
        Siblings_Spouses_Aboard,
        Parents_Children_Aboard,
        Fare
        )
        VALUES""" + str(row[1:]) + ';'
    #pg_curs.execute(insert_rows)

pg_curs.execute('SELECT * FROM titanic;')
pg_curs.fetchall()

final = pg_curs.fetchall()

first_query = """
    SELECT COUNT(survived)
    FROM "public"."titanic"
    WHERE survived=1;
"""

second_query = """
    SELECT COUNT(*)
    FROM "public"."titanic"
    GROUP BY pclass;
"""

first = pg_curs.execute(first_query)
second = pg_curs.execute(second_query)
print(first, second, pg_curs.fetchall()[0][0])

#pg_curs.close()
#pg_conn.commit()
