class ArchiveItem:
    class InvalidLineFormatException(Exception):
        pass

    def __init__(self, name = None, archive_id = None):
        self.name = name
        self.archive_id = archive_id
        self.year = "2014"
        try:
            self.friendly_name = ArchiveItem._get_friendly_name(self.name)
        except:
            self.friendly_name = self.name

    @staticmethod
    def _get_friendly_name(name):
        tokens = name.split('-')
        output = []

        for i in tokens:
            text = [x for x in i]
            text[0] = text[0].upper()
            output.append(''.join(text))
        
        return ' '.join(output)
    
    @property
    def download_game_link(self):
        link = f"https://web.archive.org/web/{self.year}/http://sandbox.yoyogames.com/games/{self.archive_id}/download"
        return link
    
    @property
    def game_page_link(self):
        link = f"https://web.archive.org/web/{self.year}/http://sandbox.yoyogames.com/games/{self.archive_id}-{self.name}"
        return link
    
    @staticmethod
    def import_line(string):
        try:
            game_id_name = string.split(':')[1]
            game_id, game_name = game_id_name.split('-', 1)

            return ArchiveItem(game_name, game_id)
        except IndexError:
            raise ArchiveItem.InvalidLineFormatException(f"{string} is not in the valid game:id-name format")