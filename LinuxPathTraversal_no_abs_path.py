class Linuxpt:

    def mod_cwd(self,cwd=['root']):
        """changes the current working directory. By default will be at root"""
        self.cwd=cwd

    def get_cwd(self):
        """Returns the current working directory"""
        return self.cwd


    def create_dir(self,FileManager,list_of_dirs):
        """Creates a directory when the Nested Dictionary and new directory are passed to it"""
        eString='FileManager'
        echeckString='FileManager'
        for d in list_of_dirs[:len(list_of_dirs)-1]:
            echeckString=echeckString+"['"+d+"']"
        check=[]
        echeckString='check.append(list_of_dirs[len(list_of_dirs)-1] in '+ echeckString +'.keys())'
        try:
            exec(echeckString)
            if check[0]==True:
                print ('ERR: DIRECTORY ALREADY EXISTS')
                return FileManager
            for d in list_of_dirs:
                eString=eString+"['"+d+"']"
            eString=eString+'={}'
            exec(eString)
            print('SUCC: CREATED')
            return FileManager
        except(KeyError):
            print('ERR: INVALID PATH')
            return FileManager


    def create_dir2(self,FileManager,pwd,new_folder):
        eString='FileManager'
        list_of_dir=[]
        for d in pwd:
            list_of_dir.append(d)
        for d in list_of_dir:
                eString=eString+"['"+d+"']"
        eString=eString+"['"+new_folder[0]+"']={}"
        print(eString)
        try:
            exec(eString)
            print('SUCC: CREATED')
            return FileManager
        except(KeyError):
            print('ERR: INVALID PATH')
            return FileManager


    

    

    def change_dir(self,FileManager, list_of_dirs):
        """Changes the directory when the Nested Dictionary and required directory are passed to it """
        eString='FileManager'
        for d in list_of_dirs:
            eString=eString+"['"+d+"']"
        try:
            exec(eString)
            self.mod_cwd(list_of_dirs)
            print('SUCC: REACHED')
        except (KeyError):
            print('ERR: INVALID PATH')


    def dir_list(self, FileManager, pwd):
        """Prints the list of folders under present directory"""
        eString='FileManager'
        for d in pwd:
            eString=eString+"['"+d+"']"
        list_of_folders=[]
        eString='list_of_folders.append(str('+eString+'.keys()))'
        try:
            exec(eString)
            if(list_of_folders[0]!='dict_keys([])'):
                print('DIRS: ',end='')
                print (list_of_folders[0].replace("dict_keys([",'').replace("'",'').replace("])",'').replace(",",''))
        except (KeyError):
            print('ERR: INVALID PATH')    


    def remove_dir(self, FileManager, list_of_dir):
        """Removes the directory when the Nested Dictionary and directory to be removed are passed to it """
        eString='FileManager'
        for d in list_of_dirs:
            eString=eString+"['"+d+"']"
        eString='del '+eString
        try:
            exec(eString)
            list_for_mod_cwd=[]
            for d in list_of_dirs[0:len(list_of_dirs)-1]:
                list_for_mod_cwd.append(d)
            self.mod_cwd(list_for_mod_cwd)
            print('SUCC: DELETED')
        except KeyError:
            print('ERR: INVALID PATH')
        

#Set of rules to follow while defining a directory. 
def rules():
    print('\nPlease stick to the below rules:')
    print('1. Please use "/" and not this "\\" for paths and also start your path with "/".  Eg:/root/your/path')
    print('2. Please provide full path for the commands mkdir, cd and rm and not just the folder name.  Eg: /root/dir1/dir2')
    print('3. Dont put "/" at the end of the path.\n')


print('Help:\n')
print('1.pwd - displays present working directory. By default it will be at root/ \n')
print('2.ls - displays list of folders in present directory\n')
print('3.rm - removes given directory\n')
print('4.mkdir - creates a directory and changes your present directory to the newly created directory\n')
print('5.cd - changes your present working directory\n')
print('6.session clear - resets the application\n')
print('7.exit - to exit the application\n')
print('8.Please use this "/" and not this "\\" while providing a path (Eg: /give/like/this)\n')
print('9.For commands mkdir,rm,cd, always provide full path from the "/root", along with the command (Eg: mkdir /root/full/path )\n')
print('-------------------------------------------------------------------------------\n\n')


FileManager = {'root':{}}
o=Linuxpt()
o.mod_cwd()
command=input("$")

#While loop for keep the session running untill exit command is given. If loops inside while are to choose the appropriate function based on given command
#If loops that check for mkdir, cd and rm commands, break the given directory(Eg: /root/folder1) into a list of strings (['root','folder'])...
#...to enable easy nested dictionary operations

while(command!='exit'):

    if command=='pwd':
        print(end='PATH: ')
        for i in (o.get_cwd()):
            print(i,end="/")
        command=input("\n$")

    #elif command[0:5]=='mkdir':
        #if command[len(command)-1]!='/' and command[6:11]=='/root':
            #list_of_dirs=command.split('/')
            #list_of_dirs.pop(0)
            #FileManager = o.create_dir(FileManager,list_of_dirs)

    elif command[0:5]=='mkdir':
        pwd=o.get_cwd()
        new_folder=command.split()
        print(pwd)
        print(new_folder)
        new_folder.pop(0)
        o.create_dir2(FileManager,pwd,new_folder)
        command=input("$")
    #else:
        #rules()
    #command=input("$")

    elif command[0:2]=='cd':
        if command[len(command)-1]!='/' and command[3:8]=='/root':
            list_of_dirs=command.split('/')
            list_of_dirs.pop(0)
            o.change_dir(FileManager,list_of_dirs)
        else:
            rules()
        command=input("$")

    elif command=='ls':
        pwd=o.get_cwd()
        o.dir_list(FileManager, pwd)
        command=input("$")

    elif command[0:2]=='rm':
        if command[len(command)-1]!='/' and command[3:8]=='/root':
            list_of_dirs=command.split('/')
            list_of_dirs.pop(0)
            o.remove_dir(FileManager,list_of_dirs)
        else:
            rules()
        command=input("$")

    elif command=='session clear':
        FileManager={'root':{}}
        o.mod_cwd()
        print('SUCC: CLEARED: RESET TO ROOT')
        command=input("$")

    else:
        print('ERR: CANNOT RECOGNIZE INPUT.')
        command=input("$")


