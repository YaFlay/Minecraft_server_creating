# Made by https://github.com/yaflay
# This is create server on new version minecraft.
# if u dont use Python 3, dont use this. urllib dont working in Python2
# if u seek some bug, write me in Telegram: @YaFlay
# if u dont have C:/ disk, dont use this Python code, this crashed the code
# Version: 1.3.2!
import os
import urllib.request
import datetime
import psutil
import time
import shutil
from urllib.request import urlopen
from tkinter import *
from tkinter import Checkbutton
from tkinter import messagebox
# import modules

backup_text = '''
# Back up file
import os
import datetime
import time
import shutil
from tkinter import *
from tkinter import Checkbutton
from distutils.dir_util import copy_tree


if os.path.isdir('C:/backup-minecraft-server'):
    os.chdir('C:/minecraft/backup')
else:  
    dir = os.mkdir('C:/backup-minecraft-server/')
    os.chdir(str(dir))

date1 = datetime.date.today()
clock = datetime.datetime.today
a = open('logs-'+str(date1)+'.txt', 'w+')
folder1 = 'C:/minecraft/'
folder2 = 'C:/backup-minecraft-server'
text_for_log = 'Folder or file '+ str(folder1)+'  copied to '+str(folder2)+'. Date on this moment: '+ str(date1) +'. Time on this moment: '+str( clock('%H.%M.%S'))+'File:'


def log_button():
    directory = ('C:/backup-minecraft-server/world'+str(date1))
    if os.path.isdir(str(directory)):
        print(directory)
    else: os.mkdir(str(directory))

    for folder_name in os.listdir('C:/minecraft/',):
     path = 'C:/minecraft/' + folder_name
    for folder_name in os.listdir(path):
       copy_tree(path, str(directory))
    a = open('logs-'+str(date1)+'.txt', 'w+')
    a.write(
        str(text_for_log)+'World folder'
    )
    a.close()


window = Tk()
window.title('Minecraft backup')
window.geometry('500x300') #500/\, 250>
# creating window
log = BooleanVar()  
log.set(True)
log=Checkbutton(window, text='World folder copyed', var=log, command=log_button)  
log.grid(column=1, row=1)




window.mainloop()

'''
# backup.py text
server_text = '''#Minecraft server properties
#Time dont aviable

broadcast-rcon-to-ops=true
view-distance=10
enable-jmx-monitoring=false
server-ip=
resource-pack-prompt=
rcon.port=25575
gamemode=survival
server-port=25565
allow-nether=true
enable-command-block=false
enable-rcon=false
sync-chunk-writes=true
enable-query=false
op-permission-level=4
prevent-proxy-connections=false
resource-pack=
entity-broadcast-range-percentage=100
level-name=world
rcon.password=
player-idle-timeout=0
motd=A Minecraft Server
query.port=25565
force-gamemode=false
rate-limit=0
hardcore=false
white-list=false
broadcast-console-to-ops=true
pvp=true
spawn-npcs=true
spawn-animals=true
snooper-enabled=true
difficulty=easy
function-permission-level=2
network-compression-threshold=256
text-filtering-config=
require-resource-pack=false
spawn-monsters=true
max-tick-time=60000
enforce-whitelist=false
use-native-transport=true
max-players=20
resource-pack-sha1=
spawn-protection=16
online-mode=true
enable-status=true
allow-flight=false
max-world-size=29999984
'''
# This is minecraft properties file

directory = os.getcwd()
print(directory)
os.chdir(str(directory))
minecraft_py = os.path.isfile('minecraft_server_installer.py')
if minecraft_py:
     minecraft_nam = str('minecraft_server_installer.py')
     file = open('file_name.txt', 'w+')
     file.write(str(minecraft_nam))
     file.close()
else:
     minecraft_nam = str('minecraft_server_installer.exe')
     file = open('file_name.txt', 'w+')
     file.write(str(minecraft_nam))
     file.close()
     print(minecraft_nam)
# creating file 
file = open('file_name.txt', 'r')
minecraft_name = str(file.read())
file.close()
print(minecraft_name)
date = datetime.date.today()
clock = datetime.datetime.today()
time_user = 'Date today: '+ str(date)+ ', time now '+str( clock.strftime('%H.%M.%S'))
# take time, date and directory

print(str(time_user))
print('Starting to create a server!')
# Give hor user time
# if directory in [G:/, D:/, F:/]:
check_file = os.path.exists('C:/minecraft')
if   check_file == False:
     os.mkdir("C:/minecraft")
     os.chdir('C:\minecraft')
