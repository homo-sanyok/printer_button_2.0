# Установка
### Требования к установке
1. Наличие интернет соединение у принтера
2. Подключённая в нужные пины к плате кнопка

    ![Alt-текст](http://www.orangepi.org/img/computersAndMmicrocontrollers/Zero%202/Rectangle%20741.png)
    * TWI1-SCK/PA18
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
