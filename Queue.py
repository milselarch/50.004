import copy


class Queue(object):
    def __init__(self, values=None):
        values = [] if values is None else values
        self.values = copy.deepcopy(values)

    def insert(self, value):
        self.values.append(value)

    def empty(self):
        return len(self.values) == 0

    def pop(self):
        value = self.values[0]
        self.values = self.values[1:]
        return value

    def __repr__(self):
        name = self.__class__.__name__
        return f'{name}({self.values})'