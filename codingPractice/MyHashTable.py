from abc import ABC, abstractmethod


class HashTableInterface(ABC):
    @property
    @abstractmethod
    def hash_table(self):
        pass

    @hash_table.setter
    def hash_table(self, value):
        pass

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
    def __init__(self):
        self.hash_table = [MyKeyValuePair("", ""), ] * 10

    @property
    def hash_table(self):
        return self._hash_table

    @hash_table.setter
    def hash_table(self, value):
        self._hash_table = value

    def hash_function(self, key):
        return key % 10

    def insert(self, kv):
        index = self.hash_function(kv.key)
        self.hash_table[index] = kv

    def remove(self, key):
        index = self.hash_function(key)
        self.hash_table[index] = MyKeyValuePair("", "")

    def print(self):
        for item in self.hash_table:
            print("[Key:{}, Value: {}]".format(item.key, item.value))


hash_table = MyHashTable()
hash_table.insert(MyKeyValuePair(20, "Hello World"))
hash_table.insert(MyKeyValuePair(321, "This is working"))
hash_table.insert(MyKeyValuePair(432, "Woah is this working?"))
hash_table.insert(MyKeyValuePair(909, "Woah is this working?"))
hash_table.print()
print("\nLets Try Removing something")
hash_table.remove(432)
hash_table.print()
