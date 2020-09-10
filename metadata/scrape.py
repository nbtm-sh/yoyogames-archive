import src.meta as meta
import src.database as database
import threading

games = open('txt/games.txt').readlines()


database = database.Database("metadata.db")
file_div = [[] for i in range(5)]

for i in range(len(games)):
    p = i % len(file_div)
    file_div[p].append(games[i])

for i in games:
    try:
        #if db.execute(f"SELECT COUNT(*) FROM GAMES WHERE FULLID=\'{i.strip()}\';").fetchone()[0] < 1:
        page = meta.Page(i.strip())
        database.add_row(page)
        
        print(f"Meta:", page.full_id)
        #else:
        #print(f"[Thread {str(thread_id)} Skip: ", page.full_id)
    except Exception as e:
        print(f"Fail: {str(e)}:", i)