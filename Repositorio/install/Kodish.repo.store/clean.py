import os
import xbmcvfs,shutil,xbmcgui

def limpezakodi():
    for a in ['special://home/addons/packages','special://home/addons/temp','special://home/cache','special://home/userdata/Thumbnails']:
        existe = xbmcvfs.translatePath(a)
        if os.path.exists(existe)==True:
            shutil.rmtree(existe)
    xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]','Limpeza Feita com Sucesso !!!') 


    
