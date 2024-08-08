import xbmc
import xbmcgui
import xbmcaddon
import xbmcvfs
import xbmcplugin
import os
import sys
import re
import urllib.parse as urllib
import urllib.request as urllib2
from resources.libs import database, downloader, extract, clear
import shutil


sitemap = 'special://home'

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
home = xbmcvfs.translatePath("special://home/addons")
#home = xbmcvfs.translatePath(addon.getAddonInfo('path'))
icon = addon.getAddonInfo('icon')
addon_handle = int(sys.argv[1])

build_url_menu = 'https://raw.githubusercontent.com/kodishmediacenter/storek202/main/storeatual'  
build_url_menu2 = 'https://raw.githubusercontent.com/kodishmediacenter/storek202/main/store2'  
build_url_menu3 = 'https://raw.githubusercontent.com/kodishmediacenter/storek202/main/fix'
build_url_menu4 = 'https://raw.githubusercontent.com/kodishmediacenter/storek202/main/ssrp/ssbr'
build_url_menu5 = 'https://raw.githubusercontent.com/kodishmediacenter/storek202/main/distro'


def fontes_addons(): 
    deffontes = xbmcvfs.translatePath("special://home/addons/Kodish.repo.store/conf/sources.xml")
    destino = xbmcvfs.translatePath("special://home/userdata/sources.xml")
    
    with open(deffontes, 'r', encoding='utf-8') as arquivo_origem:
        conteudo = arquivo_origem.read()

    # Abre um novo arquivo para escrita e grava o conteúdo lido do arquivo sources.xml
    with open(destino, 'w', encoding='utf-8') as arquivo_destino:
        arquivo_destino.write(conteudo)
        xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]','Sucesso !!! Para Surtir Efeito e necessario sair do Kodi e Abrir novamente') 








def notify(msg):
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)' % (addonname, msg, 1000, icon))

def addir(name,url,mode,iconimage,fanart,description,skin,setaddon,folder=True):
    li=xbmcgui.ListItem(name)
    if mode !=0:
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)+"&skin="+urllib.quote_plus(str(skin))+"&setaddon="+urllib.quote_plus(str(setaddon))
    else:
        u=sys.argv[1]
    li.setInfo(type="Video", infoLabels={"Title": name, "Plot": description})
    li.setArt({"icon": iconimage, "thumb": iconimage})
    li.setProperty('fanart_image', fanart)
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=u, listitem=li, isFolder=folder)

def copy_img(): 
    img = xbmcvfs.translatePath("special://home/media/backgrounds")
    import shutil
    shutil.copyfile(img,img)

def principal2():
    addir('[B]... Vc está Banido :-D !!!!!![/B] Saiba Mais em https://tinyurl.com/nokodishstore','',1000,icon,'','','','')
    xbmcplugin.endOfDirectory(addon_handle)
    
def principal31():
    #addir('[B]...[/B]','',1000,icon,'','','','')
    #addir('[B]=========================================[/B]','',500,icon,'','','','')
    addir('[B]Todos Addons 1                      [/B]','',1,icon,'','','','')
    addir('[B]Todos Addons 2                      [/B]','',5,icon,'','','','')
    addir('[B]Instalar Super Servidor             [/B]','',11,icon,'','','','')
    addir('[B]Elementum Addons                    [/B]','',3,icon,'','','','')
    addir('[B]Instalar o Fix                      [/B]','',8,icon,'','','','')
    addir('[B]Kodish Update                       [/B]','',15,icon,'','','','')
    xbmcplugin.endOfDirectory(addon_handle)

def principal32():
    addir('[B]Remover Elementum                   [/B]','',6,icon,'','','','')
    addir('[B]F4M Tester                          [/B]','',7,icon,'','','','')
    addir('[B]Mudar Player do Kodi                [/B]','',9,icon,'','','','')
    addir('[B]Remover lista PVR Simple Client     [/B]','',12,icon,'','','','')
    addir('[B]Escolher uma lista PVR              [/B]','',13,icon,'','','','')
    addir('[B]Adicionar Fontes ao Kodi            [/B]','',14,icon,'','','','')
    addir('[B]Criar addon Youtube Kodi            [/B]','',1003,icon,'','','','')
    xbmcplugin.endOfDirectory(addon_handle)


