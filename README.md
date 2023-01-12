# Установка
### Требования к установке
1. Наличие интернет соединение у принтера
2. Подключённая в нужные пины к плате кнопка

    
![Alt-текст](https://www.google.com/url?sa=i&url=http%3A%2F%2Fwww.orangepi.org%2Fhtml%2FhardWare%2FcomputerAndMicrocontrollers%2Fdetails%2FOrange-Pi-Zero-2.html&psig=AOvVaw2JqzcJbxDUkf5wOo2RIiSt&ust=1673621731769000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCKCMtPikwvwCFQAAAAAdAAAAABAE)
    * PC10
    * GND

### Инструкция по установке
1. Скачайте скрипт
```
cd /home/klipper
git clone https://github.com/homo-sanyok/printer_button_2.0.git
```
2. Перейдите в папку со скриптом и запустите установку
```
mv printer_button_2.0 printer_button
cd printer_button
sudo ./install.sh
```
