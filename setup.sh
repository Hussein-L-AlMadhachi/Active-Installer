#!/bin/sh


echo "Installing Linins 2021 version 0.1.0"

echo "[o] Note: this requires root permission"

sudo mkdir /etc/Linins

sudo mkdir /usr/src/Linins

sudo cp ./linins.py /usr/src/Linins

sudo cp ./ParserLib.py /usr/src/Linins


sudo touch /etc/Linins/SettingFile

lspci > HardwareInfo && sudo mv HardwareInfo /etc/Linins

sudo chmod +x /usr/src/Linins/linins.py


sudo cp run.py /usr/bin/linins

sudo chmod +x /usr/bin/linins

echo "[*] Linins installtion is completed"
echo "\nif you have seen any problems report them at \n    https://github.com/Hussein-L-AlMadhachi/Linins/issues"

