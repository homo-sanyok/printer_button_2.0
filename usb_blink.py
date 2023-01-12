#!/usr/bin/env python3
import requests

URL = 'http://127.0.0.1'
status = requests.get(URL + '/printer/objects/query?print_stats').json()['result']['status']['print_stats']['state']

if status != 'printing' and status != 'paused':
    requests.post(URL + '/printer/gcode/script?script=SET_LED LED=state_led RED=0.0 GREEN=0.0 BLUE=0.5 WHITE=1.0')
    requests.post(URL + '/printer/gcode/script?script=G4 S1000')
    requests.post(URL + '/printer/gcode/script?script=SET_LED LED=state_led RED=0.0 GREEN=1.0 BLUE=0.0 WHITE=1.0')
    requests.post(URL + '/printer/gcode/script?script=G4 S1000')
    requests.post(URL + '/printer/gcode/script?script=SET_LED LED=state_led RED=0.0 GREEN=0.0 BLUE=0.5 WHITE=1.0')
    requests.post(URL + '/printer/gcode/script?script=G4 S1000')
    requests.post(URL + '/printer/gcode/script?script=SET_LED LED=state_led RED=0.0 GREEN=1.0 BLUE=0.0 WHITE=1.0')
    requests.post(URL + '/printer/gcode/script?script=G4 S1000')
    requests.post(URL + '/printer/gcode/script?script=SET_LED LED=state_led RED=0.0 GREEN=0.0 BLUE=0.5 WHITE=1.0')
    requests.post(URL + '/printer/gcode/script?script=G4 S1000')
    requests.post(URL + '/printer/gcode/script?script=SET_LED LED=state_led RED=0.0 GREEN=1.0 BLUE=0.0 WHITE=1.0')
