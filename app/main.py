"""Simple spam bot that types a message repeatedly."""

import threading
import time
from typing import Self

import pyautogui as pg
from pynput import keyboard as kb


class SpamBotA:
    """Automate typing a message a set number of times."""

    def __init__(self: Self, message: str, times: int = 100) -> None:
        """Initialize with the message text and repeat count."""
        self.message = message
        self.times = times

    def start(self: Self) -> None:
        """Begin listening and trigger the typing loop."""
        print("press space to start")
        kb.Listener().start()
        for i in range(3):
            print(3 - i)
            time.sleep(1)
        typing_thread = threading.Thread(target=self._type_message)
        typing_thread.start()

    def _type_message(self: Self) -> None:
        for _i in range(self.times):
            pg.typewrite(self.message)
            pg.press("enter")
            # if kb.is_pressed("q"):


if __name__ == "__main__":
    bot = SpamBotA("Probanding el propio", 10)
    bot.start()
