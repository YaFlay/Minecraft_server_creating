# Made by https://github.com/yaflay
# This is create server on new version minecraft.
# if u dont use Python 3, dont use this. urllib dont working in Python2
# if u seek some bug, write me in Telegram: @YaFlay
# if u dont have C:/ disk, dont use this Python code, this crashed the code
# Version: 1.3.5!
# for free using with write link for my github.com
# if u dont want to write my link, send project in my Telegram: @bebra_YaFlay
import os 
import urllib.request
import datetime
import psutil
import time
import shutil
from PyQt5 import QtWidgets, uic
import sys
from urllib.request import urlopen, urlretrieve
from tkinter import *
from tkinter import Checkbutton
from tkinter import messagebox
# import modules

directory = os.getcwd()
os.chdir(str(directory))
minecraft_py = os.path.isfile('minecraft_server_installer.py')
if minecraft_py:
     minecraft_nam = str('minecraft_server_installer.py')
     with open('file_name.txt', 'w+') as file:
          file.write(str(minecraft_nam))
          file.close()
else:
     minecraft_nam = str('minecraft_server_installer.exe')
     file = open('file_name.txt', 'w+')
     file.write(str(minecraft_nam))
     file.close()
     print(minecraft_nam)
# creating file with backup text and with name python scripy
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
# 
# 
# 
print(' ')
def create_command():
     check_file = os.path.isdir('C:/minecraft')
     if   check_file == False:
          os.mkdir("C:/minecraft")
          os.chdir('C:\minecraft')
     else: 
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
     url_server_properties = 'https://raw.githubusercontent.com/YaFlay/Minecraft_server_creating/main/server_properties.py'
     urllib.request.urlretrieve(url_server_properties, 'C:/minecraft/server_properties.py')
     os.system('python3 C:/minecraft/server_properties.py')
     print('Creating server.properties')
     messagebox.showinfo('server.properties created', 'Minecraft server.properties created Press OK for leave')
     os.remove('C:/minecraft/server_properties.py')
     
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
     # take commands for checkboxes

def start():
     os.chdir('C:/minecraft')
     os.system('start mine.bat')
     messagebox.showinfo('Server_start', 'Server started!! Press OK for leave')
#  starting server

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
#  downloading x64 java
def delete_directory():
     os.chdir('C:/minecraft')
     if os.path.isfile('eula.txt'):
          os.remove('eula.txt')
     # deleting eula
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
#  deleting all files in C:/minecraft
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
     if os.path.isdir('C:/minecraft/backup/'):
          os.chdir('C:/minecraft/backup')
     else: 
          os.mkdir('C:/minecraft/backup')
          os.chdir('C:/minecraft/backup')
     # create folder

     url_backup_text='https://raw.githubusercontent.com/YaFlay/Minecraft_server_creating/main/backup.py'
     if os.path.isfile('C:/minecraft/backup/backup.py'):
          os.remove('C:/minecraft/backup/backup.py')
     urllib.request.urlretrieve(url_backup_text, 'C:/minecraft/backup/backup.py')
     os.system('python3 C:/minecraft/backup/backup.py')
     print('Minecraft back up started!')
     #  backuping minecraft files using python code from my github
def python_install():
     url = 'https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe'
     urllib.request.urlretrieve(url, 'C:/minecraft/python-3.10.0-amd64.exe')
     os.chdir('C:/minecraft/')
     os.startfile(r'C:/minecraft/python-3.10.0-amd64.exe')
     for process_python in psutil.process_iter():
          name_python = process_python.name()
          if name_python == 'python-3.10.0-amd64.exe':
                print('Wait...')
                time.sleep(30)
                print('And 10 sec more')
                time.sleep(10)
                named_64 = process_python.name()
                if not named_64 == 'python-3.10.0-amd64.exe':
                 process_python.kill()
                 print('Process has been eliminated!')
          pass
     pass
     os.remove('python-3.10.0-amd64.exe')
     messagebox.showinfo('Python','Python has been downloaded! Press ok for leave')
# download python
# take def for checkboxes and buttons



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
java_32.grid(column=1, row=11)
# java for x32
backup=Button(window, text='Backup minecraft-server files', command=backup_button)
backup.grid(column=1, row=12)
# Backup button
python_download=Button(window, text='Downloading Python with official site', command=python_install)
python_download.grid(column=0, row=12)
# downloading python
window.mainloop()
os.chdir(str(directory))
os.remove('file_name.txt')
# deleting dont`t usable file
# create window and button for start and create server

