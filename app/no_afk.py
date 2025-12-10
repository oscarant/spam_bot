import time
from random import randint
from typing import Self

import pyautogui as pg


class NoAFK:
    def __init__(self: Self, time_minutes: int = 5) -> None:
        self.time_minutes = time_minutes
        # Get screen dimensions for safe movement
        self.screen_width, self.screen_height = pg.size()

    def start(self: Self) -> None:
        start_time = time.time()
        print(f"Starting anti-afk... Press Q to stop or wait {self.time_minutes} minutes")
        # move the mouse randomly to avoid AFK
        # Add margins to avoid corners and edges (fail-safe zones)
        margin = 50
        iteration = 0
        while time.time() - start_time < self._from_minutes_to_seconds():
            x = randint(margin, self.screen_width - margin)  # noqa: S311
            y = randint(margin, self.screen_height - margin)  # noqa: S311
            pg.moveTo(x, y, 0.5)

            # Every 3rd iteration, perform a right click to simulate activity
            if iteration % 3 == 0:
                time.sleep(0.2)  # Small delay before clicking
                pg.rightClick()
                time.sleep(0.2)  # Small delay after clicking

            iteration += 1
            # Add a small pause between movements to avoid too rapid actions
            time.sleep(1)

        print("AFK time finished")

    def _from_minutes_to_seconds(self: Self) -> int:
        return self.time_minutes * 60


if __name__ == "__main__":
    bot = NoAFK(time_minutes=180)
    bot.start()
