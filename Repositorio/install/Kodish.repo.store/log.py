import shutil
import xbmcvfs
import os
import xbmcgui

def main():
    # Caminho de origem e destino utilizando xbmcvfs.translatePath
    origem = xbmcvfs.translatePath("special://home/kodi.log")
    destino = xbmcvfs.translatePath("special://home/addons/webinterface.arch/kodi.log")

    # Verifica se o arquivo já existe no destino
    if os.path.exists(destino):
        # Apaga o arquivo existente
        os.remove(destino)
        print("Arquivo existente no destino foi removido.")
    
    # Copiando o arquivo kodi.log para o destino
    shutil.copy(origem, destino)
    print('Arquivo copiado com sucesso!')
    xbmcgui.Dialog().ok('[B][COLOR white]Notificação[/COLOR][/B]', 'Arquivo copiado com sucesso! digite localhost:8080/kodi.log')

