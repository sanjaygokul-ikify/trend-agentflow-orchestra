from .executor import Executor


class Runtime:
    def __init__(self):
        self.executor = Executor()

    def run(self):
        self.executor.execute()