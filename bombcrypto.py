import webbrowser
import pyautogui
import time
from datetime import datetime

webbrowser.open('https://app.bombcrypto.io/?_ga=2.111689284.1794165064.1637188846-360359701.1636966379&_gl=1*1y3vvzp*_ga*MzYwMzU5NzAxLjE2MzY5NjYzNzk.*_ga_JECCFV3TTN*MTYzNzE4ODg0Ni4yLjAuMTYzNzE4ODg0Ni4w')
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
timer_count = 0

location_connect_wallet = None
while location_connect_wallet is None:
    location_connect_wallet = pyautogui.locateCenterOnScreen('images/connect_wallet.png', grayscale = True, confidence = 0.8)
print('connect_wallet_found')
pyautogui.doubleClick(location_connect_wallet, interval = 1)

location_metamask_sign = None
while location_metamask_sign is None:
    location_metamask_sign = pyautogui.locateCenterOnScreen('images/metamask_sign.png', grayscale = True)
print('metamask_sign_found')
pyautogui.doubleClick(location_metamask_sign, interval = 1)

location_hero_button = None
while location_hero_button is None:
    location_hero_button = pyautogui.locateCenterOnScreen('images/hero_button.png', grayscale= True,  confidence = 0.9)
pyautogui.doubleClick(location_hero_button)
print('hero_button_found')

location_work_all = None
while location_work_all is None:
    location_work_all = pyautogui.locateCenterOnScreen('images/work_all.png', grayscale = True, confidence = 0.9)
time.sleep(3)
pyautogui.doubleClick(location_work_all, interval = 1)
print('work_all_found')

time.sleep(3)
location_close_menu = None
while location_close_menu is None:
    location_close_menu = pyautogui.locateCenterOnScreen('images/close_menu.png', grayscale = True, confidence = 0.9)
    pyautogui.click(location_close_menu)
print('close_menu_found')

location_treasure_hunt = None
while location_treasure_hunt is None:
    location_treasure_hunt = pyautogui.locateCenterOnScreen('images/treasure_hunt.png', grayscale = True, confidence = 0.9)
    pyautogui.click(location_treasure_hunt)
print('treasure_hunt_found')

time.sleep(3)

location_chest = None
while location_chest is None:
    location_chest = pyautogui.locateCenterOnScreen('images/chest.png', grayscale = True, confidence = 0.9)
    pyautogui.click(location_chest)

    while True:
        time.sleep(1)
        pyautogui.screenshot('coin_info/' + "coin_status_" + now + ".png")
        break

print('chest_found')
print('screenshot_saved')

time.sleep(2)
location_close_menu = None
while location_close_menu is None:
    location_close_menu = pyautogui.locateCenterOnScreen('images/close_menu.png', grayscale = True, confidence = 0.9)
    pyautogui.click(location_close_menu)
print('close_menu_found')

def timer():
    time.sleep(10)
    location_back_arrow = None
    while location_back_arrow is None:
        location_back_arrow = pyautogui.locateCenterOnScreen('images/back_arrow.png', grayscale = True, confidence = 0.9)
        pyautogui.click(location_back_arrow)
        print('back_arrow_found')
    print('Waited')
    time.sleep(2)
    location_treasure_hunt = None
    while location_treasure_hunt is None:
        location_treasure_hunt = pyautogui.locateCenterOnScreen('images/treasure_hunt.png', grayscale = True, confidence = 0.9)
        pyautogui.click(location_treasure_hunt)
    print('treasure_hunt_found')

while timer_count < 5:
    timer()
    timer_count += 1