else: os.chdir('C:/minecraft')
# 
# 
# 
print(' ')
def create_command():
     os.chdir('C:/minecraft')
     print('Create minecraft folder!')
     print('Create Minecraft server folder...')
     print('EULA text create!')
     # downloading server files in folder
     eula =  open('eula.txt', 'w+')
     eula_text = '''#Mojang EULA(https://account.mojang.com/documents/minecraft_eula).
# Time is not aviable
# Made by https://github.com/yaflay

eula=true
 '''
     eula.write(str(eula_text))
     eula.close()
     print('EULA text has been created...')
     #  creating EULA text, and write in eula.txt
     # this is 4rd checkbox
     messagebox.showinfo('EULA', 'EULA and folders create! Press OK for leave')

def starting_server_button():  
     os.chdir('C:/minecraft')
     print('Creating .bat file')
     bat = open('mine.bat', 'w+')
     bat_text = '''
java -Xmx1024M -Xms1024M -jar server.jar nogui
'''
     bat.write(str(bat_text))
     bat.close()
     # crate bat file and downloading jar core
     print('Create .bat file!')
     print('Downloading core...')
     url = 'https://launcher.mojang.com/v1/objects/a16d67e5807f57fc4e550299cf20226194497dc2/server.jar'
     urllib.request.urlretrieve(url, 'C:/minecraft/server.jar') 
     print('Core downloaded!')
     messagebox.showinfo('bat file created', '.bat file and core created Press OK for leave')

#     first checkbox command
def server_properties_button():
     os.chdir('C:/minecraft')
     server_properties = open('server.properties', 'w+')
     server_properties.write(str(server_text))
     print('Creating server.properties')
     messagebox.showinfo('server.properties created', 'Minecraft server.properties created Press OK for leave')
     
     # second checkbox command
def close_command_button():
     os.chdir(str(directory))
     print('Your directory'+directory)
     py = open(str(minecraft_name), 'r')
     py.close()
     if directory in [ 'G:/, D:/, F:/' ]:
          os.replace(str(directory)+str(minecraft_name), 'C:/minecraft/'+str(minecraft_name))
          os.chdir('C:/minecraft')
     else:
          print(' ')
     os.replace(str(directory)+'/'+str(minecraft_name), 'C:/minecraft/'+str(minecraft_name))
     os.chdir('C:/minecraft')
     messagebox.showinfo('file deleted', 'minecraft.exe closed and deleted! Press OK for leave')
     # third checkbox command
def ok(): 
     window.destroy()
     window.quit()
     messagebox.showinfo('Close', 'Window closed Press OK for leave')
     # take commands for checkboxes
def start():
     os.chdir('C:/minecraft')
     os.startfile('mine.bat', 'open')
     os.startfile('server.properties', 'open')
     messagebox.showinfo('Server_start', 'Server started!! Press OK for leave')

# start code
def folder():
     os.startfile('C:/minecraft')
     # start folder

def java_windows():
     java='https://javadl.oracle.com/webapps/download/AutoDL?BundleId=245476_4d5417147a92418ea8b615e228bb6935'
     urllib.request.urlretrieve(java, 'C:/minecraft/jre-8u311-windows-i586-iftw.exe')
     os.chdir('C:/minecraft')
     os.startfile(r'C:/minecraft/jre-8u311-windows-i586-iftw.exe')
     for proce in psutil.process_iter():
          name = proce.name()
          if name == 'jre-8u311-windows-i586-iftw.exe':
                print('Wait...')
                time.sleep(30)
                named = proce.name()
                if not named == 'jre-8u311-windows-i586-iftw.exe':
                 proce.kill()
                 os.remove('jre-8u311-windows-i586-iftw.exe')
                 print('Process has been eliminated!')
               #   if programm is closed, passing this part
          pass
     pass
     os.remove('jre-8u311-windows-i586-iftw.exe')
     messagebox.showinfo('Java_32', 'Java has been downloaded! Press ok for leave')
               
     # for downloading java 8u311 for windows

def java_windows_64():
     java_64='https://javadl.oracle.com/webapps/download/AutoDL?BundleId=245469_4d5417147a92418ea8b615e228bb6935'
     urllib.request.urlretrieve(java_64, 'C:/minecraft/jre-8u311-windows-x64.exe')
     os.chdir('C:/minecraft/')
     os.startfile(r'C:/minecraft/jre-8u311-windows-x64.exe')
     for proce_64 in psutil.process_iter():
          name_64 = proce_64.name()
          if name_64 == 'jre-8u311-windows-x64.exe':
                print('Wait...')
                time.sleep(30)
                named_64 = proce_64.name()
                if not named_64 == 'jre-8u311-windows-x64.exe':
                 proce_64.kill()
                 print('Process has been eliminated!')
          pass
     pass
     os.remove('jre-8u311-windows-x64.exe')
     messagebox.showinfo('Java_64','Java has been downloaded! Press ok for leave')

