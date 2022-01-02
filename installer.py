from platform import architecture
from time import sleep
from urllib.request import urlretrieve
from os import chdir, startfile, remove, path
from psutil import process_iter
from tkinter import messagebox
from commands import internet_button

def java_download():
     if internet_button():
          if '32bit' in architecture():
                    java='https://javadl.oracle.com/webapps/download/AutoDL?BundleId=245477_4d5417147a92418ea8b615e228bb6935&utm_source=Java'
                    urlretrieve(java, 'C:/minecraft/jre-8u311-windows-i586-iftw.exe')
                    print('Java installer downloaded')
                    print('Openning...')
                    chdir('C:/minecraft/')
                    startfile(r'C:/minecraft/jre-8u311-windows-i586-iftw.exe')
                    def process_name_32():
                         for proce in process_iter():
                              name = proce.name()
                              if name == 'jre-8u311-windows-i586-iftw.exe':
                                   return True
                    while process_name_32():
                         sleep(1)
                    print('Java downloaded')
                    if path.isfile('C:/minecraft/jre-8u311-windows-i586-iftw.exe'):
                         remove('jre-8u311-windows-i586-iftw.exe')
                         print('Java installer deleted')
                    messagebox.showinfo('Java', 'Java has been downloaded! Press ok for leave')
          elif '64bit' in architecture():
               java_64='https://javadl.oracle.com/webapps/download/AutoDL?BundleId=245479_4d5417147a92418ea8b615e228bb6935'
               urlretrieve(java_64, 'C:/minecraft/jre-8u311-windows-x64.exe')
               print('Java installer downloaded')
               print('Openning...')
               chdir('C:/minecraft/')
               startfile(r'C:/minecraft/jre-8u311-windows-x64.exe')
               def process_name_64():
                    for proce in process_iter():
                         name = proce.name()
                         if name == 'jre-8u311-windows-x64.exe':
                              return True
               while process_name_64():
                    sleep(1)
               print('Java downloaded')
               if path.isfile('C:/minecraft/jre-8u311-windows-x64.exe'):
                    remove('jre-8u311-windows-x64.exe')
                    print('Java installer deleted')
               messagebox.showinfo('Java','Java has been downloaded! Press ok for leave')
          
     else:
          messagebox.showerror(title='Internet', message='Internet don`t connected')

def python_install():
     if internet_button():
          url = 'https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe'
          if not path.isfile('C:/minecraft/python-3.10.0-amd64.exe'):urlretrieve(url, 'C:/minecraft/python-3.10.0-amd64.exe')
          print('Python installer downloaded')
          print('Openning....')
          chdir('C:/minecraft/')
          startfile('C:/minecraft/python-3.10.0-amd64.exe')
          def process_name():
                    for proce in process_iter():
                         name = proce.name()
                         if name == 'python-3.10.0-amd64.exe':
                              return True
          while process_name():
               sleep(1)
          print('Python downloaded')
          remove('python-3.10.0-amd64.exe')
          print('Python installer removed')
          messagebox.showinfo('Python','Python has been downloaded! Press ok for leave')
     else: messagebox.showerror(title='Internet', message='Internet don`t connected')
