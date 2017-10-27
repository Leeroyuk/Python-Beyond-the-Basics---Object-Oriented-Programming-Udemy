class MaxSizeList(object):
    def __init__(self, _max_len):
        self._max_len = _max_len
        self._lst = []

    def push(self, val):
        self._lst.append(val)
        if len(self._lst) > self._max_len:
            self._lst.pop(0)

    def get_list(self):
        return self._lst
