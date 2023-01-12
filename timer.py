import time
import requests

URL = 'http://127.0.0.1'

time.sleep(180)
status = requests.get(URL + '/printer/objects/query?print_stats').json()['result']['status']['print_stats']['state']
if not (status == 'printing') and not (status == 'paused'):
    requests.post(URL + '/printer/gcode/script?script=M107')
    requests.post(URL + '/printer/gcode/script?script=G1 Z0')

