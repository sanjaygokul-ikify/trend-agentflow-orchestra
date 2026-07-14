import time

class Metrics:
    def __init__(self):
        self.start_time = time.time()

    def execution_time(self):
        return time.time() - self.start_time