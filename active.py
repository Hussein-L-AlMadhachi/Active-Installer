#!/usr/bin/env python3


import os
from os import chdir as cd
from sys import argv as args


import ParserLib



# some setup before running the rest of the program
SettingObj = ParserLib.SettingFile()


# main functionalities

#   install option
def install():
    SettingObj.load()
    if os.path.isfile( "InstallFile" ):
        ParserLib.InstallFile().execute( "InstallFile" )
    else:
        print("[!] No installation file")
        exit(0)

def debug():
    SettingObj.load()
    if os.path.isfile( "InstallFile" ):
        ParserLib.InstallFile().execute( "InstallFile", debug=True )
    else:
        print("[!] No installation files found here")
        exit(0)


#   clone option
def clone( url ):
    os.system(  "git clone " + url  )
    current_directory = os.getcwd()
    cd(   current_directory   +   "/"   +   url[  url.rindex( "/" )  :  url.rindex(".") ]   ) # change directory
    install()


#   setup option
def setup():
    global SettingObj
    SettingObj.setup()


def show_help():
    print("\nUsage:")
    print("    active help               show this help")
    print("    active version            show the version of Active installer")
    print("    active install            run the installtion scripts")
    print("    active debug              run the installtion scripts in debug mode (for developers)")
    print("    active clone [url]        clone a repository and install it")
    print("    active setup              setting up the program\n")
    exit(0)


# main program execution

print("Active Installer   Active 2023     version 0.2.1\n")



if len( args )  >  1:
    # install
    if  args[1] == "install":
        install()
    # debug
    elif  args[1] == "debug":
        debug()
    # clone
    elif  args[1] == "clone"  and  len(args) == 3:
        if  "/" in args[2]:
            clone( args[2] )
        else:
            print( "[!] invalid URL" )
    # setup
    elif args[1] == "setup":
        setup()
    # help
    elif args[1] == "help":
        show_help()
    # version
    elif args[1] == "version":
        exit(0)
    
    # invalid arguements
    else:
        show_help()
    exit(0)
        
else:
    show_help()
    exit(0)
