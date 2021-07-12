#!/bin/sh

echo Installing Linins 2021 version 0.1.0

echo "[o] Note: this requires root permission"

# git installation
sudo apt install git
sudo pacman -S git
sudo dnf install git
sudo yum install git
sudo emerge --ask dev-vcs/git
sudo pkg install git

# pciutils installation
sudo apt install pciutils
sudo emerge --ask sys-apps/pciutils
sudo emerge --ask sys-apps/hwids
sudo dnf install pciutils
sudo yum install pciutils
sudo pkg install pciutils
sudo apk add --upgrade pciutils-dev



mkdir ~/.Linins

git clone https://github.com/Hussein-L-AlMadhachi/Linins.git

cd Linins


cp ./linins.py ~/.Linins

cp ./ParserLib.py ~/.Linins


touch /etc/Linins/SettingFile

lspci > HardwareInfo && sudo mv HardwareInfo /etc/Linins

chmod +x ~/.Linins/linins.py

sudo mkdir /etc/Linins

sudo cp run.py /usr/bin/linins

echo "[*] Linins installtion is completed"
echo "\nif you have seen any problems report them at \n    https://github.com/Hussein-L-AlMadhachi/Linins/issues"

