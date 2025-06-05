import sys
from datetime import datetime

class Logger:
    def __init__(self, out_stream, time_format):
        self.out_stream = out_stream
        self.time_format = time_format

    def log(self, message: str):
        timestamp = datetime.now().strftime(self.time_format)
        print(f"[{timestamp}] {message}", file=self.out_stream)
