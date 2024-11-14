import xbmc
import xbmcvfs
import xbmcgui
import xbmcaddon
import shutil
import os
import re

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
home = xbmcvfs.translatePath(addon.getAddonInfo('path'))
cache = xbmcvfs.translatePath(os.path.join('special://','home', 'cache'))
addons = xbmcvfs.translatePath(os.path.join('special://','home', 'addons'))

def check_skin():
    skin_txt = os.path.join(home, 'skin.txt')
    if os.path.isfile(skin_txt):
        try:
            f = open(skin_txt,'r+')
            data = f.read().replace('\n','').replace('\r','').replace(' ','')
            match = re.compile('skin="(.*?)"').findall(data)
            if match !=[]:
                try:
                    skin_folder = os.path.join(addons, match[0])
                    if os.path.isdir(skin_folder):
                        xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"lookandfeel.skin","value":"%s"}}'%match[0])
                        xbmc.sleep(1000)
                        xbmc.executebuiltin('SendClick(11)')
                        f.close()
                        xbmc.sleep(1000)
                        try:
                            os.remove(skin_txt)
                        except:
                            print('Build Wizard: skin.txt esta em uso e nao pode ser deletado')
                except:
                    print('Build Wizard: Falha ao trocar de skin, id invalido ou nao existe')
                    raise Exception
            else:
                f.close()
        except:
            xbmc.executebuiltin('Notification(%s, %s, %d, %s)' % ('[B]Kodish Store Rametta[/B]', 'Falha ao mudar skin....', 3000, ''))
            
def clear(folder):
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)' % ('[B]Kodish Store Rametta[/B]', 'Limpando cache....', 3000, ''))
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except:
            pass

check_skin()
if os.path.isdir(cache):
    clear(cache)   