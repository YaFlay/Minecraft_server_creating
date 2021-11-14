import tkinter
import os
# from urllib.request import urlretrieve
import urllib
import urllib.request

#Minecraft server properties
#Time dont aviable
text_for_server_properties= '''
broadcast-rcon-to-ops=true
view-distance=''' 
viev = input('Viev distnce: ')
text_for_server_properties_2='''
enable-jmx-monitoring=false
server-ip=
resource-pack-prompt='''
resource_pack = input('Resource pack link: ')
text_for_server_properties_3 = '''
rcon.port=25575
gamemode='''
gamemode = input('Gamemode on your server(s/c): ')
if gamemode == 's':
    gamemode = 'survival'
else:
    gamemode = 'creative'
text_for_server_properties_4='''
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
whitelist='''
whitelist = input('White list allow? (true/false)')
'''
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
server_properties=open('C:/minecraft/server.properties', 'w+')
server_properties.write(str(text_for_server_properties))
server_properties.write(str(viev))
server_properties.write(str(text_for_server_properties_2))
server_properties.write(str(gamemode))
server_properties.write(str(text_for_server_properties_4))
server_properties.write(str(whitelist))