def principal():
    addir('[B]Instalação de Add-dons e Complementos                  [/B]','',1001,icon,'','','','')
    addir('[B]Kodi e Configurações diversas                          [/B]','',1002,icon,'','','','')
    xbmcplugin.endOfDirectory(addon_handle)



def external_pvr():
    dialog = xbmcgui.Dialog()
    player = dialog.select('Kodish Store - Rammeta Escolha sua Lista', ['Pluto TV BR','Lista Gratis','Formiga'])

    player_mx = ['pluto','listagratis','formiga']
    cplayer = str(player_mx[player])
    

    file = ''+sitemap+'/addons/Kodish.repo.store/pvr/'+cplayer+'/instance-settings-1.xml'
    filewk = os.path.join(xbmcvfs.translatePath(file))
        
    file2 = 'special://home/userdata/addon_data/pvr.iptvsimple/instance-settings-1.xml'
    filewk2 = os.path.join(xbmcvfs.translatePath(file2))
    
    import shutil
    shutil.copy(filewk,filewk2)
    xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]','Para Player Funcionar terá sair do Kodi')

def external_player():
    dialog = xbmcgui.Dialog()
    player = dialog.select('Kodish Store - Rammeta Escolha seu Player', ['Remover Externo Player','VLC Windows 32 bits','VLC Windows 64 bits','VLC Linux','VLC Android','Archos Video Android','BSPlayer Free','Daroon Player','Dice Player Free','Dice Player Paid','Just Player','Mobo player Free','m Video player Free','MX Player Free','MX Player Pro','Pot Player (Windows)','Rock Player','Rock Player Lite','SopCast','TPlayer','Wondershare Player','MPV Windows 32 bits','MPV Windows 64 bits','MPV Linux'])

    player_mx = ['nenhum','VLCwin32','VLCwin64','VLClinux','VLCPlayer','ArchosVideo','BSPlayerFree','DaroonPlayer','DicePlayerFree','DicePlayerPaid','JustPlayer','MoboplayerFree','mVideoplayerFree','MXPayerFree','MXPlayerPro','PotPlayer(windows)','RockPlayer','RockPlayerLite','SopCast','TPlayer','WondersharePlayer','MPVwin32','MPVwin64','MPVlinux']
    cplayer = str(player_mx[player])
    

    file = ''+sitemap+'/addons/Kodish.repo.store/externalplayer/'+cplayer+'/playercorefactory.xml'
    filewk = os.path.join(xbmcvfs.translatePath(file))
        
    file2 = 'special://home/userdata/playercorefactory.xml'
    filewk2 = os.path.join(xbmcvfs.translatePath(file2))
    
    import shutil
    shutil.copy(filewk,filewk2)
    xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]','Para Player Funcionar terá sair do Kodi')



def elementum_buffer():
    dialog = xbmcgui.Dialog()
    player = dialog.select('Kodish Store - Rammeta', ['20 mb','50 mb','70 mb','100 mb',''])
    
    player_mx = ['20mb','50mb','70mb','100mb']
    cbuffer = str(player_mx[player])
    

    file = 'special://home/addons/Kodish.repo.store/defs/'+cbuffer+'/settings.xml'
    filewk = os.path.join(xbmcvfs.translatePath(file))
        
    file2 = 'special://home/userdata/addon_data/plugin.video.elementum/settings.xml'
    filewk2 = os.path.join(xbmcvfs.translatePath(file2))

    import buffer
    buffer.buffer(filewk,filewk2)

    os.remove(filewk2)

    import shutil
    shutil.copy(filewk,filewk2)
    xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]','Para aplicar buffer tem reiniciar o Kodi') 


