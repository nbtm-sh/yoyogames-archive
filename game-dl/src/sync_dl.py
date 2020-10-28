import src.file_utils as fu
import src.archive_item as ai
import src.web_archive_page as wap
import requests
import os
from datetime import datetime

class SyncDL:
    def __init__(self, downloads, output_folder, verbose = True, path_delim = '/', error_log = None, thread_id = 0):
        self.downloads = downloads
        self.output_folder = output_folder
        self.verbose = verbose
        self.path_delim = path_delim
        self.error_log = error_log
        self.thread_id = thread_id
    
    def start_download_sync(self):
        for i in self.downloads:
            try:
                download_path = self.output_folder + self.path_delim + i.archive_id + "-" + i.name

                if (os.path.exists(download_path)):
                    continue # Skip this download
                page = wap.WebArchivePage(i)
                download_link = page.get_download_button()

                os.mkdir(download_path)
                dl_file = download_path + self.path_delim + fu.FileUtils.get_filename(download_link)

                start = datetime.now()

                with requests.get(download_link, stream=True) as r:
                    with open(dl_file, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            f.write(chunk)
                
                end = datetime.now()

                time = (end - start).total_seconds()
                size = os.path.getsize(dl_file)

                speed = round((size / time) / 1000000, 1)

                print(f"[Thread {str(self.thread_id)}]", download_path, f"Done. ({str(speed)} MiB/s)")
            except:
                self.error_log.missing_file(i)
                print(f"[Thread {str(self.thread_id)}]", download_path, f"Failed.")
