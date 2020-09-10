import time
import datetime
import psutil
import os

csv = open('out.csv', 'a')
DIRECTORY = "./download/"

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def get_time():
    return datetime.datetime.now().strftime("%Y-%M-%d %H:%M")

def convert_to_mbyte(value):
    return round(value/1000000, 1)

def get_net_throughput():
    old = (psutil.net_io_counters().bytes_recv + psutil.net_io_counters().bytes_sent)
    time.sleep(1)
    new = (psutil.net_io_counters().bytes_recv + psutil.net_io_counters().bytes_sent)
    return new - old

def get_total_file_size():
    files = get_files(DIRECTORY)
    size = 0
    for i in files:
        size += os.path.getsize(i)
    
    return size

def get_files(directory):
    files_ = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            files_.append(os.path.join(root, file))
    
    return files_

def send_stat(value):
    print (value)

def main():
    old_file_size = 0
    old_net_throughput = 0
    old_file_count = 0

    while True:
        current_file_size = get_total_file_size()
        current_file_count = len(get_files(DIRECTORY))
        current_net_throughput = 0

        file_count_change = current_file_count - old_file_count
        file_size_change = current_file_size - old_file_size

        for i in range(60):
            current_net_throughput += get_net_throughput()

        current_net_throughput /= 60
        current_net_throughput = round(current_net_throughput, 1)

        net_throughput_change = current_net_throughput - old_net_throughput

        print(get_time(), current_file_size, current_file_count, current_net_throughput, file_size_change, file_count_change, net_throughput_change, sep = ', ', file = csv)
        csv.flush()

        old_file_count = current_file_count
        old_net_throughput = current_net_throughput
        old_file_size = current_file_size 


main()