class HashTable(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * self.capacity

    def _hash(self, key):
        hashsum = 0
        for index, char in enumerate(key):
            hashsum += (index + len(key)) ** ord(char)
        hashsum = hashsum % self.capacity
        return hashsum

    def set(self, key, value):
        address = self._hash(key)
        if self.data[address] is None:
            self.data[address] = []
        self.data[address].append([key, value])

    def get(self, key):
        address = self._hash(key)
        buckets = self.data[address]
        if buckets is not None:
            for bucket in buckets:
                if bucket[0] == key:
                    return bucket[1]
        return None

    def keys(self):
        keys = []
        for buckets in self.data:
            if (isinstance(buckets, list)):
                for bucket in buckets:
                    keys.append(bucket[0])
        return keys
