#   Copyright (C) 2018 Lunatixz
#
#
# This file is part of ComicBook.com - YouTube.
#
# ComicBook.com - YouTube is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ComicBook.com - YouTube is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ComicBook.com - YouTube.  If not, see <http://www.gnu.org/licenses/>.


# -*- coding: utf-8 -*-

import sys
import xbmcaddon, xbmcgui, xbmcplugin

# Plugin Info
ADDON_ID      = 'plugin.video.kpoplist'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')
YOUTUBE_CHANNEL_ID1=  "playlist/PLjGxP4zgfFsAea4KjKifa0VUVMbxuwX2B"
YOUTUBE_CHANNEL_ID2=  "playlist/PLgA8PQBu3V3augI_wlHSeeIabWtiexHKh"
YOUTUBE_CHANNEL_ID3=  "playlist/PLFtZiEH-vG5t7vqrr8e-vcjOpsM0xHpMl"
YOUTUBE_CHANNEL_ID4=  "playlist/PLD5qNRSaxnF6evMxx6JIPhLD5gL2CiK5U"


def addDir(title, url):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':ICON,'fanart':FANART})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)
    
if __name__ == '__main__':
    addDir(title="Kpop List #1"            , url="plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID1+"/")
    addDir(title="Kpop List #2"            , url="plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID2+"/")
    addDir(title="Kpop List #3"            , url="plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID3+"/")
    addDir(title="Kpop List #4"            , url="plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID4+"/")
    xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)
