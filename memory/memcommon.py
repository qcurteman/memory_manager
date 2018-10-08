class MemoryCommon:
    row_size = 0

    @classmethod
    def invalid_index(cls, index):
        if index < 0:
            return True
        else:
            return False