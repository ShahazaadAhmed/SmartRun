import time
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
chrm=Application(backend="uia")
utube='open youtube'
utube_ing='open -p youtube'
op_mail='open gmail'
op_telegram='open telegram'
op_moodle='open moodle'
op_books='open books'
op_books_ing='open -p books'
op_claude='open claude'
op_chatgpt='open chatgpt'
op_chatgpt_ing='open -p chatgpt'
op_anime='open anime'
op_anime_ing='open -p anime'
def inputtask(x):   
    if utube==x:
        apl=chrm.start('"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"')
        
        time.sleep(1)
        send_keys('youtube.com{ENTER}')
    elif utube_ing==x:
        apl=chrm.start('"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"')
        
        time.sleep(1)
        send_keys('^+n')
        time.sleep(1)
        send_keys('youtube.com{ENTER}')
    elif op_telegram==x:
        apl=chrm.start('"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"')
        
        time.sleep(1)
        send_keys('https://web.telegram.org/a/{ENTER}')
    elif op_mail==x:
        apl=chrm.start('"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"')
        
        time.sleep(1)
        send_keys('https://mail.google.com/mail/u/4/#inbox{ENTER}')
    elif op_moodle==x:
        apl=chrm.start('"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"')
        
        time.sleep(1)
        send_keys('https://moodle2025.ncirl.ie/{ENTER}')
    elif op_books==x:
        apl=chrm.start('"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"')
        
        time.sleep(1)
        send_keys('https://welib.org/{ENTER}')
    elif op_books_ing==x:
        apl=chrm.start('"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"')
        
        time.sleep(1)
        send_keys('^+n')
        time.sleep(1)
        send_keys('https://welib.org/{ENTER}')
    elif op_claude==x:
        apl=chrm.start('"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"')
        
        time.sleep(1)
        send_keys('https://claude.ai/new{ENTER}')
    elif op_chatgpt==x:
        apl=chrm.start('"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"')
            
        time.sleep(1)
        send_keys('https://chatgpt.com/{ENTER}')
    elif op_chatgpt_ing==x:
        apl=chrm.start('"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"')
        
        time.sleep(1)
        send_keys('^+n')
        time.sleep(1)
        send_keys('https://chatgpt.com/{ENTER}')
    elif op_anime==x:
        apl=chrm.start('"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"')
        
        time.sleep(1)
        send_keys('https://anisuge.tv/home{ENTER}')
    elif op_anime_ing==x:
        apl=chrm.start('"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"')
        
        time.sleep(1)
        send_keys('^+n')
        time.sleep(1)
        send_keys('https://anisuge.tv/home{ENTER}')