# Active installer
##### Active installer 2023 version 0.2.1 

Note: this project is no longer maintained and it has been replaced with [Rhenium](https://github.com/Hussein-L-AlMadhachi/Rhenium)

![The Active installer](https://raw.githubusercontent.com/Hussein-L-AlMadhachi/Active-Installer/main/ACTIVE.png) 

Active installer is an installer for compiling and installing source code and binaries with the ability to write scripts that runs when a specified operating systems or distribution exist, or when a particular hardware device or software exist on the users computers. this project aim to make an automated installation possible for Linux and also and few other operating systems

---

# Content
* Why to use this program
* How a regular user should use Active installer
* How to create an installer for your project with Active installer
* Final words

## Why to use this program

if you wanted to make an open source project one of the biggest challenges that you have to face, is that your users uses a wide range of hardware devices , operating systems and software. and if your users do not have the needed technical knowladge, they cannot compile the source code and install all the required dependencies to use your program. so the author of the project has to compile the source code and the binaries needed for each operating system and in some cases for some certain hardware devices or some certain software. that is why this program aims to solve this problem by providing you with the followings options to add to your shell scripts:

* You can specify a line of shell script to run only when the user is using a certain Linux distribution or a certain operating system
* You can specify a line of shell script to run when a certain hardware device exist (e.g GPU , network adaptors)
* You can specify a line of shell script to run when a certain software path exist (e.g GCC , Python , Nim , R)
* You can clone any other additionl repositories
* You can clone repositories that support Active installer Installation file's format "InstallFile" and install additional software that is specified in those repositories installtion files without worrying about how to install them when you writing your installtion files


Note: the same functionalities are available in [Rhenium](https://github.com/Hussein-L-AlMadhachi/Rhenium.git)

