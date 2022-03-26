import copy


class HashMap(object):
    def __init__(
        self, values=None, size=40, max_load_factor=None,
        hash_func=None, resize_factor=2, fill_all_keys=False,
        probing=False
    ):
        if hash_func is None:
            hash_func = self.mod_hash

        self.size = size
        self.hash_func = hash_func
        self.fill_all_keys = fill_all_keys
        self.max_load_factor = max_load_factor
        self.resize_factor = resize_factor
        self.probing = probing
        self.mapping = {}

        if values is not None:
            self.add_values(values)

    def get_full_keys(self):
        return list(range(self.size))

    def resort_keys(self):
        if self.fill_all_keys:
            keys = self.get_full_keys()
        else:
            keys = list(self.mapping.keys())

        keys = sorted(keys)
        new_mapping = {}

        for key in keys:
            if key not in self.mapping:
                new_mapping[key] = []
                continue

            new_mapping[key] = self.mapping[key]

        self.mapping = new_mapping

    def add_values(self, values, verbose=False):
        for value in values:
            self.add(value, verbose=verbose)

    @staticmethod
    def mod_hash(size, k, i=0):
        return int((k+i) % size)

    def max_allowed_load(self):
        if self.max_load_factor is None:
            return None

        return self.size * self.max_load_factor

    def get_all_values(self):
        all_values = []
        for key in self.mapping:
            all_values.extend(self.mapping[key])

        return all_values

    def get_load(self):
        return len(self.get_all_values())

    def load_factor(self):
        return self.get_load() / self.get_slots()

    def get_slots(self):
        return self.size

    def __repr__(self):
        name = self.__class__.__name__
        return f'{name}({self.mapping}, size={self.size})'

    def add(self, value, verbose=False):
        key = self.hash_func(self.size, value, i=0)
        key = self.mod_hash(self.size, key)
        assert type(key) is int
        assert self.size > key >= 0

        if key not in self.mapping:
            self.mapping[key] = []

        if self.probing:
            i = 0
            while True:
                key = self.hash_func(self.size, value, i=i)
                key = self.mod_hash(self.size, key)

                if key not in self.mapping:
                    self.mapping[key] = []

                if not self.mapping.get(key, []):
                    self.mapping[key].append(value)
                    break

                i += 1
        else:
            self.mapping[key].append(value)

        self.resort_keys()

        if verbose:
            print(f'adding {value} - {self}')
            print(f'load factor = {self.load_factor()}')
            print(f'max allowed load = {self.max_allowed_load()}')
            print(f'load = {self.get_load()}')
            print('')

        if self.max_load_factor is None:
            return

        elif self.load_factor() > self.max_load_factor:
            new_size = self.size * self.resize_factor
            if verbose:
                print('REHASHING', new_size)

            new_hashmap = HashMap(
                values=self.get_all_values(),
                max_load_factor=self.max_load_factor,
                size=new_size, hash_func=self.hash_func
            )

            self.size = new_size
            self.mapping = new_hashmap.mapping
            self.resort_keys()

            if verbose:
                print(f'rehashing after {value} - {self}')
                print(f'load = {self.get_load()}')

            return self

    def __getitem__(self, key):
        try:
            assert self.size > key >= 0
            assert type(key) is int
        except AssertionError as e:
            print(f'BAD KEY {key}')
            raise e

        if key in self.mapping:
            return self.mapping[key]
        else:
            return []
