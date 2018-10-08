class MemoryError(Exception):
    def __init__(self, message):
        self.message = message

class IndexError(MemoryError):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
