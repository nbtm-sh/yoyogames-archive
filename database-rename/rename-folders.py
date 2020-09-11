import sqlite3
import shutil
import os

database = sqlite3.connect('metadata.db')
cursor = database.cursor()

for i in os.listdir('./download/'):
    folder = i.replace('./download/', '')
    rows = cursor.execute(f"SELECT * FROM GAMES WHERE FULLID LIKE \"%{folder}\"")
    rows = rows.fetchall()

    for i in rows:
        print(i[1])