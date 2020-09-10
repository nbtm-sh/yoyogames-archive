def construct_archive_url(line):
    data = line.split(':')[1]
    return f"https://web.archive.org/web/2014/http://sandbox.yoyogames.com/games/{data}"