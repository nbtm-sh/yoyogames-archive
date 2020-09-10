import requests

class FileUtils:
    @staticmethod
    def get_filename(url):
        page = requests.get(url)
        return eval(page.headers['Content-Disposition'].split("filename=")[1])