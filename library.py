class Array(object):
    def __init__(self, *items):
        self.negative_indexing = True

        if len(items) == 0:
            self.items = []
        elif type(items[0]) in (list, tuple):
            assert len(items) == 1
            self.items = items[0]
        else:
            for item in items:
                assert type(item) in (float, int)

            self.items = list(items)

    def pop(self):
        return self.items.pop()

    def get(self, index, default=None):
        if index <= len(self):
            return self[index]

        return default

    def __contains__(self, item):
        return item in self.items

    def append(self, item):
        self.items.append(item)

    def __delitem__(self, key):
        del self.items[self.translate_index(key)]

    def __getitem__(self, index):
        if isinstance(index, slice):
            assert index.stop < 0
            return self.items[index]

        new_index = self.translate_index(index)
        return self.items[new_index]

    def disable_negative_indexing(self):
        self.negative_indexing = False

    def translate_index(self, index):
        if index > 0:
            return index - 1
        else:
            assert self.negative_indexing
            assert index != 0
            return index

    def __setitem__(self, key, value):
        new_index = self.translate_index(key)
        self.items[new_index] = value

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        if len(self.items) == 0:
            str_items = ''
        else:
            str_items = ', '.join([str(item) for item in self.items])

        return f"{self.__class__.__name__}({str_items})"


if __name__ == '__main__':
    a = Array(1,2,3,4)
    a[1] = 24
    print(a)