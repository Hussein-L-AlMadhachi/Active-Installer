#!/bin/sh

echo Using Linins 2021 version 0.1.0

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
if os.path.isfile(\"/usr/bin/linins\"):
    os.system(\"linins install\")
else:
    os.system(\"git clone https://github.com/Hussein-L-AlMadhachi/Linins.git; cd Linins ; sh install.sh ; linins install\")
" > install.py



python3 install.py || python install.py || python3.6 install.py ||  python3.7 install.py || python3.8 install.py ||  python3.9 install.py || py3 install.py || hy install.py

rm install.py
rm.install.sh

echo "[*] Installtion completed"
