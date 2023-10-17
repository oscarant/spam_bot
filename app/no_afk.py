import time
from random import randint
from typing import Self

import pyautogui as pg


class NoAFK:
    def __init__(self: Self, time_minutes: int = 5) -> None:
        self.time_minutes = time_minutes

    def start(self: Self) -> None:
        start_time = time.time()
        print(f"Starting anti-afk... Press Q to stop or wait {self.time_minutes} minutes")
        # move the mouse randomly to avoid AFK
        while time.time() - start_time < self._from_minutes_to_seconds():
            pg.moveTo(randint(0, 1920), randint(0, 1080), 0.5)  # noqa: S311
            # press Q to stop
            # if pg.is_key_pressed("q"):

        print("AFK time finished")

    def _from_minutes_to_seconds(self: Self) -> int:
        return self.time_minutes * 60


if __name__ == "__main__":
    bot = NoAFK(time_minutes=1)
    bot.start()
