# -*- coding: utf-8 -*-

import sys
import xbmcaddon, xbmcgui, xbmcplugin

# Plugin Info
ADDON_ID      = 'plugin.video.andreguedes'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')

YOUTUBE_CHANNEL_ID1=  "channel/UCwS-7_1aHcx4KrqOPhTU-IA"
YOUTUBE_CHANNEL_ID2=  "channel/UCwS-7_1aHcx4KrqOPhTU-IA/playlists"


icon2 = "https://yt3.ggpht.com/a/AATXAJx2gyNPztNTs0JpjKF9jIPqVeByeQiI3tcBOmxr=s256-c-k-c0xffffffff-no-rj-mo"
icon3 = icon2



def addDir(title, url, thumbnail):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':thumbnail,'fanart':FANART})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)
    
if __name__ == '__main__':

   addDir(title = "Todos os Videos",url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID1+"/",thumbnail = icon2,)
   addDir(title = "Playlist",url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID2+"/",thumbnail = icon3,)
   xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)

	


