sudo rm -r /home/klipper/poweroff_btn
sudo rm -r /home/klipper/usb_mount
sudo rm -r /etc/systemd/system/usb-mount.service
sudo apt update
sudo apt install python3 python3-pip usbmount -y
sudo pip3 install subprocess.run requests flask flask-cors subprocess.run sh
cd ~
git clone https://github.com/orangepi-xunlong/wiringOP.git
cd wiringOP
sudo ./build clean
sudo ./build
sudo cp /home/klipper/printer_button/services/*.service /etc/systemd/system/
sudo cp /home/klipper/printer_button/wifi_settings/services/*.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable printer_button_main.service
sudo systemctl enable printer_button_lastfile.service
sudo systemctl enable wifi-settings-rest.service
sudo systemctl start printer_button_main.service
sudo systemctl start printer_button_lastfile.service
sudo systemctl start wifi-settings-rest.service
sudo cp /home/klipper/printer_button/services/10-local.rules /etc/udev/rules.d/
sudo rm /etc/nginx/sites-enabled/fluidd
sudo mv /home/klipper/printer_button/wifi_settings/fluidd /etc/nginx/sites-enabled/
sudo systemctl restart nginx
sudo service udev reload
sudo service udev restart
mv /home/klipper/moonraker/.git /home/klipper/moonraker/.git_
mv /home/klipper/moonraker/.github /home/klipper/moonraker/.github_
