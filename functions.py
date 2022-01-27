import webbrowser
import pyautogui
import time
from datetime import datetime

now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
timer_count = 0
timeout = time.time() + 60*1

def connect_wallet():
    location_connect_wallet = None
    while location_connect_wallet is None:
        location_connect_wallet = pyautogui.locateCenterOnScreen('images/connect_wallet.png', grayscale = True, confidence = 0.8)
    print('connect_wallet_found')
    pyautogui.doubleClick(location_connect_wallet, interval = 1)

def metamask_sign():
    location_metamask_sign = None
    while location_metamask_sign is None:
        location_metamask_sign = pyautogui.locateCenterOnScreen('images/metamask_sign.png', grayscale = True)
    print('metamask_sign_found')
    pyautogui.doubleClick(location_metamask_sign, interval = 1)

def hero_button():
    location_hero_button = None
    while location_hero_button is None:
        location_hero_button = pyautogui.locateCenterOnScreen('images/hero_button.png', grayscale= True,  confidence = 0.9)
    pyautogui.doubleClick(location_hero_button)
    print('hero_button_found')

def work_all():
    location_work_all = None
    while location_work_all is None:
        location_work_all = pyautogui.locateCenterOnScreen('images/work_all.png', grayscale = True, confidence = 0.9)
    time.sleep(3)
    pyautogui.doubleClick(location_work_all, interval = 1)
    print('work_all_found')

def close_menu():
    location_close_menu = None
    while location_close_menu is None:
        location_close_menu = pyautogui.locateCenterOnScreen('images/close_menu.png', grayscale = True, confidence = 0.9)
        pyautogui.click(location_close_menu)
    print('close_menu_found')

def treasure_hunt():
    location_treasure_hunt = None
    while location_treasure_hunt is None:
        location_treasure_hunt = pyautogui.locateCenterOnScreen('images/treasure_hunt.png', grayscale = True, confidence = 0.9)
        pyautogui.click(location_treasure_hunt)
    print('treasure_hunt_found')

def chest_coin_start():
    location_chest = None
    while location_chest is None:
        location_chest = pyautogui.locateCenterOnScreen('images/chest.png', grayscale = True, confidence = 0.9)
        pyautogui.click(location_chest)

        while True:
            time.sleep(1)
            pyautogui.screenshot('coin_info/' + "coin_status_start_" + now + ".png")
            break

def back_arrow():
    location_back_arrow = None
    while location_back_arrow is None:
        location_back_arrow = pyautogui.locateCenterOnScreen('images/back_arrow.png', grayscale = True, confidence = 0.9)
        pyautogui.click(location_back_arrow)
        print('back_arrow_found')

def sleep_all():
    location_sleep_all = None
    while location_sleep_all is None:
        location_sleep_all = pyautogui.locateCenterOnScreen('images/sleep_all.png', grayscale = True, confidence = 0.9)
    time.sleep(2)
    pyautogui.doubleClick(location_sleep_all, interval = 1)
    print('sleep_all_found')

def chest_coin_end():
    location_chest = None
    while location_chest is None:
        location_chest = pyautogui.locateCenterOnScreen('images/chest.png', grayscale = True, confidence = 0.9)
        pyautogui.click(location_chest)

        while True:
            time.sleep(1)
            pyautogui.screenshot('coin_info/' + "coin_status_end_" + now + ".png")
            break
