import subprocess
import time

def pinMode(pin, mode):
    res = bool(subprocess.call(['gpio', 'mode', str(pin), str(mode)]))
    if (not res) and mode == 'in': res = bool(subprocess.call(['gpio', 'pwm', str(pin), '500']))
    return not res

def read(pin):
    res = subprocess.check_output(['gpio', 'read', str(pin)], universal_newlines=True)
    res = not bool(int(res.replace('\n', '')))
    if res:
        time.sleep(0.1)
        res = subprocess.check_output(['gpio', 'read', str(pin)], universal_newlines=True)
        res = not bool(int(res.replace('\n', '')))
    return res

def wfi(pin):
    first_time = time.gmtime().tm_sec
    while read(16):
        time.sleep(0.1)
        read(16)
    second_time = time.gmtime().tm_sec
    if second_time < first_time: return 60 - abs(second_time - first_time - 1)
    return second_time - first_time