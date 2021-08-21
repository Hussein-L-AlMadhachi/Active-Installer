#!/usr/bin/env python3


import os
from os import chdir as cd
from sys import argv as args


import ParserLib


# some setup before running the rest of the program
SettingObj = ParserLib.SettingFile()




# main functionalities

#   debug option
def debug():
    SettingObj.load()
    if os.path.isfile( "InstallFile" ):
        ParserLib.InstallFile().debug( "InstallFile" )
        os.system( "clear" )
    else:
        print("[!] No installation file")
        exit(0)

#   install option
def install():
    SettingObj.load()
    if os.path.isfile( "InstallFile" ):
        ParserLib.InstallFile().execute( "InstallFile" )
    else:
        print("[!] No installation file")
        exit(0)


#   clone option
def clone( url ):
    os.system(  "git clone " + url  )
    current_directory = os.getcwd()
    cd(   current_directory   +   "/"   +   url[  url.rindex( "/" )  :  url.rindex(".") ]   ) # change directory
    
    install()


#   setup option
def setup():
    settingObj = ParserLib.SettingFile()
    print( "What is the Linux disribution that you are using?" )
    print( "\t1)  Arch Linux" )
    print( "\t2)  Fedora Linux" )
    print( "\t3)  OpenSUSE Linux" )
    print( "\t4)  CentOS" )
    print( "\t5)  Apline Linux" )
    print( "\t6)  Gentoo Linux" )
    print( "\t7)  BSD" )
    print( "\t8)  Debian Linux" )
    print( "\t9)  Ubuntu Linux" )
    print( "\t10) Void Linux" )
        
    user_choice = input( "write the number of your choice: " )
    if user_choice in [ "1" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "10" ]:
        ParserLib.settings.update( { "Distribution" : user_choice } )
        settingObj.save()
        print( "[!] saved" )
    else:
        print( "invalid option" )


#   settings option
def start_settings_interface():
    options ="""
1) change distribution
2) Exit\n
"""
    print( options )
    user_choice = input( "choice >  " )
    
    settingObj = ParserLib.SettingFile()
    
    if user_choice == "1":
        print( "What is the Linux disribution that you are using?" )
        print( "\t1)  Arch Linux" )
        print( "\t2)  Fedora Linux" )
        print( "\t3)  OpenSUSE Linux" )
        print( "\t4)  CentOS" )
        print( "\t5)  Apline Linux" )
        print( "\t6)  Gentoo Linux" )
        print( "\t7)  BSD" )
        print( "\t8)  Debian Linux" )
        print( "\t9)  Ubuntu Linux" )
        print( "\t10) Void Linux")
        user_choice = input("write the number of your choice: ")
        
        
        valid_choices = [ "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "10"]
        
        if user_choice in valid_choices:
            ParserLib.settings[ "Distribution" ] = user_choice
            settingObj.save()
            print( "[*] saved" )
            exit(0)
        else:
            print( "[!] invalid option")
            exit(0)
        
    elif user_choice == "2":
        print( "[*] exited" )
        exit(0)
    
    else:
        print( "[!] invalid option" )




# main program execution

print("Active Installer   Active 2021     version 0.2\n")



if len( args )  >  1:
    # install
    if  args[1] == "install":
        install()
    # debug
    elif args[1] == "debug":
        debug()
    # clone
    elif  args[1] == "clone"  and  len(args) == 3:
        if  "/" in args[2]:
            clone( args[2] )
        else:
            print( "[!] invalid URL" )
    # settings
    elif args[1] == "settings":
        start_settings_interface()
    # setup
    elif args[1] == "setup":
        setup()
    # invalid arguements
    else:
        print("\nUsage:")
        print("    active install\t    run the installtion scripts")
        print("    active debug\t    debug the installtion scripts (for developers)")
        print("    active clone [url]\t    clone a repository and install it")
        print("    active setup\t    setting up the program")
        print("    active settings\t    to access program's settings")
        exit(0)

        
else:
    print("\nUsage:")
    print("    active install\t    run the installtion scripts")
    print("    active debug\t    debug an installtion file (for developers)")
    print("    active clone [url]\t    clone a repository and install it")
    print("    active setup\t    setting up the program")
    print("    active settings\t    to access program's settings")
    exit(0)
