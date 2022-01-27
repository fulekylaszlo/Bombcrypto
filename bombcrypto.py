import webbrowser
import pyautogui
import time
from functions import *
from datetime import datetime


webbrowser.open('https://app.bombcrypto.io/?_ga=2.111689284.1794165064.1637188846-360359701.1636966379&_gl=1*1y3vvzp*_ga*MzYwMzU5NzAxLjE2MzY5NjYzNzk.*_ga_JECCFV3TTN*MTYzNzE4ODg0Ni4yLjAuMTYzNzE4ODg0Ni4w')
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
timer_count = 0
timeout = time.time() + 60*1

connect_wallet()

metamask_sign()

hero_button()

work_all()

time.sleep(3)

close_menu()

treasure_hunt()


time.sleep(3)

chest_coin_start()

print('chest_found')
print('screenshot_saved')

time.sleep(2)

close_menu()

def timer():
    time.sleep(300)
    back_arrow()
    print('Waited')
    time.sleep(2)
    treasure_hunt()

while timer_count < 6:
    timer()
    timer_count += 1

back_arrow()

hero_button()

sleep_all()

time.sleep(1)

close_menu()

time.sleep(1)

chest_coin_end()

print('chest_found')
print('screenshot_saved')
