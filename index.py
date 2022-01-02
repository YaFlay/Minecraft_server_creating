from os import  getcwd, system, path
from urllib.request import urlretrieve
# import modules

cwd = getcwd()
windows = 'https://raw.githubusercontent.com/YaFlay/Minecraft_server_creating/main/windows.py'
if not path.isfile('/windows.py'): urlretrieve(windows, str(cwd)+'/windows.py')
#   download windows.py
commands = 'https://raw.githubusercontent.com/YaFlay/Minecraft_server_creating/main/commands.py'
if not path.isfile('/commands.py'): urlretrieve(commands, str(cwd)+'/commands.py')
#   download commands.py
installer = 'https://raw.githubusercontent.com/YaFlay/Minecraft_server_creating-BETA-/main/installer.py'
if not path.isfile('/installer.py'): urlretrieve(installer, str(cwd)+'/installer.py')
#   download commands.py
system('python3 '+ str(cwd)+'/windows.py')

