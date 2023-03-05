#!/bin/sh


echo "Installing Active installer 2021 version 0.1.0"

echo "[o] Note: this requires root permission"

sudo mkdir /etc/active

sudo mkdir /usr/src/active

sudo cp ./active.py /usr/src/active

sudo cp ./ParserLib.py /usr/src/active


sudo touch /etc/active/SettingFile

lspci > HardwareInfo && sudo mv HardwareInfo /etc/active

sudo chmod +x /usr/src/active/linins.py


sudo cp run.py /usr/bin/active

sudo chmod +x /usr/bin/active

echo "[*] Active installer installtion is completed"
echo "\nif you have seen any problems report them at \n    https://github.com/Hussein-L-AlMadhachi/Active-Installer/issues"

