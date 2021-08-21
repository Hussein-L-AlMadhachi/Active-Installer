#!/bin/sh

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
