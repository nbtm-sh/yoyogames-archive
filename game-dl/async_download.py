CONFIG_PATH = "dl.conf"

# Read the config file
config = {}
config_file = open(CONFIG_PATH, 'r').readlines()

for i in config_file:
    key, value = i.split('=', 1)
    try:
        value = eval(value.strip())
    except:
        value = value.strip()
    
    config[key] = value

# Verify the integritiy of the file
present_keys = ["async", "sim_dl", "output_dir", "path_mode"]
missing = []
for i in present_keys:
    if i not in config.keys():
        missing.append(i)

if len(missing) > 0:
    print(f"[ERROR]. Configuration missing: {missing}")
    exit()

print(f"Downloading files to {config['output_dir']}... Reading from {config['dl_list']}")

# Import shit
import src.archive_item as ai
import src.sync_dl as sd
import src.web_archive_page as wap
import src.file_utils as fu
import src.error_log as el
import threading

# Read the lines and import them as archive items
list_file = open(config['dl_list'], 'r').readlines()
items = [ai.ArchiveItem.import_line(i.strip()) for i in list_file]

print(f"Preparing to download {len(items)} items...")

print("Dividing files into groups")
dispatch = [[] for i in range(config['sim_dl'])]

for i in range(len(items)):
    dispatch[i % config['sim_dl']].append(items[i])

for i in dispatch:
    print(len(i), end = ' ')

print()

threads = []
error_log =  el.ErrorLog("error.log")

def new_dl(files, i):
    sync_dl = sd.SyncDL(files, config['output_dir'], path_delim = '/' if config['path_mode'] == 'unix' else '\\', error_log = error_log, thread_id = i)
    print(f"Starting download on thread {i}")
    sync_dl.start_download_sync()

print("Starting threads...")

i = 0
for x in dispatch:
    t = threading.Thread(target=new_dl, args=(x,i,))
    t.start()
    i += 1

while True:
    pass