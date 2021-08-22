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

echo Using Active installer 2021 version 0.1.0

echo "[o] Note: this may require root permission"
echo "[*] It is ok to see some errors"
# git installation
sudo apt install git
sudo pacman -S git
sudo dnf install git
sudo yum install git
sudo emerge --ask dev-vcs/git
sudo pkg install git



echo "
import os
if os.path.isfile(\"/usr/bin/active\"):
    os.system(\"active install\")
else:
    os.system(\"git clone https://github.com/Hussein-L-AlMadhachi/Active-Installer.git; cd Active-Installer ; sh install.sh ; active install\")
" > install.py



python3 install.py || python install.py || python3.6 install.py ||  python3.7 install.py || python3.8 install.py ||  python3.9 install.py || py3 install.py || hy install.py

rm install.py
rm.install.sh

echo "[*] Installtion completed"
