#/usr/bin/env python3

from os import system , path
import json

__version__ = "0.2.1"


""" in SettingFile class"""
class SettingFile:
    def __init__( self ):
        self.SettingFile = "/etc/active/SettingFile.json"
        self.settings = {}
        self.os_ids = {
            "1":"arch",
            "2":"fedora",
            "3":"opensuse",
            "4":"cent os",
            "5":"alpine",
            "6":"gentoo",
            "7":"freebsd",
            "8":"netbsd",
            "9":"openbsd",
            "10":"debian",
            "11":"ubuntu",
            "12":"void"
        }
        
        if not path.exists( "/etc/active/SettingFile.json" ):
            self.setup()
        else:
            self.load()
            if self.settings.get("version") != __version__:
                print( "[*] setting up Active Installer after updates..." )
                self.setup()

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
            print("[*] setting active installer for the first time...\n\n")
        
        print( "What is the Linux disribution that you are using?" )
        print( "\t1)   Arch Linux" )
        print( "\t2)   Fedora Linux" )
        print( "\t3)   OpenSUSE Linux" )
        print( "\t4)   CentOS" )
        print( "\t5)   Apline Linux" )
        print( "\t6)   Gentoo Linux" )
        print( "\t7)   FreeBSD" )
        print( "\t8)   NetBSD" )
        print( "\t9)   OpenBSD" )
        print( "\t10)  Debian Linux" )
        print( "\t11)  Ubuntu Linux" )
        print( "\t12)  Void Linux" )
        
        print( "\n\ttype 0 to exit" )

        choice = str(input( "your choice: " ))

        if choice.strip() in list(self.os_ids.keys()):
            self.settings["os"] = self.os_ids[choice.strip()]
            self.settings["version"] = __version__
            self.save()
        else:
            print( "you have to choose on of the given numbers only" )




class InstallFile:
    def __init__( self ):
        file_descriptor = open( "/etc/active/HardwareInfo" , "r" )
        self.info = file_descriptor.read()
        file_descriptor.close()
        settingObj = SettingFile()
        self.settings = settingObj.settings
        del settingObj
        self.selectors = ["pci" , "path" , "os"]


    def check_pci( self, device ):
        return  device in self.info

    def check_path( self , fsys_path ):
        return  path.exists( fsys_path )

    def check_os( self , os ):
        os = os.strip()
        return self.settings.get("os") == os

    def parse( self , scriptline ):

        index = 0
        
        selector = ""
        params = ""
        should_execute = True

        if scriptline.strip() == "exec":
            return {"selector": "exec", "should-execute":True , "params":None}

        elif ("{" in scriptline):
            index = scriptline.index("{")
            selector = scriptline[ :index ].strip()
            if "not" in selector:
                should_execute = False
                selector = selector[:-3].strip()
            
            if not( selector in self.selectors):
                return "\"" + selector + "\" is not a valid option. this can be only one of the followings: \"exec\" , \"pci\" , \"path\" or \"os\"."
            
            if "}" in scriptline[index:]:
                params = scriptline[ index+1:scriptline.index("}") ]
                if scriptline[ scriptline.index("}")+1: ].strip() != "":
                    return "unexpected token \""+scriptline[ scriptline.index("}")+1: ].strip()+"\" you shouldn't add anything after \"}\""
                return {"selector":selector , "should-execute":should_execute , "params":params}
            else:
                return "you should not leave {...} open"
            
        else:
            return "you need to add to put your parameters inside {...}"

    def should_exec( self ,  parse_params ):
        # PCI
        if parse_params["selector"] == "pci":
            if parse_params["should-execute"]:
                return self.check_pci( parse_params["params"] )
            else:
                return not self.check_pci( parse_params["params"] )

        # Path
        elif parse_params["selector"] == "path":
            if parse_params["should-execute"]: 
                return self.check_path( parse_params["params"] )
            else:
                return not self.check_path( parse_params["params"] )
        
        # OS
        elif parse_params["selector"] == "os":
            if parse_params["should-execute"]: 
                return self.check_os( parse_params["params"] )
            else:
                return not self.check_os( parse_params["params"] )

        # Execute
        elif parse_params["selector"] == "exec":
            return True
        else:
            print( "ERROR No.1: please report this error you should not see this if Active Installer is running as intended" )



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
            
            elif line.strip()[0] == "#":
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
                    print("\n\n \033[31mSYNTAX ERROR: the InstallFile is written incorrectly \033[0m")
                    print( "\033[33m [!] " , counter , "|\033[0m\t" , line[:-1] )
                    print( "\033[31m in line" , counter , "\033[0m: \033[33m" , p , "\033[0m" )
                    exit(-1)
                else:
                    should_execute = self.should_exec( p )
                    keep_going = True
                    if debug:
                        if p["selector"] == "exec":
                            print( "\033[32m", counter , " |   execute this \033[0m" ) 
                        elif should_execute:
                            if p["should-execute"]:
                                print( "\033[32m", counter , " |   the " , p["selector"] , p["params"] ," exist, execute this {\033[0m" )
                            else:
                                print( "\033[32m", counter , " |   the " , p["selector"] , p["params"] ,"does not exist , execute this\033[0m" )
                        else:
                            if p["should-execute"]:
                                print( "\033[36m", counter , " |   the condition " , p["selector"] , p["params"] ," exist was unmet\033[0m" )
                            else:
                                print( "\033[36m", counter , " |   the condition" , p["selector"] , p["params"] ,"does not exist was unmet\033[0m" )
        file_stream.close()
