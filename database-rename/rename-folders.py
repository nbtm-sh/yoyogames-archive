import sqlite3
import shutil
import os

file_rows = open('../../txt/games.txt').readlines()

for i in os.listdir('../../download/'):
    folder = i.replace('../../download/', '')
    rename = ""
    for i in file_rows:
        if folder in i:
            rename = i.strip().replace("game:", "")
    
    print(rename)