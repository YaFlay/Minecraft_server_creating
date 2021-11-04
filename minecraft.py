# Made by https://github.com/yaflay
# This is create server on new version minecraft.
# if u dont use Python 3, dont use this. urllib dont working in Python2
# if u seek some bug, write me in Telegram: @YaFlay
# if u dont have C:/ disk, dont use this Python code, this crashed the code
import os
import urllib.request
import datetime
from urllib.request import urlopen
from tkinter import *
from tkinter import Checkbutton
from tkinter import messagebox
# import modules

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
date = datetime.date.today()
clock = datetime.datetime.today()
time = 'Date today: '+ str(date)+ ', time now '+str( clock.strftime('%H.%M.%S'))
# take time, date and directory

print(str(time))
print('Starting to create a server!')
# Give hor user time

# 
# 
# 
print(' ')
def create_command():
     print('Create minecraft folder!')
     check_file = os.path.exists('C:/minecraft')
     if   check_file == False:
          os.mkdir("C:/minecraft")
          os.chdir('C:\minecraft')
     else: os.chdir('C:/minecraft')

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
     messagebox.showinfo('EULA and folders create!', 'Press OK for leave')

def starting_server_button():  
     bat = open('mine.bat', 'w+')
     bat_text = '''
java -Xmx1024M -Xms1024M -jar server.jar
'''
     bat.write(str(bat_text))
     bat.close()
     # crate bat file and downloading jar core
     print('Create .bat file...')
     url = 'https://launcher.mojang.com/v1/objects/a16d67e5807f57fc4e550299cf20226194497dc2/server.jar'
     urllib.request.urlretrieve(url, 'C:/minecraft/server.jar') 
     messagebox.showinfo('.bat file and core created', 'Press OK for leave')

#     first checkbox command
def server_properties_button():
     server_properties = open('server.properties', 'w+')
     server_properties.write(str(server_text))
     print('Creating server.properties')
     messagebox.showinfo('Minecraft server.properties created', 'Press OK for leave')
     
     # second checkbox command
def close_command_button():

     os.chdir(str(directory))
     print(directory)
     py = open('minecraft.py', 'r')
     py.close()
     os.replace(str(directory)+'/minecraft.py', 'C:/minecraft/minecraft.py')
     os.chdir('C:/minecraft')
     messagebox.showinfo('minecraft.py closed and deleted!', 'Press OK for leave')
     # third checkbox command
def ok(): 
     window.destroy()
     window.quit()
     messagebox.showinfo('Window closed', 'Press OK for leave')
     # ok button
def start():
     os.chdir('C:/minecraft')
     os.startfile('mine.bat', 'open')
     os.startfile('server.properties', 'open')
     messagebox.showinfo('Server started!!', 'Press OK for leave')
#  start server button
# start code
def folder():
     os.startfile('C:/minecraft')
# open folder
# take def for checkboxes

window = Tk()
window.title('Minecraft server')
window.geometry('250x250')
# creating window
create_server = BooleanVar()  
create_server.set(True)
create_server=Checkbutton(window, text='1)Create server file amd folder', var=create_server, command=create_command)  
create_server.grid(column=0, row=1)
# 4rd checkbox
start_server = BooleanVar()  
start_server.set(True)  
start_server = Checkbutton(window, text='2)Create .bat file and downloading core', var=start_server, command=starting_server_button)  
start_server.grid(column=0, row=2) 
# first checkbox
server_properties = BooleanVar()  
server_properties.set(True)  
server_properties = Checkbutton(window, text='3) Create server.properties', var=server_properties, command=server_properties_button)  
server_properties.grid(column=0, row=3) 
# second checkbox
close_command = BooleanVar()  
close_command.set(True)  
close_command = Checkbutton(window, text='4) Close minecraft.py file', var=close_command, command=close_command_button)  
close_command.grid(column=0, row=4) 
# 
open_folder = BooleanVar()  
open_folder.set(True)  
open_folder = Checkbutton(window, text='Open minecraft server folder', var=close_command, command=folder)  
open_folder.grid(column=0, row=5) 
# third checkbox
button = Button(window, text='OK', command=ok)
button.grid(column=0, row=7)
starting_button = Button(window, text='Start server and open server.properties!', command=start)
starting_button.grid(column=0, row=6)

window.mainloop()
# create window and button for start server

