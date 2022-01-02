from os import  getcwd, system, path
import urllib.request as urlreq
# import modules

def window_download():
    cwd = getcwd()
    url = 'https://raw.githubusercontent.com/YaFlay/Minecraft_server_creating/main/windows.py'
    if not path.isfile('/windows.py'): urlreq.urlretrieve(url, str(cwd)+'/windows.py')
    url2 = 'https://raw.githubusercontent.com/YaFlay/Minecraft_server_creating/main/commands.py'
    if not path.isfile('/commands.py'): urlreq.urlretrieve(url2, str(cwd)+'/commands.py')
    system('python3 '+ str(cwd)+'/windows.py')

window_download()
