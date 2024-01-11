class Node(object):
    def __init__(self, key, value, prev_node=None, next_node=None):
        self.key = key
        self.value = value

        self.prev = prev_node
        self.next = next_node

    def to_str(self):
        return f'Node({self.key}, {self.value})'

    def __repr__(self):
        prev_key = None
        next_key = None

        if self.prev is not None:
            prev_key = self.prev.key
        if self.next is not None:
            next_key = self.next.key

        return (
            f'Node({self.key}, {self.value}, {prev_key}, {next_key})'
        )


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        # self.ordering = None
        self.start_head = None
        self.last_node = None
        self.capacity = capacity

    def print_ordering(self):
        node_list = self.get_ordering_list()
        print(node_list)

    def get_ordering_list(self):
        head = self.start_head
        node_list = []

        count = 0
        while head is not None:
            node_list.append(head)
            head = head.next
            count += 1

            if count > 100:
                print(node_list)
                raise ValueError

        return node_list

    def get(self, key: int) -> int:
        # print('GET', key, self.cache)
        # self.print_ordering()

        if key in self.cache:
            if len(self.cache) == 1:
                node = self.cache[key]
                assert len(self.get_ordering_list()) == len(self.cache)
                return node.value
            else:
                start_ordering_list = self.get_ordering_list()
                node = self.cache[key]
                prev_start_head = self.start_head

                if node.prev is not None:
                    # current node is not first node
                    prev_node = node.prev
                    prev_node.next = node.next

                    if node.next is None:
                        self.last_node = prev_node
                        self.last_node.next = None
                    else:
                        node.next.prev = prev_node

                    node.prev = None
                    node.next = self.start_head

                    self.start_head = node
                    self.start_head.prev = None
                    self.start_head.next = prev_node
                else:
                    # current node is first node
                    self.start_head.prev = None

                if self.start_head != prev_start_head:
                    self.start_head.next = prev_start_head

                if self.start_head.next == self.last_node:
                    # cache has only 2 elements
                    self.last_node.next = None
                    self.last_node.prev = self.start_head

                if self.start_head.next is not None:
                    self.start_head.next.prev = self.start_head
                if self.last_node.prev is not None:
                    self.last_node.prev.next = self.last_node

                self.get_ordering_list()
                assert len(self.get_ordering_list()) == len(self.cache)
                return node.value
        else:
            self.get_ordering_list()
            return -1

    def put(self, key: int, value: int) -> None:
        # print('PUT', (key, value), self.start_head, self.last_node)
        if self.last_node is not None:
            self.last_node.next = None

        self.print_ordering()

        if key in self.cache:
            # print('OLD_NODE')
            node = self.cache[key]
            node.value = value

            if node.prev is not None:
                prev_node = node.prev
                next_node = node.next
                prev_node.next = next_node

                node.next = self.start_head
                self.start_head.prev = node
                self.start_head = node

                if next_node is None:
                    self.last_node = prev_node
                    self.last_node.next = None

        elif len(self.cache) < self.capacity:
            # cache is under max capacity
            new_node = Node(key, value, next_node=self.start_head)
            self.cache[key] = new_node
            self.start_head = new_node

            if self.last_node is None:
                # print('REASSIGN_START')
                self.last_node = self.start_head
                self.last_node.next = None
            elif self.start_head.next == self.last_node:
                # cache has only 2 elements
                self.last_node.next = None
                self.last_node.prev = self.start_head
            else:
                self.last_node.next = None

            if self.start_head.next is not None:
                self.start_head.next.prev = self.start_head

        else:
            # cache is at max capacity
            new_node = Node(key, value, next_node=self.start_head)
            self.cache[key] = new_node
            self.start_head.prev = new_node
            self.start_head = new_node

            if self.last_node is not None:
                # print('CACHE', self.cache)
                del self.cache[self.last_node.key]
                prev_last_node = self.last_node.prev

                self.last_node.prev = None
                self.last_node.next = None

                self.last_node = prev_last_node
                self.last_node.next = None
            else:
                self.last_node = new_node
                self.last_node.next = None

        ordering = self.get_ordering_list()
        assert len(ordering) == len(self.cache)

        if (self.last_node is not None) and (len(self.cache) > 1):
            assert self.last_node.prev is not None

        # print('END_STATE')
        # self.print_ordering()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    """
    commands = [
        "LRUCache", "put", "put", "get", "put", "get",
        "put", "get", "get", "get"
    ]
    params = [
        [2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]
    ]
    """
    """
    commands = ["LRUCache", "put", "put", "put", "put", "get", "get"]
    params = [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]]
    """

    commands = [
        "LRUCache", "put", "put", "put", "put", "get", "get",
        "get", "get", "put", "get", "get", "get", "get", "get"
    ]
    params = [
        [3], [1, 1], [2, 2], [3, 3], [4, 4], [4], [3], [2],
        [1], [5, 5], [1], [2], [3], [4], [5]
    ]

    cache = None
    items = zip(commands, params)
    output = []

    for k, item in enumerate(items):
        command, param = item
        print(f'COMMAND [{k}]', command, param)

        if command == 'LRUCache':
            cache = LRUCache(*param)
            output.append(None)
        elif command == "put":
            cache.put(*param)
            output.append(None)
        elif command == "get":
            value = cache.get(*param)
            output.append(value)

        print('CACHE', cache.cache)
        cache.print_ordering()
        print(f'OUTPUT [{k}]', output)
        print('')

    print('OUTPUT', output)
