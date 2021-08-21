#!/bin/sh

echo Installing Active installer 2021 version 0.1.0

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


sudo mkdir /usr/src/active
sudo mkdir /etc/active

git clone https://github.com/Hussein-L-AlMadhachi/Active-Installer.git
cd Active-Installer


sudo cp ./active.py /usr/src/active
sudo cp ./ParserLib.py /usr/src/active
sudo chmod +x /usr/src/active/active.py

sudo touch /etc/active/SettingFile
lspci > HardwareInfo && sudo mv HardwareInfo /etc/active
rm HardwareInfo

sudo cp run.py /usr/bin/active
sudo chmod +x /usr/bin/active

echo "[*] Active Installer installtion is completed"
echo "\nif you have seen any problems report them at \n    https://github.com/Hussein-L-AlMadhachi/Active-Installer/issues\n"

sudo active setup

cd ..
rm -rf Active-Installer
