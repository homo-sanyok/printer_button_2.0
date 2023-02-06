import time
import requests

URL = 'http://127.0.0.1'

def read_file():
    file = ''
    with open('/home/klipper/printer_button/lastfile.txt', 'r') as out:
        file = out.read()
        out.close()
        return file

while True:
    try:
        moonraker_file = requests.get(URL + '/printer/objects/query?print_stats').json()['result']['status']['print_stats']['filename']
        lasfile_txt = read_file()
        if not moonraker_file == '':
            if not moonraker_file == lasfile_txt:
                with open('/home/klipper/printer_button/lastfile.txt', 'w') as out:
                    out.write(moonraker_file)
                    out.close()
        time.sleep(5)
    except:
        time.sleep(5)