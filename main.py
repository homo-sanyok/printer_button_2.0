import gpio
import time
import os
import shutil
import requests

def print_static():
    f = open('/home/klipper/printer_button/lastfile.txt', 'r')
    file = f.read()
    f.close()
    if file != '':
        requests.post(URL + '/printer/gcode/script?script=G28')
        requests.post(URL + '/printer/print/start?filename=' + file)

URL = 'http://127.0.0.1'

gpio.pinMode(16)
while not gpio.read(16):
    time.sleep(0.1)

clamp = gpio.wfi(16) < 3
if not clamp:
    requests.post(URL + '/printer/gcode/script?script=SET_LED LED=state_led RED=0.0 GREEN=1.0 BLUE=0.0 WHITE=1.0')
    requests.post(URL + '/printer/gcode/script?script=G91')
    requests.post(URL + '/printer/gcode/script?script=G0 Z5')
    requests.post(URL + '/printer/gcode/script?script=G28 X0 Y0')
    requests.post(URL + '/printer/gcode/script?script=G0 Y100')
    requests.post(URL + '/printer/gcode/script?script=G90')
    requests.post(URL + '/printer/print/cancel')
    os.system('systemctl start printer_button_timer.service')
else:
    status = requests.get(URL + '/printer/objects/query?print_stats').json()['result']['status']['print_stats']['state']
    print(status)
    if status == 'printing':
        requests.post(URL + '/printer/gcode/script?script=SET_LED LED=state_led RED=0.7 GREEN=0.2 BLUE=0.0 WHITE=1.0')
        requests.post(URL + '/printer/print/pause', timeout=1)
    elif status == 'paused':
        requests.post(URL + '/printer/gcode/script?script=SET_LED LED=state_led RED=0.0 GREEN=0.0 BLUE=0.5 WHITE=1.0')
        requests.post(URL + '/printer/print/resume', timeout=1)
    else:
        files = os.listdir("/media/usb/")
        requests.post(URL + '/printer/gcode/script?script=SET_LED LED=state_led RED=0.0 GREEN=0.0 BLUE=0.5 WHITE=1.0')
        if len(files) == 0:
            print_static()
        else:
            gcodeFiles = []
            for i in files:
                try:
                    if i.split('.')[1] == 'gcode':
                        gcodeFiles.append('/media/usb/' + i)
                except:
                    pass
            if len(gcodeFiles) != 0:
                gcodeFile = max(gcodeFiles, key=os.path.getctime)
                shutil.copyfile(gcodeFile, '/home/klipper/gcode_files/' + gcodeFile.split('/')[3])
                requests.post(URL + '/printer/print/start?filename=' + gcodeFile.split('/')[3], timeout=1) 
            else:
                static_print()