def list_builds():
    addir('[B]...[/B]','',999,icon,'','','','')
    data = open_url(build_url_menu)
    list_build = re.compile('name="(.*?)"\nurl="(.*?)"\niconimage="(.*?)"\nfanart="(.*?)"\ndescription="(.*?)"\nskin_id="(.*?)"').findall(data)
    for name, url, iconimage, fanart, description, skin in list_build:       
       addir(name.encode('utf-8', 'ignore'),url,2,str(iconimage),str(fanart),str(description).encode('utf-8', 'ignore'),str(skin),'',folder=False)

def list_builds2():
    addir('[B]...[/B]','',999,icon,'','','','')
    data = open_url(build_url_menu2)
    list_build = re.compile('name="(.*?)"\nurl="(.*?)"\niconimage="(.*?)"\nfanart="(.*?)"\ndescription="(.*?)"\nskin_id="(.*?)"').findall(data)
    for name, url, iconimage, fanart, description, skin in list_build:       
       addir(name.encode('utf-8', 'ignore'),url,2,str(iconimage),str(fanart),str(description).encode('utf-8', 'ignore'),str(skin),'',folder=False)

def list_fix():
    addir('[B]...[/B]','',999,icon,'','','','')
    list_build = ""
    data = open_url(build_url_menu3)
    list_build = re.compile('name="(.*?)"\nurl="(.*?)"\niconimage="(.*?)"\nfanart="(.*?)"\ndescription="(.*?)"\nskin_id="(.*?)"').findall(data)
    for name, url, iconimage, fanart, description, skin in list_build:       
       addir(name.encode('utf-8', 'ignore'),url,2,str(iconimage),str(fanart),str(description).encode('utf-8', 'ignore'),str(skin),'',folder=False)

def list_super():
    addir('[B]...[/B]','',999,icon,'','','','')
    data = open_url(build_url_menu4)
    list_build = re.compile('name="(.*?)"\nurl="(.*?)"\niconimage="(.*?)"\nfanart="(.*?)"\ndescription="(.*?)"\nskin_id="(.*?)"').findall(data)
    for name, url, iconimage, fanart, description, skin in list_build:       
       addir(name.encode('utf-8', 'ignore'),url,2,str(iconimage),str(fanart),str(description).encode('utf-8', 'ignore'),str(skin),'',folder=False)

def list_update():
    addir('[B]...[/B]','',999,icon,'','','','')
    list_build = ""
    data = open_url(build_url_menu5)
    list_build = re.compile('name="(.*?)"\nurl="(.*?)"\niconimage="(.*?)"\nfanart="(.*?)"\ndescription="(.*?)"\nskin_id="(.*?)"').findall(data)
    for name, url, iconimage, fanart, description, skin in list_build:       
       addir(name.encode('utf-8', 'ignore'),url,2,str(iconimage),str(fanart),str(description).encode('utf-8', 'ignore'),str(skin),'',folder=False)
       
def mybuilds():
    try:
        list_builds()
    except:
        pass
    xbmcplugin.endOfDirectory(addon_handle)

def mybuilds2():
    try:
        list_builds2()
    except:
        pass
    xbmcplugin.endOfDirectory(addon_handle)

def mybuilds3():
    try:
        list_fix()
    except:
        pass
    xbmcplugin.endOfDirectory(addon_handle)

def mybuilds4():
    try:
        list_super()
    except:
        pass
    xbmcplugin.endOfDirectory(addon_handle)

def mybuilds5():
    try:
        list_update()
    except:
        pass
    xbmcplugin.endOfDirectory(addon_handle)
def limpapvr():
    for a in ['special://home/userdata/addon_data/pvr.iptvsimple']:
        existe = xbmcvfs.translatePath(a)
        if os.path.exists(existe)==True:
            shutil.rmtree(existe)
            xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]','PVR Resetado por Renicie o Kodi') 
            
