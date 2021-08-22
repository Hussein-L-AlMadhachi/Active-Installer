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

