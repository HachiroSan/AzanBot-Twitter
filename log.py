import json
import os
from collections import deque
import datetime


class LogContainer:
    def __init__(self, max_size=50, file="logs.txt"):
        self.logs = deque(maxlen=max_size)
        self.file = file

    def add_log(self, log):
        try:
            # Get the current time
            now = datetime.datetime.now()

            # Format the timestamp as year, month, day, hour, minute, and second
            timestamp = now.strftime("[%Y-%m-%d %H:%M:%S]")
            self.logs.append((timestamp, log))
            with open(self.file, "a") as f:
                f.write(f"{timestamp}: {log}\n")
        except Exception as e:
            print(f"Error adding log: {e}")

    def get_logs(self):
        try:
            return list(self.logs)
        except Exception as e:
            print(f"Error getting logs: {e}")
            return []

    def clear_logs(self):
        self.logs.clear()
