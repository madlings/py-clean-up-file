import os


class CleanUpFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        # Called when entering the 'with' block
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Called when exiting the 'with' block
        if os.path.exists(self.filename):
            os.remove(self.filename)
