# Back up file
# backup code for github.com/yaflay
# for free using and add link for my github.com
import os
import datetime
import time
import shutil
from shutil import copyfile
from time import strftime
from tkinter import *
from tkinter import Checkbutton
from distutils.dir_util import copy_tree
import requests
# import modules


p = os.getcwd()
print(p)
ext_ip = requests.get('https://checkip.amazonaws.com').text.strip()
print ( ext_ip)
ip = open('my_ip.txt', 'w+')
ip.write(str(ext_ip))
ip.close()
# take ip 

if os.path.isdir('C:/backup-minecraft-server'):
    os.chdir('C:/minecraft/backup')
else:  
    os.mkdir('C:/backup-minecraft-server/')
    os.chdir('C:/backup-minecraft-server/')

date1 = datetime.date.today()
clock = datetime.datetime.today
a = open('logs-'+str(date1)+'.txt', 'w+')
folder1 = 'C:/minecraft/'
folder2 = 'C:/backup-minecraft-server'
text_for_log = 'Folder or file '+ str(folder1)+'  copied to '+str(folder2)+'. Date on this moment: '+ str(date1) +'. Time on this moment: '+str( time.strftime('%H.%M.%S'))+'File:'


def world_button():
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
    # creating world+time folder and copying files

def log_button():
    directory_log = ('C:/backup-minecraft-server/server-folder-'+str(date1))
    if os.path.isdir(str(directory_log)):
        print(directory_log)
    else: os.mkdir(str(directory_log))
    a = os.listdir('C:/minecraft')
    print(a)
    if a :
        os.chdir(str(directory_log))
        if os.path.isfile('C:/minecraft/ops.json'):
            shutil.copy('C:/minecraft/ops.json', str(directory_log) )
        if os.path.isfile('C:/minecraft/banned-ips.json'):
            shutil.copy('C:/minecraft/banned-ips.json', str(directory_log) )
        if os.path.isfile('C:/minecraft/banned-players.json'):
            shutil.copy('C:/minecraft/banned-players.json', str(directory_log) )
        if os.path.isfile('C:/minecraft/euls.txt'):
            shutil.copy('C:/minecraft/eula.txt', str(directory_log) )
        if os.path.isfile('C:/minecraft/server.properties'):
            shutil.copy('C:/minecraft/server.properties', str(directory_log) )
        if os.path.isfile('C:/minecraft/server.jar'):
            shutil.copy('C:/minecraft/server.jar', str(directory_log) )
        if os.path.isfile('C:/minecraft/mine.bat'):
            shutil.copy('C:/minecraft/mine.bat', str(directory_log) )
        if os.path.isfile('C:/minecraft/whitelist.json'):
            shutil.copy('C:/minecraft/whitelist.json', str(directory_log) )
        if os.path.isfile('C:/minecraft/usercache.json'):
            shutil.copy('C:/minecraft/usercache.json', str(directory_log) )
    else: 
         print('No file detected')
    a = open('logs-'+str(date1)+'.txt', 'w+')
    a.writelines(
        
        str(text_for_log)+'server file folder folder'
    )
    a.close()


window = Tk()
window.title('Minecraft backup')
window.geometry('500x300') #500/\, 250>
# creating window
world=Button(window, text='World folder copyed', command=world_button)  
world.grid(column=1, row=1)
# world folder
log=Button(window, text='Copy server files', command=log_button)  
log.grid(column=2, row=1)
# create log folder




window.mainloop()


# 
