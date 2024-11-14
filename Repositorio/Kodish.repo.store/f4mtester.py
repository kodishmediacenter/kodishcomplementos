# Python 3 code
import urllib.request, urllib.parse, urllib.error
import zipfile
import os,xbmcvfs,shutil,xbmcplugin,xbmcgui,xbmcaddon,xbmc
import re

ADDON_ID      = 'Kodish.repo.store'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')

def limpacache():
    for a in ['special://home/media/*','special://home/media/*.zip']:
        existe = xbmcvfs.translatePath(a)
        if os.path.exists(existe)==True:
            shutil.rmtree(existe)

    
    
def ativaaddon(ids):
    import database
    nome = ids
    database.insert_id(nome)
    database.enable_addon(nome)
    #sxbmc.executebuiltin("Container.Update()")
    
def execc2():
    param2 = 'nome'
    zip_file = "special://home/addons/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = "f4mtester.zip"
    url = 'https://raw.githubusercontent.com/kodishmediacenter/kodi19/master/fix/f4mtester.zip'
    
    pDialog = xbmcgui.DialogProgress()
    pDialog.create('Aguarde', 'Iniciando o Download')
    pDialog.update(25, 'Download Iniciado Aguarde')
    
    filezip2 = "f4mtester.zip" 
    print("Imagem em Instalacao Aguarde")
    os.chdir (api_file) 
    urllib.request.urlretrieve(url, ""+filezip2+"")
    pDialog.update(50, 'Download Concluido')
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    pDialog.update(75, 'Extraindo os arquivos')
    source = ""+api_file+"/"+filezip21+""
    destination = "special://home/"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    #shutil.move(source, destination2)
    pDialog.update(100, 'Instalacao Feita com sucesso')
    dialog = xbmcgui.Dialog()
    pDialog.close()
    dialog.ok('Kodish Store', 'Imagem Instalada com Sucesso !!!')

    ids1 = "plugin.video.f4mTester"
    ids2 = "script.video.F4mProxy"
    ativaaddon(ids1)
    ativaaddon(ids2)

# f4mtester.execc2()

    
    




#execc2()
