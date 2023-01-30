#!/usr/bin/python3

from crypt import methods
import subprocess
from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/get/list/ssid", methods=['GET'])
def send_list_ssid():
    connectedSsid = subprocess.check_output("nmcli -t d status | grep wlan0", shell=True).decode("utf-8").split(":")
    if connectedSsid[2] == "connected":
        connectedSsid = connectedSsid[3].split("\n")[0]
    else:
        connectedSsid = 0

    listWifi = subprocess.check_output("nmcli -t d wifi list", shell=True).decode("utf-8").split("\n")
    resListWifi = []
    for i in range(len(listWifi) - 2):
        ssid = listWifi[i].split(":")
        if ssid[7] != '':
            flag = False
            for i in resListWifi:
                if i == ssid[7]:
                    flag = True
            if not flag and connectedSsid != ssid[7]:
                resListWifi.append(ssid[7])
        else:
            flag = False
            for i in resListWifi:
                if i == ssid[8] or connectedSsid == ssid[8]:
                    flag = True
            if not flag and connectedSsid != ssid[8]:
                resListWifi.append(ssid[8])
    return jsonify({"connected": connectedSsid, "ssid":resListWifi})

@app.route("/connect", methods=["POST"])
def connect():
    ssid = request.args.get("ssid")
    password = request.args.get("password")
    try:
        connectRes = subprocess.check_output("nmcli -t d wifi connect '" + ssid + "' password '" + password + "'", shell=True).decode("utf-8")
        localIp = subprocess.check_output("ip route show | awk '{print $9}'", shell=True).decode('utf-8').split('\n')[3]
        return jsonify({"status": "1", "ip": localIp})
    except:
        return jsonify({"status": "0"})

@app.route("/get/local/ip", methods=["GET"])
def send_local_ip():
    localIp = subprocess.check_output("ip route show | awk '{print $9}'", shell=True).decode('utf-8').split('\n')[3]
    return jsonify({"ip": localIp})

@app.route("/get/password", methods=["GET"])
def send_password():
    return jsonify({"pass": "1234"})

if __name__ == "__main__":
    app.run(port=1234, host='0.0.0.0')
