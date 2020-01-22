import json


class PyArray(object):
    def __init__(self):
        self.length = 0
        self._data = {}

    def __str__(self):
        response = {
            "length": self.length,
            "data": self._data
        }
        return json.dumps(response)

    @property
    def data(self):
        return self._data.values()

    def push(self, item):
        self._data[self.length] = item
        self.length += 1
        return self.length

    def delete(self, index):
        item = self._data[index]
        self._shift_items(index)
        return item

    def _shift_items(self, index):
        for index in list(self._data)[index:-1]:
            self._data[index] = self._data[index + 1]
        del self._data[self.length - 1]
        self.length -= 1
