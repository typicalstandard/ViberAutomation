from pywinauto import Application
from pywinauto.keyboard import send_keys
import pyautogui
import time

class ViberAutomation:
    def __init__(self, app_path):
        self.app_path = app_path
        self.app = None
        self.dlg = None

    @staticmethod
    def select(count=7, cord_x=1600, cord_y=310, scroll=-350):
        for i in range(1, count):
            time.sleep(1)
            s = 100
            pyautogui.click(cord_x, cord_y + (s * i))

        pyautogui.scroll(scroll)


    def start_app(self):
            self.app = Application().start(self.app_path, timeout=15)
            self.app = Application(backend="uia").connect(title='Rakuten Viber', timeout=15)
            self.dlg = self.app.Rakuten_Viber
            for i in range(5):
                pyautogui.press('esc')

    def maximize_window(self):
        time.sleep(1)
        pyautogui.hotkey("win", "up")


    def open_notes(self):
        self.dlg.CheckBox.click_input()
        self.dlg.child_window(title='Мои заметки', control_type="Button").wait('ready', timeout=15).click_input()

    def open_details(self):
            send_keys('^i')
            time.sleep(1)
            self.dlg.child_window(title="Ссылки", control_type="Button").wait('ready', timeout=15).click()
            time.sleep(1)


    def select_element(self,count_post):
        pyautogui.click(1600, 330, button='right')
        self.dlg.child_window(title="Выбрать", control_type="MenuItem").wait('ready', timeout=15).click_input()
        if count_post < 8:
            self.select(count=count_post,scroll=0)
        else:
            for i in range(count_post // 7):
                if i == 0:
                    self.select()
                else:
                    self.select(count=8, cord_x=1600, cord_y=180, scroll=-335)
            if count_post % 7 != 0:
                self.select(count=(count_post % 7) + 1, cord_x=1600, cord_y=180, scroll=0)

    def post_messages(self,group):
        self.dlg.window(class_name_re='.*IconButton.*', found_index=3).wait('ready', timeout=15).click_input()
        time.sleep(1)
        for post in group:
            pyautogui.hotkey("shift", "alt")
            pyautogui.typewrite(post, interval=0.10)
            pyautogui.hotkey("shift", "alt")
            pyautogui.press('enter')
        pyautogui.press('enter')

