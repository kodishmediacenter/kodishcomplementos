# -*- coding: utf-8 -*- 
import sys 
import xbmcaddon, xbmcgui, xbmcplugin 
import requests,json
# Plugin Info

ADDON_ID      = 'plugin.video.swenfilmes'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')

YOUTUBE_CHANNEL_ID1=  "channel/UCoBSoU_ho6gYEsEdO72h1Zg"
icon1 = "https://yt3.googleusercontent.com/wykTvToRvQYCpmTAMoCZlOB-uXWas3ycMMsWkas65WP1b2tWIW6EXWs90OF2e8pV6p1bkzqhhA=s512-c-k-c0x00ffffff-no-rj"
ids = YOUTUBE_CHANNEL_ID1
name = "Swen Filmes"
def addDir(title, url, thumbnail):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':thumbnail,'fanart':FANART})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)

if __name__ == '__main__':
   addDir(title = name,url = "plugin://plugin.video.youtube/"+ids+"/",thumbnail = icon1,)
   xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)
