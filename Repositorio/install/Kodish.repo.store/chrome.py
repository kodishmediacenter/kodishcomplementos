def web(url):
    
    import subprocess
    import platform

    os = platform.system()
    print(os)
    if os == 'Windows':
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
        subprocess.run([chrome_path, url])
    if os == 'Darwin'
        chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        subprocess.run([chrome_path, url])
    if os == 'Linux'
        chrome_path = '/usr/bin/google-chrome'
        subprocess.run([chrome_path, url])
    else
        




url = "youtube.com/tv"
web(url)
