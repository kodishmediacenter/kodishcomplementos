import os
import wget
#from PIL import Image
import xbmc,xbmcgui
import xbmcvfs


def main():
    folder = nome = desc = versao = desv = ''
    dialog = xbmcgui.Dialog()
    folder = dialog.input('[COLOR yellow]Digite a pasta do seu Addon[/COLOR]','ex: plugin.video.milacats', type=xbmcgui.INPUT_ALPHANUM)

    os.makedirs(xbmcvfs.translatePath("special://home/addons/"+folder+""))
    pasta = xbmcvfs.translatePath("special://home/addons/"+folder+"")
    root_folder = pasta
    
    nome = dialog.input('[COLOR yellow]Qual Nome do Seu Addon[/COLOR]','', type=xbmcgui.INPUT_ALPHANUM)
    desc = dialog.input('[COLOR yellow]Descreva seu Addon[/COLOR]','', type=xbmcgui.INPUT_ALPHANUM)
    versao = dialog.input('[COLOR yellow]Versao do Addon[/COLOR]','', type=xbmcgui.INPUT_ALPHANUM)
    desv = dialog.input('[COLOR yellow]Quem desenvolveu seu Addon[/COLOR]','', type=xbmcgui.INPUT_ALPHANUM)

    os.makedirs(""+pasta+"/resources")
    file = open(""+pasta+"/addon.xml","w") 
    file.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
    file.write('<addon id=\"'+folder+'\" name=\"'+nome+'\" version=\"'+versao+'\" provider-name=\"'+desv+'\">\n')
    file.write('  <requires>\n')
    #file.write('    <import addon="xbmc.python2" version="3.0.0"/>\n')
    file.write('    <import addon="plugin.video.youtube" version="5.0.0"/>\n')
    file.write('  </requires>\n')
    file.write(' <extension point="xbmc.python.pluginsource" library="default.py">\n')
    file.write('    <provides>video</provides>\n')
    file.write(' </extension>\n')
    file.write(' <extension point="xbmc.addon.metadata">\n')
    file.write('    <summary lang="en">'+nome+'</summary>\n')
    file.write('    <description lang="en">'+desc+'</description>\n')
    file.write('    <platform>all</platform>\n')
    file.write('    <forum></forum>\n')
    file.write('    <website></website>\n')
    file.write('    <assets>\n')
    file.write('    <icon>icon.jpg</icon>\n')
    file.write('    </assets>\n')
    file.write(' </extension>\n')
    file.write('</addon>\n')
    file.close()

    file2 = open(""+pasta+"/default.py","w")
    file2.write('# -*- coding: utf-8 -*- \n')

    file2.write('import sys \n')
    file2.write('import xbmcaddon, xbmcgui, xbmcplugin \n')
    file2.write('import requests,json\n')

    file2.write('# Plugin Info\n\n')
    file2.write('ADDON_ID      = \''+folder+'\'\n')
    file2.write('REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)\n')
    file2.write('ADDON_NAME    = REAL_SETTINGS.getAddonInfo(\'name\')\n')
    file2.write('ICON          = REAL_SETTINGS.getAddonInfo(\'icon\')\n')
    file2.write('FANART        = REAL_SETTINGS.getAddonInfo(\'fanart\')\n\n')

    canalytb = icone = ''
    canalytb = dialog.input('[COLOR yellow]Digite Link do canal ou playlist do Youtube:[/COLOR]','', type=xbmcgui.INPUT_ALPHANUM)
    icone =    dialog.input('[COLOR yellow]Digite Link do icone do canal do Youtube:[/COLOR]','', type=xbmcgui.INPUT_ALPHANUM)

    #icone = "https://yt3.ggpht.com/ytc/AAUvwniHCQOcR1k6g5mIDH1C1YxU2pxsneZkOYKXEPVnlg=s256-c-k-c0x00ffffff-no-rj"

    file_path=""+pasta+"/channels4_profile.jpg"
    file_path2=""+pasta+"/icon.jpg"
    
    if os.path.exists(file_path):
        os.remove(file_path)
        os.remove(file_path2)
        
    wget.download(icone,root_folder)
    

    file2.write('YOUTUBE_CHANNEL_ID1=  \"'+canalytb+'\"\n')
    file2.write('icon1 = \"'+icone+'\"\n')
    file2.write('ids = YOUTUBE_CHANNEL_ID1\n')
    file2.write('name = "'+nome+'"\n')

    file2.write('def addDir(title, url, thumbnail):\n')
    file2.write('    liz=xbmcgui.ListItem(title)\n')
    file2.write('    liz.setProperty(\'IsPlayable\', \'false\')\n')
    file2.write('    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )\n')
    file2.write('    liz.setArt({\'thumb\':thumbnail,\'fanart\':FANART})\n')
    file2.write('    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)\n\n')


    file2.write('if __name__ == \'__main__\':\n')
    #file2.write('   for name, id, icon in channellist:\n')
    file2.write('   addDir(title = name,url = "plugin://plugin.video.youtube/"+ids+"/",thumbnail = icon1,)\n')
    file2.write('   xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)\n')

    file2.close()
    #os.rename("unnamed.jpg", "icon.jpg")
    os.rename(file_path, file_path2)
    #im1 = Image.open(r'icon.jpg')
    #im1.save(r'icon.png')

    #import shutil
    #shutil.copyfile('default.py',''+pasta+'/default.py')
    #shutil.copyfile('addon.xml',''+pasta+'/addon.xml')
    #shutil.copyfile('icon.jpg',''+pasta+'/icon.jpg')
    #shutil.copyfile('icon.png',''+pasta+'/icon.png')

