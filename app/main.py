from typing import Self

import keyboard as kb
import pyautogui as pg


class SpamBotA:
    def __init__(self: Self, message: str, times: int = 100) -> None:
        self.message = message
        self.times = times

    def start(self: Self) -> None:
        print("press space to start")
        kb.wait("space")
        print("space was pressed, starting...")
        for _i in range(self.times):
            pg.typewrite(self.message)
            pg.press("enter")
            if kb.is_pressed("q"):
                break


if __name__ == "__main__":
    bot = SpamBotA("Probanding el propio", 10)
    bot.start()
