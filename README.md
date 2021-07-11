# Linins source installer
##### Linins 2021 version 0.1.0 

![The Linins Project](https://raw.githubusercontent.com/Hussein-L-AlMadhachi/Linins/main/Linins_logo.png)

Linins is souce code installer for compiling and installing source code with the ability to write scripts that runs when a specified operating systems or distribution exist, or when a particular hardware device or software exist on the users computers. this project aim to make an automated installation possible primarly for Linux and also other open source operating systems
---
___
###### Note: there is another project that has the same name and the the same source code in some parts uploaded by HusseinL-Almadhachi which is my account but I lost both the the account and the recovery email. so that project IS NOT UNDER ACTIVE DEVELOPMENT you might face strange bugs and compatibilty issues with that project
___

## Introduction

if you wanted to make an open source project one of the biggest challenges that you have to face, is that your users uses a wide range of hardware devices , operating systems and software. and if your users do not have the needed technical knowladge, they cannot compile the source code and install all the required dependencies to use the program. so the author of the project has to compile the source code for each operating system and in some cases for some certain hardware devices or some certain software. that is why this program aims to solve this problem by providing you with the followings options to add to your shell scripts:


* You can specify a line of shell script to run only when the user is using a certain Linux distribution or a certain operating system
* You can specify a line of shell script to run when a certain hardware device exist (e.g GPU , network adaptors)
* You can specify a line of shell script to run when a certain software path exist (e.g GCC , Python , Nim , R)
* You can clone any other additionl repositories
* You can clone repositories that support Linins Installation file's format "InstallFile" and install additional software that is specified in those repositories installtion files without worrying about how to install them when you writing your installtion files

## how a user should install ansd use this
* run this [script](https://raw.githubusercontent.com/Hussein-L-AlMadhachi/Linins/main/setup.sh)
``` shell
user@machine:~$ chmod +x setup.sh && ./setup.sh
```

* write the following in your shell then select your operating system:
``` shell
user@machine:~$ linins setup
```

* now Linins is ready so if want to download a repository then inside its directory run:

Note: the repository here is only an examle of any reposiotry 

``` shell
user@machine:~$ git clone https://github.com/Hussein-L-AlMadhachi/Linins.git


user@machine:~$ cd Linins


user@machine:~$ linins install


```
