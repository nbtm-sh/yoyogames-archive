import sqlite3
import src.meta

class Database:
    def __init__(self, database):
        self.database = sqlite3.connect(database)
    
    @staticmethod
    def escape_string(string):
        string = string.replace("\"", "\\'")
        string = string.replace("\n", "<br>")
        string = string.replace("\'", "\\\'")

        return string

    def add_row(self, page : src.meta.Page):
        query = f'''INSERT INTO "GAMES" (ID, FULLID, NAME, CREATOR, TAGS, DATE, DESCRIPTION, CATEGORY, VERSION, ARCHIVEORG, FEATURED, LOCALDIR, PLAYS)
        VALUES (
            "{Database.escape_string(page.id)}",
            "{Database.escape_string(page.full_id)}",
            "{Database.escape_string(page.name)}",
            "{Database.escape_string(page.creator)}",
            "{Database.escape_string(','.join(page.tags))}",
            "{Database.escape_string(page.sql_date_time)}",
            "{Database.escape_string(page.description)}",
            "{Database.escape_string(page.category)}",
            "{Database.escape_string(page.version)}",
            "{Database.escape_string(page.url)}",
            0,
            "./",
            "{Database.escape_string(page.plays)}");'''
        try:
            self.database.execute(query)
        except:
            print(query)
            return
        self.database.commit()
        
        #print(query)