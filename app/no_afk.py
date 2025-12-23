"""Keep the user active by moving the mouse with an ESC cancel hotkey."""

import threading
import time
from random import randint
from typing import Self

import keyboard
import pyautogui as pg


class NoAFK:
    """Periodically move/click the mouse to prevent AFK detection."""

    def __init__(self: Self, time_minutes: int = 5) -> None:
        """Configure the anti-AFK duration in minutes."""
        self.time_minutes = time_minutes
        # Get screen dimensions for safe movement
        self.screen_width, self.screen_height = pg.size()
        self.stop_event = threading.Event()

    def start(self: Self) -> None:
        """Run the anti-AFK loop until time elapses or ESC is pressed."""
        start_time = time.time()
        total_seconds = self._from_minutes_to_seconds()
        print(f"Starting anti-afk... Press ESC to stop or wait {self.time_minutes} minutes")
        # move the mouse randomly to avoid AFK
        # Add margins to avoid corners and edges (fail-safe zones)
        margin = 50
        iteration = 0
        stop_hotkey = keyboard.add_hotkey("esc", self.stop_event.set)
        try:
            while not self.stop_event.is_set():
                elapsed = time.time() - start_time
                remaining = max(0, int(total_seconds - elapsed))
                remaining_str = self._format_remaining_time(remaining)
                print(f"\rTime remaining: {remaining_str}", end="", flush=True)
                if elapsed >= total_seconds:
                    break

                x = randint(margin, self.screen_width - margin)  # noqa: S311
                y = randint(margin, self.screen_height - margin)  # noqa: S311
                pg.moveTo(x, y, 0.5)

                # Every 3rd iteration, perform a right click to simulate activity
                if iteration % 3 == 0:
                    if self._wait_or_stop(0.2):
                        break
                    pg.rightClick()
                    if self._wait_or_stop(0.2):
                        break

                iteration += 1
                # Add a small pause between movements to avoid too rapid actions
                if self._wait_or_stop(1):
                    break
        finally:
            keyboard.remove_hotkey(stop_hotkey)

        print()  # move to next line after the carriage-return prints
        if self.stop_event.is_set():
            print("\nRun cancelled by user.")
        else:
            print("AFK time finished")

    def _from_minutes_to_seconds(self: Self) -> int:
        return self.time_minutes * 60

    def _wait_or_stop(self: Self, duration: float) -> bool:
        """Sleep with minimal CPU while honoring stop requests."""
        return self.stop_event.wait(duration)

    def _format_remaining_time(self: Self, remaining_seconds: int) -> str:
        """Return remaining time formatted as HH:MM:SS."""
        hours, remainder = divmod(remaining_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


if __name__ == "__main__":
    bot = NoAFK(time_minutes=60 * 6)
    bot.start()