def delete_directory():
     os.chdir('C:/minecraft')
     if os.path.isfile('eula.txt'):
          os.remove('eula.txt')
     # deleting eula
     pass
     if os.path.isfile('mine.bat'):
          os.remove('mine.bat')
     # deleting .bat file
     if os.path.isfile('server.jar'):
          os.remove('server.jar')
     # deleting core
     if os.path.isfile('server.properties'):
          os.remove('server.properties')
     # deleting server.properties
     if os.path.isfile('banned-ips.json'):
          os.remove('banned-ips.json')
          # deleting banned-ips.json
     if os.path.isfile('banned-players.json'):
          os.remove('banned-players.json')
          # deleting banned-players.json
     if os.path.isfile('ops.json'):
          os.remove('ops.json')
          # deleting ops.json
     if os.path.isfile('usercache.json'):
          os.remove('usercache.json')
          # deleting ops.json
     if os.path.isfile('whitelist.json'):
          os.remove('whitelist.json')
          # deleting whitelist.json

     minecraft_files = os.path.isfile(minecraft_name)
     if minecraft_files:
          minecraft_exe = open(minecraft_name)
          minecraft_exe.close()
          os.remove(minecraft_name)
          print('File deleted')
     else:
          print('File dont created')
          # checking and deleting file
     directory_file = os.listdir()
     print(directory_file)
     if directory_file == ['logs', 'world']:
          os.chdir('C:/')
          shutil.rmtree('C:/minecraft')
     else:
          os.chdir('C:/')
          shutil.rmtree('C:/minecraft')
          # delete directory with files
          
def backup_button():
     if os.path.isdir('C:/minecraft/backup/') == True:
          os.chdir('C:/minecraft/backup')
     else: 
          os.mkdir('C:/minecraft/backup')
          os.chdir('C:/minecraft/backup')
     # create folder
     if os.path.isfile('C:/minecraft/backup/backup.py'):
          os.startfile('backup.py')
     else:
          back_up = open('backup.py', 'w+')
          back_up.write(str(backup_text))
          os.startfile('backup.py', '')
     
     

# open folder
# take def for checkboxes

window = Tk()
window.title('Minecraft server')
window.geometry('500x300') #500/\, 250>
# creating window
create_server = BooleanVar()  
create_server.set(True)
create_server=Checkbutton(window, text='1)Create server file amd folder', var=create_server, command=create_command)  
create_server.grid(column=1, row=1)
# 4rd checkbox
start_server = BooleanVar()  
start_server.set(True)  
start_server = Checkbutton(window, text='2)Create .bat file and downloading core', var=start_server, command=starting_server_button)  
start_server.grid(column=1, row=2) 
# first checkbox
server_properties = BooleanVar()  
server_properties.set(True)  
server_properties = Checkbutton(window, text='3) Create server.properties', var=server_properties, command=server_properties_button)  
server_properties.grid(column=1, row=3) 
# second checkbox
close_command = BooleanVar()  
close_command.set(True)  
close_command = Checkbutton(window, text='4) Close minecraft.py file', var=close_command, command=close_command_button)  
close_command.grid(column=1, row=4) 
# replace minecraft.py command
open_folder = BooleanVar()  
open_folder.set(True)  
open_folder = Checkbutton(window, text='Open minecraft server folder', var=close_command, command=folder)  
open_folder.grid(column=1, row=5) 
# third checkbox
button = Button(window, text='OK', command=ok)
button.grid(column=1, row=7)
# close program button
starting_button = Button(window, text='Start server and open server.properties!', command=start)
starting_button.grid(column=1, row=6)
# starting server button
delete_button=Button(window, text='Delete folder and files', command=delete_directory)
delete_button.grid(column=1, row=10)
# delete folder button
java_64=Button(window, text='Downloading Java for x64', command=java_windows_64)
java_64.grid(column=0, row=11)
# java for x64
java_32=Button(window, text='Downloading Java for x32', command=java_windows)
java_32.grid(column=2, row=11)
# java for x32
backup=Button(window, text='Backup server', command=backup_button)
backup.grid(column=1, row=12)

window.mainloop()
os.chdir(str(directory))
os.remove('file_name.txt')
# create window and button for start server

