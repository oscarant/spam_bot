from typing import Self

import pyautogui as pg
from pynput import keyboard as kb


class SpamBotA:
    def __init__(self: Self, message: str, times: int = 100) -> None:
        self.message = message
        self.times = times

    def start(self: Self) -> None:
        print("press space to start")
        kb.Listener().start()
        print("space was pressed, starting...")
        for _i in range(self.times):
            pg.typewrite(self.message)
            pg.press("enter")
            # if kb.is_pressed("q"):


if __name__ == "__main__":
    bot = SpamBotA("Probanding el propio", 10)
    bot.start()
