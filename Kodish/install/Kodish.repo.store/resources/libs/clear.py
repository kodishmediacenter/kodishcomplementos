import xbmc
import xbmcgui
def notify(msg):
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)' % ('Kodi', msg, 1000, ''))

#EVITAR EXCLUIR O WIZARD
addon_folder = 'Kodish.repo.store'

def reset(folder):
    import os, shutil
    dp = xbmcgui.DialogProgress()
    dp.create('Limpando','Por favor aguarde...')
    dp.update(0)
    total = len(os.listdir(folder))
    addon_wizard = os.path.join(folder, addon_folder)
    if os.path.isdir(addon_wizard):
        total = total-1
    part = total/100
    count = 0
    for filename in os.listdir(folder):
        if filename != addon_folder:
            file_path = os.path.join(folder, filename)
            count += 1
            percent = int(count/part)
            msg = 'Limpando '+filename
            dp.update(percent, msg)
            if dp.iscanceled():
                dp.close()
                raise notify('Limpeza cancelada.')
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
            if percent == 100:
                notify('Limpo com Sucesso!')
            