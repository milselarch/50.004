class HashMapUnchain(object):
    def __init__(self, size, hash_func):
        self.values = {k: None for k in range(size)}
        self.hash_func = hash_func

    def __getitem__(self, item):
        key = self.hash_func(item)
        return self.values[key]

    def __setitem__(self, key, value):
        hash_key = self.hash_func(key)
        assert (self.values[hash_key] is None) ^ (value is None)
        self.values[hash_key] = value

    def __len__(self):
        total = 0

        for k in self.values:
            if self.values[k] is not None:
                total += 1

        return total

    def __repr__(self):
        return f'{self.__class__.__name__}[{self.values}]'