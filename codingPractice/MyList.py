from abc import ABC, abstractmethod


class FormalListInterface(ABC):
    @property
    @abstractmethod
    def length(self) -> int:
        pass
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def get_item(self, index):
        pass
    @abstractmethod
    def _increment_length(self):
        pass
    @abstractmethod
    def add_item(self, item):
        pass

class ItemInterface(ABC):
    @property
    @abstractmethod
    def value(self):
        pass
    @abstractmethod
    def __init__(self, value):
        pass
    @abstractmethod
    def get_value(self):
        pass


class InformalListInterface:
    def get_length(self) -> int:
        pass

    def increment_length(self):
        pass


class MyList(FormalListInterface):
    def __init__(self):
        self.length = 0
        self.list = []

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    def get_item(self, index):
        return self.list[index]

    def _increment_length(self):
        self.length += 1

    def add_item(self, item):
        self._increment_length()
        self.list.append(item)


print("Displaying a simple list")
thelist = MyList()
print("list legth: {}".format(thelist.length))
thelist.add_item(item=5)
print("list legth: {}".format(thelist.length))
print("item in index {} is: {}".format(0, thelist.get_item(index=0)))
