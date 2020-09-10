import src.url as url
from bs4 import BeautifulSoup
import requests
from time import strptime
import datetime

class Page:
    def __init__(self, line, user_agent = "YoYoGames Database Archive Project (github/NathanBitTheMoon)"):
        self.url = url.construct_archive_url(line)
        self.page = requests.get(self.url).content

        f = open('f.html', 'wb')
        f.write(self.page)
        f.flush()
        f.close()

        self.bs4_data = BeautifulSoup(self.page, "html.parser")

        self.name = self.bs4_data.find_all('div', {"class": "top"})[0].find_all('a')[0].text
        self.creator = self.bs4_data.find_all('div', {"class": "top"})[0].find_all('a')[1].text
        self.category = self.bs4_data.find_all('div', {"class", "top"})[0].find_all('a')[2].text
        self.description = self.bs4_data.find_all('div', {"class": "right"})[0].find_all('p')[3].text.replace('\n', '<br>')
        self.tags = [i.text for i in self.bs4_data.find_all('div', {"class": "tags"})[0].find_all('ul')[0].find_all('a')]
        self.version = self.bs4_data.find_all('div', {"class": "right"})[0].find_all("p")[0].contents[11].strip().replace("\n", "").replace('\t\t', '')
        self.featured = len(self.bs4_data.find_all('div', {"class": "staffpick"})) > 0
        self.plays = self.bs4_data.find_all('span', {"id": "game-downloads"})[0].contents[2].text
        self.full_id = line.split(':', 1)[1]
        self.id = line.split(':', 1)[1].split('-', 1)[0]

        self.day, self.month, self.year = self.bs4_data.find_all('div', {"class": "right"})[0].find_all('p')[0].contents[2].strip().split(' ')
        self.sql_date_time = Page.sql_date(self.day, self.month, self.year)
    
    @staticmethod
    def sql_date(day, month, year):
        day = int(day)
        month = strptime(month,'%B').tm_mon
        year = int(year)

        date = datetime.datetime(year, month, day)
        return date.strftime("%Y-%m-%d")
