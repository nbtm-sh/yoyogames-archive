import sqlite3
import shutil
import os

GAMES_FILE = '../../txt/games.txt'
DOWNLOAD_DIRECTORY = '../../download/'

file_rows = open(GAMES_FILE).readlines()

for i in os.listdir(DOWNLOAD_DIRECTORY):
    folder = i.replace(DOWNLOAD_DIRECTORY, '')
    rename = ""
    for i in file_rows:
        if folder in i:
            rename = i.strip().replace("game:", "")
    
    print(i, DOWNLOAD_DIRECTORY + rename)
    os.rename(i, DOWNLOAD_DIRECTORY + '/' + rename)