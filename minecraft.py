# Made by https://github.com/yaflay
# This is create server on new version minecraft.
# if u dont use Python 3, dont use this. urllib dont working in Python2
# if u seek some bug, write me in Telegram: @YaFlay
# if u dont have C:/ disk, dont use this Python code, this crashed the code
import os
import urllib.request
import datetime
from urllib.request import urlopen
# import modules


z = datetime.date.today()
x = datetime.datetime.today()
c = 'Date today: '+ str(z)+ ', time now '+str( x.strftime('%H.%M.%S'))
# take time and date


# opening and creating starting .bat and EULA.txt files

print('Starting to create a server!')
print(str(c))
# Give now time, and print for user

check_file = os.path.exists('C:/minecraft')
if check_file == False:
     os.mkdir("C:/minecraft")
     os.chdir('C:\minecraft')
else: os.chdir('C:/minecraft')
print('Create Minecraft server folder...')
# check folder, if u dont have, creating


url = 'https://launcher.mojang.com/v1/objects/a16d67e5807f57fc4e550299cf20226194497dc2/server.jar'
urllib.request.urlretrieve(url, 'C:/minecraft/server.jar')
print('Server core downloaded...')
# downloading server files in folder

eul =  open('eula.txt', 'w+')
c = '''#Mojang EULA(https://account.mojang.com/documents/minecraft_eula).
# Time is not aviable
# Made by https://github.com/yaflay
eula=true
'''
eul.write(str(c))
eul.close()
print('EULA text has been created...')
#  creating EULA text, and write in eula.txt

a = open('mine.bat', 'w+')
b = '''
    
 java -Xmx1024M -Xms1024M -jar server.jar

 '''
a.write(str(b))
a.close()
print('Create .bat file...')
# creating .bat text and write in mine.bat file

os.startfile('mine.bat')
 # start mine.bat and server
print('Server starting!')
 # print for user
 # Thanks for using!
