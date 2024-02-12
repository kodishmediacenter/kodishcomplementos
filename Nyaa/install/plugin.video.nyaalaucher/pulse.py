# -*- coding: utf-8 -*-

import re
import urllib.request
import gzip
from html.parser import HTMLParser
import xbmc
import xbmcvfs
import xbmcgui
import xbmcplugin


dialog = xbmcgui.Dialog()
bid = dialog.input('Digite o Codigo do Nyaa veja no site na url https://nyaa.si','', type=xbmcgui.INPUT_ALPHANUM).encode('utf-8').decode('unicode_escape')
    
link = "https://nyaa.si/view/"+bid+""
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

arq = xbmcvfs.translatePath('special://home/addons/plugin.video.nyaalaucher/play.m3u')
    
# Faz a solicitação HTTP
req = urllib.request.Request(link, headers=headers)
pagina_de_busca = urllib.request.urlopen(req)

# Verifica se o conteúdo está compactado e descompacta se necessário
if pagina_de_busca.info().get('Content-Encoding') == 'gzip':
    html_content = gzip.decompress(pagina_de_busca.read())
else:
    html_content = pagina_de_busca.read()
    
def addDir(title, url, thumbnail):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':thumbnail,'fanart':''})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=xbmc.Player().play(url),listitem=liz,isFolder=True)
    parser = MyHTMLParser()

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href' and 'magnet' in attr[1]:
                    magnet_link = attr[1]
                    link3 = re.sub('(.*)href=', r'', magnet_link).replace('"><i class="fa fa-magnet fa-fw"></i>Magnet</a>', '').encode('utf-8').decode('unicode_escape')
                    url = 'plugin://plugin.video.elementum/play?uri=' + link3

                    p_file = open(arq,'w')
                    p_file.write(url)
                    p_file.close()

                    addDir(title="Play", url=url, thumbnail="https://raw.githubusercontent.com/kodishmediacenter/storek202/main/icons/fix.png")
                    xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)
                    #xbmc.executebuiltin(f'PlayMedia({arq})')
                    #xbmc.Player().play(arq)

parser = MyHTMLParser()
parser.feed(html_content.decode('utf-8'))