def limpaelementum():
    for a in ['special://home/addons/plugin.video.elementum','special://home/addons/script.elementum.burst','special://home/addons/context.elementum','special://home/userdata/addon_data/plugin.video.elementum']:
        existe = xbmcvfs.translatePath(a)
        if os.path.exists(existe)==True:
            shutil.rmtree(existe)
            
def elementum():
    import ntpath
    data = open_url('https://elementumorg.github.io/')
    list_addons = re.compile('<div class="platform-asset"><a href="(.*?)" title="(.*?)".+?</a>').findall(data)
    for link, name in list_addons:
        #print(name.strip())
        if '-' in link and not 'Client' in name:
            filename = ntpath.basename(link)
            addon_id = filename.split('-')[0]
            #name = name.strip()+' - '+addon_id 
            name = addon_id+' - '+name.strip()
            addir(name.encode('utf-8', 'ignore'),link,4,'','','','',addon_id,folder=False)

def elementum_list():
    #addir('[B]-------- Plugins do Elementum --------[/B]','',0,'','','','','')
    addir('[B]...[/B]','',999,icon,'','','','')
    try:
        elementum()
    except:
        pass
    xbmcplugin.endOfDirectory(addon_handle)
    
    
def setskin(skin_id):
    skin_txt = os.path.join(home, 'skin.txt')
    try:
        os.remove(skin_txt)
    except:
        pass
    try:
        f = open(skin_txt,'w')
        f.write('skin="%s"'%skin_id)
        f.close()
    except:
        pass  

def install_build(name,url,skin):
    if xbmcgui.Dialog().yesno(addonname, 'Deseja Instalar %s?\nA Configuração atual do kodi será modificada'%name):
        kodi = xbmcvfs.translatePath('special://home/addons')
        addons = xbmcvfs.translatePath('special://home/addons')
        packages = xbmcvfs.translatePath('special://home/addons/packages')
        media_kodi = xbmcvfs.translatePath('special://home/media')
        userdata_kodi = xbmcvfs.translatePath('special://home/userdata')
        download_file = resolve(url)
        
        addons_id = re.sub('https://raw.githubusercontent.com/kodishmediacenter/kodi19/master/addons/',r'',url).replace('.zip','')
        database.enable_addon(addons_id)
        database.enable_addon(addons_id)
        
        try:
            if download_file.endswith(".zip"):
                # limpando kodi
                #try:
                #    clear.reset(addons)
                #except:
                #    pass
                #try:
                #    clear.reset(userdata_kodi)
                #except:
                #    pass
                #try:
                #    clear.reset(media_kodi)
                #except:
                #    pass                    
                import ntpath
                try:
                    os.mkdir(packages)
                except:
                    pass
                filename = ntpath.basename(download_file)
                dest=os.path.join(packages, filename)
                try:
                    os.remove(lib)
                except:
                    pass
                try:
                    downloader.download(download_file, name, dest)
                except:
                    print('Wizard Builds: Falha ao baixar, link invalido ou download cancelado')
                    raise Exception
                try:
                    extract.extract_zip(dest,kodi)
                except:
                    print('Wizard Builds: Falha ao extrair arquivos.')
                    raise Exception
                xbmc.sleep(1000)
                try:
                    os.remove(dest)
                except:
                    pass
                skin_folder = os.path.join(addons, skin)
                if os.path.isdir(skin_folder):
                    setskin(skin)                    
                #xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]','APERTE OK PARA FECHAR O KODI E ABRA NOVAMENTE!')   
                #xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Application.Quit","id":1}') 
            else:
                print('Kodish Store: Arquivo não é zip ou não foi encontrado um link')
                raise Exception
        except:
            notify('Falha ao Instalar o conteudo!')
            
