# -*- coding: utf-8 -*- 
import sys 
import xbmcaddon, xbmcgui, xbmcplugin 
import requests,json
# Plugin Info

ADDON_ID      = 'plugin.video.freedocs'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')

icon1 = "https://yt3.ggpht.com/zsVAKjOhubWpAZvCbgyJAu9gk9uCCUHFe0iQc1mRXt7rXGT_AeyiieQ4op9JfXm6e9TCC4tFbw=s256-c-k-c0x00ffffff-no-rj"
def addDir(title, url):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':ICON,'fanart':FANART})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)

if __name__ == '__main__':
    addDir(title="Free Documentary",url="plugin://plugin.video.youtube/channel/UCijcd0GR0fkxCAZwkiuWqtQ/")
    addDir(title="FD Real",url="plugin://plugin.video.youtube/channel/UCihmYOoCWYffpuMfuP7BAqA/")
    addDir(title="FD Survive",url="plugin://plugin.video.youtube/channel/UC6LweKXMrLmT9zzXFWBrHhw/")
    addDir(title="Free Documentary - Shorts",url="plugin://plugin.video.youtube/channel/UC9_BKfayJfXO5fZWLi-GVrg/")
    addDir(title="Free Documentary - Nature",url="plugin://plugin.video.youtube/channel/UCQtW2oz8ec8pHjjxawujNjg/")
    addDir(title="Free Documentary - Paranormal",url="plugin://plugin.video.youtube/channel/UCJEyqfr-DVfKd7aRqPtyGEA/")
    addDir(title="Free Documentary - History",url="plugin://plugin.video.youtube/channel/UCsgPO6cNV0wBG-Og3bUZoFA/")
    addDir(title="Pet Docs",url="plugin://plugin.video.youtube/channel/UCbrW1SyigPkgibo0lWzaRIA/")
    addDir(title="ENDEVR",url="plugin://plugin.video.youtube/channel/UCuw0GgMlZlAsWvpI8PgCN8g/")
    xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)
