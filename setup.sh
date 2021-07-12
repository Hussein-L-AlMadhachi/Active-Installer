#!/bin/sh


echo "Installing Linins 2021 version 0.1.0"

echo "[o] Note: this requires root permission"

mkdir ~/.Linins

cp ./linins.py ~/.Linins

cp ./ParserLib.py ~/.Linins


touch /etc/Linins/SettingFile

lspci > /etc/Linins/HardwareInfo

chmod +x ~/.Linins/linins.py

sudo cp run.py /usr/bin/linins

sudo chmod +x /usr/bin/linins

echo "[*] Linins installtion is completed"
echo "\nif you have seen any problems report them at \n    https://github.com/Hussein-L-AlMadhachi/Linins/issues"















