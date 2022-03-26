class Node(object):
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value})'


class LinkedList(object):
    def __init__(self, values=(), single=True):
        self.single = single
        self.head = None

        for value in values:
            self.add(value)

    def go_to_end(self):
        if self.head is None:
            return None

        node = self.head
        while node.next is not None:
            node = node.next

        return node

    def __repr__(self):
        name = self.__class__.__name__
        return f'{name}({self.to_list()})'

    def to_list(self):
        node_list = []
        node = self.head

        while node is not None:
            node_list.append(node)
            node = node.next

        return node_list

    def add(self, other):
        new_node = Node(value=other)

        if self.head is None:
            self.head = new_node
            return new_node

        end = self.go_to_end()
        end.next = new_node
        if not self.single:
            new_node.prev = end

        return new_node
