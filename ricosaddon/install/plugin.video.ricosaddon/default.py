import xbmcgui
import xbmc
import xbmcplugin
import webbrowser
import os
import xbmcaddon

dialog = xbmcgui.Dialog()
link = dialog.select('Bem Vindo Addon Web ricos', ['Talvez seja necessario Clicar denovo','','Ao Vivo', 'Canal No Youtube','Whatsapp'])

# Plugin Info
ADDON_ID      = 'plugin.video.ricosaddon'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')

def addDir(title, url):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':ICON,'fanart':FANART})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)

if link == 2:
    url = "https://5d82644094cc0.streamlock.net:443/ricostv/ricostv/playlist.m3u8"
    xbmc.Player().play(url)

if link == 3:
    addDir(title="Canal da Ricos", url="plugin://plugin.video.youtube/channel/UCsx3z9zMWDEDZrveqZ4vPbA/")
    xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)

if link == 4:
     if xbmc . getCondVisibility ( 'system.platform.android' ) :
         xbmc . executebuiltin ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://api.whatsapp.com/send?phone=5511988700735' ) )
     else:
        webbrowser . open ( 'https://api.whatsapp.com/send?phone=5511988700735' )
    
    
