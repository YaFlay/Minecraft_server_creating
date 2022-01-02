from tkinter import messagebox
from os import chdir, getcwd, mkdir, remove, system, startfile, path, listdir, popen
from shutil import rmtree
from datetime import datetime, date
from urllib.request import urlopen, urlretrieve

def internet_button():
     try:
          urlopen("http://github.com")
          return True
     except IOError:
          messagebox.showerror(title='Internet', message='Internet don`t connected, function download core, java, python and backup don`t working.')
          return False

def time_user_def():
     datetimed = date.today()
     clock = datetime.today()
     time_user = 'Date today: '+ str(datetimed)+ ', time now '+str( clock.strftime('%H.%M.%S'))
     # take time, date and directory
     print(str(time_user))
     print('Starting to create a server!')
# User time
time_user_def()
def create_command():
     check_file = path.isdir('C:/minecraft')
     if   check_file == False:
          mkdir("C:/minecraft")
          chdir('C:\minecraft')
     else: 
          chdir('C:/minecraft')
     print('EULA text create...')
     # downloading server files in folder
     eula =  open('eula.txt', 'w+')
     eula_text = '''#Mojang EULA(https://account.mojang.com/documents/minecraft_eula).
# Time is not aviable
# Made by https://github.com/yaflay

eula=true
 '''
     eula.write(str(eula_text))
     eula.close()
     print('EULA text has been created!')
     print('Creating .bat file')
     bat = open('mine.bat', 'w+')
     bat_text = '''
java -Xmx1024M -Xms1024M -jar server.jar nogui
'''
     bat.write(str(bat_text))
     bat.close()
     # crate bat file and downloading jar core
     print('Created .bat file!')
     messagebox.showinfo('EULA', 'eula, bat and folser created! Press OK for leave')

def starting_server_button():  
     chdir('C:/minecraft')
     print('Downloading core...')
     url = 'https://launcher.mojang.com/v1/objects/a16d67e5807f57fc4e550299cf20226194497dc2/server.jar'
     urlretrieve(url, 'C:/minecraft/server.jar') 
     print('Core downloaded!')
     messagebox.showinfo('core downloaded', 'core created Press OK for leave')
#     first checkbox command

def server_properties_button():
     if internet_button():
          chdir('C:/minecraft')
          url_server_properties = 'https://raw.githubusercontent.com/YaFlay/Minecraft_server_creating/main/server_properties.py'
          urlretrieve(url_server_properties, 'C:/minecraft/server_properties.py')
          system('python3 C:/minecraft/server_properties.py')
          print('Creating server.properties')
          messagebox.showinfo('server.properties created', 'Minecraft server.properties created Press OK for leave')
          remove('C:/minecraft/server_properties.py')
          return True
     else: messagebox.showerror(title='Internet', message='Internet don`t connected')
# second checkbox command

def close_command_button():
     remove(str(__file__))
     remove(str(getcwd)+'index.py')
     remove(str(getcwd)+'windows.py')
     remove(str(getcwd)+'installer.py')
     messagebox.showinfo('file deleted', 'minecraft.exe closed and deleted! Press OK for leave')
#    deleting main file

def start():
     chdir('C:/minecraft')
     system('start mine.bat')
     messagebox.showinfo('Server_start', 'Server started! Press OK for leave')
#  starting server

def folder():
     startfile('C:/minecraft')
# start folder

def delete_directory():
          if path.isdir('C:/minecraft'):
                    chdir('C:/')
                    rmtree('C:/minecraft')
                    # delete directory with files
          else:
               print('Folder already deleted')
                    
def backup_button():
     if internet_button():
          if path.isdir('C:/minecraft/backup/'):
               chdir('C:/minecraft/backup')
          else: 
               mkdir('C:/minecraft/backup')
               chdir('C:/minecraft/backup')
          # create folder

          url_backup_text='https://raw.githubusercontent.com/YaFlay/Minecraft_server_creating/main/backup.py'
          if path.isfile('C:/minecraft/backup/backup.py'):
               remove('C:/minecraft/backup/backup.py')
          urlretrieve(url_backup_text, 'C:/minecraft/backup/backup.py')
          chdir('C:/minecraft/backup/')
          popen('python3 C:/minecraft/backup/backup.py')
          #  backuping minecraft files using python code from my github
     else: messagebox.showerror(title='Internet', message='Internet don`t connected')
# download python
# take def for checkboxes and buttons