def install_addon(addon_id,url):
    if xbmcgui.Dialog().yesno(addonname, 'Deseja Instalar %s?'%addon_id):
        addons = xbmcvfs.translatePath('special://home/addons')
        packages = xbmcvfs.translatePath('special://home/addons/packages')
        try:
            import ntpath
            try:
                os.mkdir(packages)
            except:
                pass
            filename = ntpath.basename(url)
            dest=os.path.join(packages, filename)            
            try:
                downloader.download(url, addon_id, dest)
            except:
                print('Wizard Builds: Falha ao baixar, link invalido ou download cancelado')
                raise Exception
            try:
                extract.extract_zip(dest,addons)
            except:
                print('Wizard Builds: Falha ao extrair arquivos.')
                raise Exception
            xbmc.sleep(1000)
            database.enable_addon(addon_id)
            #xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]','APERTE OK PARA FECHAR O KODI E ABRA NOVAMENTE!')   
            #xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Application.Quit","id":1}')
        except:
            notify('Falha ao Instalar Addon!')         


def open_url(url):
    try:
        hdr = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36', 
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
        req = urllib2.Request(url, headers=hdr)
        response = urllib2.urlopen(req)
        data = response.read().decode('utf-8')
        return data
    except:
        data = ''
        return data

def mediafire(url):
    data = open_url(url)
    link = re.compile('aria-label="Download file"\n.+?href="(.*?)"',re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data)
    return link[0]

def resolve(url):
    if 'mediafire' in url:
        try:
            resolved = mediafire(url)
        except:
            resolved = ''
    else:
        resolved = url
    return resolved    


def get_params():
    param=[]
    paramstring=sys.argv[2]
    if len(paramstring)>=2:
        params=sys.argv[2]
        cleanedparams=params.replace('?','')
        if (params[len(params)-1]=='/'):
            params=params[0:len(params)-2]
        pairsofparams=cleanedparams.split('&')
        param={}
        for i in range(len(pairsofparams)):
            splitparams={}
            splitparams=pairsofparams[i].split('=')
            if (len(splitparams))==2:
                param[splitparams[0]]=splitparams[1]

    return param
    
def main():
    params=get_params()
    name=None
    mode=None
    iconimage=None
    fanart=None
    description=None
    try:
        url=urllib.unquote_plus(params["url"])
    except:
        pass
    try:
        name=urllib.unquote_plus(params["name"])
    except:
        pass
    try:
        iconimage=urllib.unquote_plus(params["iconimage"])
    except:
        pass
    try:
        mode=int(params["mode"])
    except:
        pass
    try:
        fanart=urllib.unquote_plus(params["fanart"])
    except:
        pass
    try:
        description=urllib.unquote_plus(params["description"])
    except:
        pass
    try:
        skin=urllib.unquote_plus(params["skin"])
    except:
        pass
    try:
        setaddon=urllib.unquote_plus(params["setaddon"])
    except:
        pass                
    if mode==None:
        for a in ['special://home/addons/KeltecMP.repository','special://home/addons/plugin.video.KelTec.MP.matrix','special://home/addons/plugin.program.keltec.wizard','special://home/userdata/addon_data/plugin.video.TorrentPlay']:
            existe = xbmcvfs.translatePath(a)
            if os.path.exists(existe)==True:
                principal2()
            else:
                principal()
                break
    elif mode==1:
        mybuilds()
    elif mode==2:
        install_build(name,url,skin)
    elif mode==3:
        elementum_list()
    elif mode==4:
        install_addon(setaddon,url)
    elif mode==5:
        mybuilds2()
    elif mode==6:
        limpaelementum()
    elif mode==7:
        import f4mtester
        f4mtester.execc2()
    elif mode==8:
        mybuilds3()
    elif mode==9:
        external_player()
    elif mode==10:
        elementum_buffer()
    elif mode==11: 
        mybuilds4()
    elif mode==12:
        limpapvr()
    elif mode==13:
        external_pvr()
    elif mode==14: 
        fontes_addons()
    elif mode==15: 
        mybuilds5()
    elif mode==999:
        principal()
    elif mode==1000:
        xbmc.executebuiltin('ActivateWindow(Videos,Addons,return)')
    elif mode==1001:
        principal31()
    elif mode==1002:
        principal32()
    elif mode==1003:
        import youtubeaddon
        youtubeaddon.main()

if __name__ == "__main__":
	main()
 
