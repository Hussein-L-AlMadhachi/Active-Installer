# Active source code installer
##### Active installer 2021 version 0.1.0

![The Active installer](https://raw.githubusercontent.com/Hussein-L-AlMadhachi/Active-Installer/main/ACTIVE.png)

Active installer is souce code installer for compiling and installing source code with the ability to write scripts that runs when a specified operating systems or distribution exist, or when a particular hardware device or software exist on the users computers. this project aim to make an automated installation possible for Linux and also other open source operating systems
---

# Content
* Why to use this program
* How a regular user should use Active installer
* How to create an installer for your project with Active installer
* Final words

## Why to use this program

if you wanted to make an open source project one of the biggest challenges that you have to face, is that your users uses a wide range of hardware devices , operating systems and software. and if your users do not have the needed technical knowladge, they cannot compile the source code and install all the required dependencies to use your program. so the author of the project has to compile the source code for each operating system and in some cases for some certain hardware devices or some certain software. that is why this program aims to solve this problem by providing you with the followings options to add to your shell scripts:


* You can specify a line of shell script to run only when the user is using a certain Linux distribution or a certain operating system
* You can specify a line of shell script to run when a certain hardware device exist (e.g GPU , network adaptors)
* You can specify a line of shell script to run when a certain software path exist (e.g GCC , Python , Nim , R)
* You can clone any other additionl repositories
* You can clone repositories that support Active installer Installation file's format "InstallFile" and install additional software that is specified in those repositories installtion files without worrying about how to install them when you writing your installtion files

## how a regular user should use Active installer

if you want to install a repository or source code that support Active installer installation file format `InstallFile` then to install Active installer do this:  

save this [script](https://raw.githubusercontent.com/Hussein-L-AlMadhachi/Active-Installer/main/install.sh) and run it
``` bash
user@machine:~$ sh install.sh
``` 

Now Active-Installer is ready. if you have the repository Git URL and that project supports Active installer, to download the repository and install it automatically write:

``` bash
user@machine:~$ active clone [URL]
```

or if you have the source code for a project and the project has Active installtion files `InstallFile` write:

``` bash
user@machine:~$ cd (path to the folder that contains 'InstallFile')

```

``` bash
user@machine:~$ active install
```
If you wanted to access and change Active installer settings write:
``` bash
user@machine:~$ sudo active settings
```
if you ran into any problems for example your files are deleted or Active installer is not functioning correctly then rerun the installtion script  
`sh install.sh` and it's okay to see some error messages

## How a developer who wants to create an installer and a compiler for his/her project should use this program

1. save this [script](https://raw.githubusercontent.com/Hussein-L-AlMadhachi/Active-Installer/main/install.sh) then run it
```
user@machine:~$ sh install.sh
```

2. create installation file script in a file called `InstallFile` which we will talk about how to write the script inside it in the next section

3. add [`active-installer.sh`](https://github.com/Hussein-L-AlMadhachi/Active-Installer/raw/main/active-installer.sh) to the same path that `InstallFile` is located

4. Now the user can use `active-installer.sh` to install Active installer and run your installation script automatically once your user run the installer, so you only need to notify the user that you support Active installation files so they can clone your repository using `active clone [your URL]`

# Creating Installation files
installation files are just a regular shell scripts and the only difference is that it contains some suffix and notations to specify when a line of script should run these suffix so first create a file called `InstallFile` then follow these instruction to write your script  

Active installer provides you five ways to write your installtion file's script:

## regular shell script
runs on any computer you should write it just like any regular shell script for example
```
echo "hello this is a computer that runs shell script"
```


## One distribution or one operating system specific script
runs only when the script runs on the specified distribution you should write it in this order
```
[disribution number] [script]
```
where the numbers for each disribution are:  
`1` for Arch Linux  
`2` for Fedora Linux  
`3` for OpenSUSE Linux  
`4` for CentOS  
`5` for Apline Linux  
`6` for Gentoo Linux  
`7` for BSD  
`8` for Debian Linux  
`9` for Ubuntu Linux  
for example:
```
5 echo "hello Alpine Linux user"
```

if you think we forgot some distributions or open source operating systems tell us in the [Discussions](https://github.com/Hussein-L-AlMadhachi/Active-Installer/discussions)


## A script specific for a gourp of distributions or operating systems
runs when the operating system that the user has is inside the the group 
```
{ [distribution number 1] , [distribution number 2] }  [script]
```
Note: space are tolerated inside `{}`



## Hardware specific script
runs when a hardware device exist you should first run this in your terminal:
```
user@machine:~$ lspci
... etc
0000:01:00.0 3D controller: NVIDIA Corporation GP107M [GeForce MX350] (rev a1)
... etc
```
let say that you want to your program to install dirvers for a NVIDIA graphics card and you want your script to run for this model `GeForce MX350` now to create an installtion script write this way
```
#[the keyword(s) inside the lspci command]: [script to run]
```
note that you should copy the words that you are looking for in the `lspci` command and place them between `#` and `:` and remmember that spaces between `#` and `:` counts as a part of the word that you are looking for.  
so your installation script going to be:
```
#GeForce MX350: echo "installing NVIDIA GeForce MX350 drivers"
```
or for example if you want your script to run for any Nvidia GPU then just change the keyword `GeForce MX350` to `NVIDIA`
```
#NVIDIA: echo "you are using Nvidia GPU"
```

## Software specific script
runs when the specified software path exist to write this you should know where the software that you are looking for is located for example some programs require to be ran only on python3.9

```
@[software path]: [script]
```
so the script for python3.9 inside the `InstallFile` should be:
```
@python3.9: echo "you are using Python version 3.9"
```
# Debug your installation script
to see how your script in executed you use
```
user@machine:~$ active debug
```
if the executed script was `#` that means that line of script is not executed either because of wrong script or the specific lines of script don't match with what you have (e.g Hardware device , Software path , Operating system) on your computer

# Final words
Have you seen any problem?  
Do you think there is something we forgot?  
Do you have some ideas about how to improve this program?  

Join our [Community discussions](https://github.com/Hussein-L-AlMadhachi/Active-Installer/discussions)  
Report an [Isseue](https://github.com/Hussein-L-AlMadhachi/Active-Installer/issues)
