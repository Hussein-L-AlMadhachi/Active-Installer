#!/bin/sh

<<com

Active source code installer
Copyright (C) 2021  Hussein Layth Al-Madhachi

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License 
as published by the Free Software Foundation, version 2


This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA

com

echo Installing Active installer 2021 version 0.1.2

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
