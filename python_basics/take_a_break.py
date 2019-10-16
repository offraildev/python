import webbrowser
import time 


for i in range(3):
    webbrowser.open_new_tab('https://www.keybr.com/')
    print(f'Break started {time.ctime()}')
    time.sleep(10)