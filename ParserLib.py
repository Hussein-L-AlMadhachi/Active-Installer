#/usr/bin/env python3

import os
import json



""" in SettingFile class"""
class SettingFile:
    def __init__( self ):
        self.SettingFile = "/etc/active/SettingFile.json"
        self.settings = {}
        self.valid_os_ids = [ "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "10" ]
        
        if not os.path.exists( "/etc/active/SettingFile.json" ):
            self.setup()
        else:
            self.load()

    def load( self ):
        file_descriptor = open( self.SettingFile , "r" )
        self.settings = json.loads(file_descriptor.read())
        file_descriptor.close()

    def save( self ):
        try:
            file_descriptor = open( self.SettingFile , "w" )
        except PermissionError:
            print( "[!] you must be root to do any changes to the settings" )
            exit(-1)
        file_descriptor.write( json.dumps( self.settings ) )
        file_descriptor.close()

    def setup( self ):
        print( "current settings:\n" )
        if self.settings != {}:
            print( "\tos :" , self.settings["os"] )
            choice = input( "\nDo you want to change the current options? [Y/N]  " )
            if choice.strip().lower() != "y":
                exit(0)
        else:
            print("setting active installer for the first time..\n\n")
        
        print( "What is the Linux disribution that you are using?" )
        print( "\t1)  Arch Linux" )
        print( "\t2)  Fedora Linux" )
        print( "\t3)  OpenSUSE Linux" )
        print( "\t4)  CentOS" )
        print( "\t5)  Apline Linux" )
        print( "\t6)  Gentoo Linux" )
        print( "\t7)  BSD" )
        print( "\t8)  Debian Linux" )
        print( "\t9))  Ubuntu Linux" )
        print( "\t10) Void Linux" )
        
        print( "\n\ttype 0 to exit" )

        choice = str(input( "your choice: " ))

        if choice.strip() in self.valid_os_ids:
            self.settings["os"] = choice.strip()
            self.save()
        else:
            print( "you have to choose on of the given numbers only" )
    def info( self ):
        print( self.settings )



from os import system


selectors = ["pci" , "path" , "file"]


class InstallFile:
    def __init__( self ):
        file_descriptor = open( "/etc/active/HardwareInfo" , "r" )
        self.info = file_descriptor.read()
        file_descriptor.close()


    def check_pci( self, device ):
        return  device in self.info

    def check_path( self , path ):
        return  os.path.exists( path )


    def parse( self , scriptline ):

        index = 0
        
        selector = ""
        params = ""
        should_execute = True

        if ("{" in scriptline):
            index = scriptline.index("{")
            selector = scriptline[ :index ].strip()
            if "not" in selector:
                should_execute = False
                selector = selector[:-3].strip()
            
            if not( selector in selectors):
                return "Wrong selector: it should be one of the following  pci , file , cpuinfo , software"
            
            if "}" in scriptline[index:]:
                params = scriptline[ index+1:scriptline.index("}") ]
                return {"selector":selector , "should-execute":should_execute , "params":params}
            else:
                return "you cannot leave {} open"
            
        else:
            return "you need to add to put your parameters inside {}"

    def should_exec( self ,  parse_params ):
        if parse_params["selector"] == "pci":
            if parse_params["should-execute"]:
                return self.check_pci( parse_params["params"] )
            else:
                return not self.check_pci( parse_params["params"] )

        elif parse_params["selector"] == "path":
            if parse_params["should-execute"]: 
                return self.check_path( parse_params["params"] )
            else:
                return not self.check_path( parse_params["params"] )
        else:
            print( "HOW THE HELL DO YOU GET HERE!!!" )



    def execute( self, filename , debug=False ):
        file_stream = open( filename , "r" )

        script = ""
        keep_going = False
        should_execute = True
        counter = 0
        
        for line in file_stream:
            counter += 1
            
            if line.strip() == "":
                continue

            if keep_going:
                if line.strip() == "end":
                    if debug:
                        if should_execute:
                            print( "\033[32m" , counter , "|  end \033[0m\n" )
                    keep_going = False

                elif should_execute:
                    if debug:
                        print(  counter , " |\texecuting:" , line )
                    system( line )
            else:
                p = self.parse( line )
                if type(p) == str:
                    print( counter , "|\t" , line )
                    print( "ERROR in line " , counter , ":  " ,p )
                    exit(-1)
                else:
                    should_execute = self.should_exec( p )
                    keep_going = True
                    if debug:
                        if should_execute:
                            if p["should-execute"]:
                                print( "\033[32m", counter , " |   the " , p["selector"] , p["params"] ," exist, execute this {\033[0m" )
                            else:
                                print( "\033[32m", counter , " |   the " , p["selector"] , p["params"] ,"does not exist , execute this {\033[0m" )
                        else:
                            if p["should-execute"]:
                                print( "\033[31m", counter , " |   the condition " , p["selector"] , p["params"] ," exist , was unmet\033[0m" )
                            else:
                                print( "\033[31m", counter , " |   the condition" , p["selector"] , p["params"] ,"does not exist , was unmet\033[0m" )
        file_stream.close()
