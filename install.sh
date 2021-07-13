#!/bin/sh

echo Installing Linins 2021 version 0.1.0

echo "[o] Note: this requires root permission"
echo "[*] It is ok to see some errors"
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


sudo mkdir /usr/src/Linins
sudo mkdir /etc/Linins

git clone https://github.com/Hussein-L-AlMadhachi/Linins.git
cd Linins


sudo cp ./linins.py /usr/src
sudo cp ./ParserLib.py /usr/src
chmod +x /usr/src/linins.py

sudo touch /etc/Linins/SettingFile
lspci > HardwareInfo && sudo mv HardwareInfo /etc/Linins
rm HardwareInfo

sudo cp run.py /usr/bin/linins
sudo chmod +x /usr/bin/linins

echo "[*] Linins installtion is completed"
echo "\nif you have seen any problems report them at \n    https://github.com/Hussein-L-AlMadhachi/Linins/issues\n"

sudo linins setup
linins install

cd ..
rm -rf Linins
