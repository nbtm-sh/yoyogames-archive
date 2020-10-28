import sqlite3
import shutil
import os

GAMES_FILE = '../game-dl/txt/games.txt'
DOWNLOAD_DIRECTORY = '../game-dl/download/'

file_rows = open(GAMES_FILE).readlines()

for i in os.listdir(DOWNLOAD_DIRECTORY):
    folder = i.replace(DOWNLOAD_DIRECTORY, '')
    rename = ""
    for x in file_rows:
        if folder in x:
            rename = x.strip().replace("game:", "")
            print(rename, x)
    
    print(DOWNLOAD_DIRECTORY + i, DOWNLOAD_DIRECTORY + rename)
    os.rename(DOWNLOAD_DIRECTORY + i, DOWNLOAD_DIRECTORY + rename)