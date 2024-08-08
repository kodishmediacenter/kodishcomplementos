# Python 3 code
import urllib.request, urllib.parse, urllib.error
import zipfile
import os,xbmcvfs,shutil,xbmcplugin,xbmcgui,xbmcaddon,xbmc
import sys
import re


ADDON_ID      = 'Kodish.repo.store'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')

def limpaelementum():
    for a in ['special://home/addons/plugin.video.elementum','special://home/addons/script.elementum.burst','special://home/addons/context.elementum','special://home/userdata/addon_data/plugin.video.elementum']:
        existe = xbmcvfs.translatePath(a)
        if os.path.exists(existe)==True:
            shutil.rmtree(existe)

def elementum_android(nome):

    param2 = nome
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = "plugin.video.elementum"
    url = 'https://raw.githubusercontent.com/kodishmediacenter/elementum/main/android/plugin.video.elementum.zip'
    filezip2 = "plugin.video.elementum.zip" 
    print("baixando addon ....")
    os.chdir (api_file) 
    urllib.request.urlretrieve(url, ""+filezip2+"")
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    shutil.move(source, destination2)
    dialog = xbmcgui.Dialog()
    dialog.ok('Kodish Store', 'Addon Instalado com sucesso !!!')
    database.insert_id(filezip21)



def elementum_apple(nome):

    param2 = nome
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = "plugin.video.elementum"
    url = 'https://raw.githubusercontent.com/kodishmediacenter/elementum/main/apple/plugin.video.elementum.zip'
    filezip2 = "plugin.video.elementum.zip" 
    print("baixando addon ....")
    os.chdir (api_file) 
    urllib.request.urlretrieve(url, ""+filezip2+"")
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    shutil.move(source, destination2)
    dialog = xbmcgui.Dialog()
    dialog.ok('Kodish Store', 'Addon Instalado com sucesso !!!')
    database.insert_id(filezip21)


def elementum_linux(nome):

    param2 = nome
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = "plugin.video.elementum"
    url = 'https://raw.githubusercontent.com/kodishmediacenter/elementum/main/linux/plugin.video.elementum.zip'
    filezip2 = "plugin.video.elementum.zip" 
    print("baixando addon ....")
    os.chdir (api_file) 
    urllib.request.urlretrieve(url, ""+filezip2+"")
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    shutil.move(source, destination2)
    dialog = xbmcgui.Dialog()
    dialog.ok('Kodish Store', 'Addon Instalado com sucesso !!!')
    database.insert_id(filezip21)

def elementum_windows(nome):

    param2 = nome
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = "plugin.video.elementum"
    url = 'https://raw.githubusercontent.com/kodishmediacenter/elementum/main/windows/plugin.video.elementum.zip'
    filezip2 = "plugin.video.elementum.zip" 
    print("baixando addon ....")
    os.chdir (api_file) 
    urllib.request.urlretrieve(url, ""+filezip2+"")
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    shutil.move(source, destination2)
    dialog = xbmcgui.Dialog()
    dialog.ok('Kodish Store', 'Addon Instalado com sucesso !!!')
    database.insert_id(filezip21)

def elementum_dep(nome):

    param2 = nome
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = "context.elementum"
    filezip22 = "script.elementum.burst"
    url = 'https://raw.githubusercontent.com/kodishmediacenter/elementum/main/dep.zip'
    filezip2 = "dep.zip" 
    print("baixando addon ....")
    os.chdir (api_file) 
    urllib.request.urlretrieve(url, ""+filezip2+"")
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    source2 = ""+api_file+"/"+filezip22+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    shutil.move(source, destination2)
    shutil.move(source2, destination2)
    dialog = xbmcgui.Dialog()
    dialog.ok('Kodish Store', 'Addon Instalado com sucesso !!!')
    database.insert_id(filezip21)




def main_elementum():
    dialog = xbmcgui.Dialog()
    link = dialog.select('Kodish Store - Rammeta', ['Android','Apple','Linux','Windows','Dependencias','','Remover Elementum'])

    if link == 0:
        nome = ""
        elementum_android(nome)

    if link == 1:
        nome = ""
        elementum_apple(nome)

    if link == 2:
        nome = ""
        elementum_linux(nome)

    if link == 3:
        nome = ""
        elementum_windows(nome)

    if link == 4:
        nome = ""
        elementum_dep(nome)

    if link == 6: 
        limpaelementum()
