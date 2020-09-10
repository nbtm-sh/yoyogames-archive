from bs4 import BeautifulSoup
import requests

class WebArchivePage:
    def __init__(self, archive_item):
        self.archive_item = archive_item
        self.bs4_download_page = WebArchivePage._get_bs4(archive_item.download_game_link)
        self.bs4_game_page = WebArchivePage._get_bs4(archive_item.game_page_link)

    def get_download_button(self):
        tags = self.bs4_download_page.find_all("a")
        tags = ("https://web.archive.org" + tags[16]['href']).split('/')
        tags[4] = tags[4] + "if_"
        
        return '/'.join(tags)
    
    @staticmethod
    def _get_bs4(page):
        bs4_page = requests.get(page)
        bs4_page = BeautifulSoup(bs4_page.content, "html.parser")

        return bs4_page