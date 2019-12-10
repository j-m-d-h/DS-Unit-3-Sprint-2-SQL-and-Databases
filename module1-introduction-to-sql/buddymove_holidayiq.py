import sqlite3
import os
import pandas as pd


df = pd.read_csv('buddymove_holidayiq.csv')

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()
conn.commit()

df.to_sql('REVIEW', conn, if_exists='replace')

answer_11 = curs.execute('SELECT COUNT(*) FROM REVIEW').fetchall()

answer_12 = curs.execute('SELECT COUNT(*) FROM REVIEW WHERE Nature >= 100 AND Shopping >= 100').fetchall()

print(answer_11, answer_12)
