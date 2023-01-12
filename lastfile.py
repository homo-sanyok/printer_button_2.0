import time
import requests

URL = 'http://127.0.0.1'

def read_file(last_file):
    try:
        file = ''
        with open('/home/klipper/printer_button/lastfile.txt', 'r') as out:
            file = out.read()
            out.close()
            return last_file == file
    except:
        read_file(last_file)

last_file = requests.get(URL + '/printer/objects/query?print_stats').json()['result']['status']['print_stats']['filename']

while read_file(last_file) or last_file == '':
    last_file = requests.get(URL + '/printer/objects/query?print_stats').json()['result']['status']['print_stats']['filename']

with open('/home/klipper/printer_button/lastfile.txt', 'w') as out:
    out.write(last_file)
    out.close()

time.sleep(20)