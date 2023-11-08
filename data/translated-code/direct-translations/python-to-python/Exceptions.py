class SillyError(Exception):
    def __init__(self, args=None):
        self.args = args