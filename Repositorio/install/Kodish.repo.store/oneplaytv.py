import xbmcvfs,os,shutil 

def removeonetv():
    for a in ['special://home/addons/service.oneplaytv']:
        existe = xbmcvfs.translatePath(a)
        if os.path.exists(existe)==True:
            shutil.rmtree(existe)