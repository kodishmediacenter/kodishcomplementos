import zipfile
import xbmcgui
import xbmc
import os.path

def notify(msg):
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)' % ('Kodi', msg, 1000, ''))

def extract_zip(filename,dest):
    dp = xbmcgui.DialogProgress()
    name = os.path.basename(filename)
    dp.create('Extraindo '+name,'Por favor aguarde...')
    dp.update(0)
    with zipfile.ZipFile(filename) as zf:
        total = len(zf.infolist())
        part = total/100
        count = 0
        for zip in zf.infolist():
        #print(zip.filename, ' : ', zip.file_size, ' : ', zip.date_time, ' : ', 
            try:
                zf.extract(zip, dest)
                #except zipfile.error as e:
            except:
                pass
            count += 1
            percent = int(count/part)
            #print(percent)
            msg = 'Extraindo '+zip.filename
            dp.update(percent, msg)
            if percent == 100:
                notify('Extraido com Sucesso!')
            #elif dp.iscanceled():
            #    dp.close()
            #    raise notify('Extração cancelada.')
            