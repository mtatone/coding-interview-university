from abc import ABC, abstractmethod


class HashTableInterface(ABC):
    # @property
    # @abstractmethod
    # def hash_table(self):
    #     pass
    #
    # @hash_table.setter
    # def hash_table(self, value):
    #     pass

    @abstractmethod
    def hash_function(self, key):
        pass

    @abstractmethod
    def insert(self, kv):
        pass

    @abstractmethod
    def remove(self, key):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def print(self):
        pass


class KeyValuePairInterface(ABC):
    @property
    @abstractmethod
    def key(self):
        pass

    @key.setter
    def key(self, value):
        pass

    @property
    @abstractmethod
    def value(self):
        pass

    @value.setter
    def value(self, value):
        pass


class MyKeyValuePair(KeyValuePairInterface):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class MyHashTable(HashTableInterface):
    def __init__(self, length):
        self.hash_table = [None] * length

    def hash_function(self, key):
        return key % len(self.hash_table)

    def insert(self, kv):
        index = self.hash_function(kv[0])
        if self.hash_table[index] == None:
            self.hash_table[index] = [kv]
        else:
            for item in self.hash_table[index]:
                if item[0] == kv[0]:
                    item[1] = kv[1]
                    return
            self.hash_table[index].append(kv)

    def get(self, key):
        index = self.hash_function(key)
        for item in self.hash_table[index]:
            if item[0] == key:
                return item[1]
        return "Unable To Find Key"

    def remove(self, key):
        index = self.hash_function(key)
        for item_index, item in enumerate(self.hash_table[index]):
            if item[0] == key:
                if len(self.hash_table[index]) == 1:
                    self.hash_table[index] = None
                    return
                else:
                    del(self.hash_table[index][item_index])
                    return -1
        return "Unable To Find Key"

    def print(self):
        for item in self.hash_table:
            if item == None:
                print("[]")
            else:
                print(item)


hash_table = MyHashTable(10)
hash_table.insert([123, "Marco"])
hash_table.insert([323, "Marco Tee"])
hash_table.insert([321, "This is working"])
hash_table.print()
print("")
print(hash_table.get(123))
print("")
print(hash_table.get(321))
hash_table.insert([432, "Woah is this working?"])
hash_table.insert([909, "Woah is this working?"])
print("")
hash_table.print()
print("\nLets Try Removing something")
hash_table.remove(432)
hash_table.print()
