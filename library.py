class Array(object):
    """
    Yes, this is an Array implementation
    indexed from 1 made just for algo homework
    """
    def __init__(self, *items):
        self.negative_indexing = True

        if len(items) == 0:
            self.items = []
        elif type(items[0]) in (list, tuple):
            assert len(items) == 1
            self.items = items[0]
        else:
            self.items = list(items)

    def copy(self):
        return Array(self.items[::])

    def pop(self):
        return self.items.pop()

    def __iter__(self):
        for item in self.items:
            yield item

    def __add__(self, other):
        if type(other) is list:
            return self.__class__(self.items + other)
        elif isinstance(other, Array):
            return self.__class__(self.items + other.items)
        else:
            raise NotImplementedError(f'unknown type {other}')

    def get(self, index, default=None):
        if index <= len(self):
            return self[index]

        return default

    def __contains__(self, item):
        return item in self.items

    def append(self, item):
        self.items.append(item)

    def __eq__(self, other):
        return self.items == other.items

    def __delitem__(self, key):
        del self.items[self.translate_index(key)]

    def __getitem__(self, index):
        if isinstance(index, slice):
            if index == slice(None):
                return self.__class__(self.items[::])

            if index.stop is None:
                # e.g. A[2:]
                assert index.start > 0
                new_slice = slice(
                    self.translate_index(index.start),
                    None, index.step
                )
                return self.__class__(self.items[new_slice])

            if index.stop < 0:
                assert index.start is None
                assert index.step is None
                return self.__class__(self.items[index])
            else:
                start = None
                if index.start is not None:
                    start = self.translate_index(index.start)

                stop, step = index.stop, index.step
                return self.__class__(self.items[start:stop:step])

        new_index = self.translate_index(index)
        return self.items[new_index]

    def to_tuple(self):
        return tuple(self.items)

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
            str_items = ', '.join([
                repr(item) for item in self.items
            ])

        return f"{self.__class__.__name__}({str_items})"


class FixedArray(Array):
    def __init__(self, *items):
        super().__init__(*items)
        self.items = tuple(self.items)

    def append(self, item):
        raise TypeError('Array is fixed')

    def pop(self):
        raise TypeError('Array is fixed')

    def __hash__(self):
        return hash(tuple(self.items))


class Queue(object):
    """
    double stack implementation of a queue
    """
    def __init__(self, items=()):
        self._items = []
        self.reverse_items = []

        for item in items:
            self.put(item)

    def put(self, item):
        self._items.append(item)

    def transfer_stack(self):
        while len(self._items) > 0:
            self.reverse_items.append(self._items.pop())

    @property
    def is_empty(self):
        return len(self._items) == len(self.reverse_items) == 0

    @property
    def items(self):
        return self.get_items()

    def get_items(self):
        return self._items + self.reverse_items[::-1]

    def pop(self):
        if len(self.reverse_items) == 0:
            self.transfer_stack()

        item = self.reverse_items.pop()
        return item

    def __repr__(self):
        all_items = self.get_items()
        return self.__class__.__name__ + (
            f'({[item for item in all_items]})'
        )


if __name__ == '__main__':
    a = Array(1,2,3,4)
    a[1] = 24
    print(a)