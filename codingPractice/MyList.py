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

    @abstractmethod
    def delete_item(self, index):
        pass


class ItemInterface(ABC):
    @property
    @abstractmethod
    def value(self):
        pass
    @value.setter
    def value(self, value):
        pass
    @abstractmethod
    def __init__(self, value):
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

    def get_item(self, index=False):
        if index:
            return self.list[index]
        else:
            return self.list[self.length - 1]

    def _increment_length(self):
        self.length += 1

    def _decrement_length(self):
        self.length -= 1

    def add_item(self, item):
        self._increment_length()
        self.list.append(item)

    def delete_item(self, index=False):
        if index:
            self.list.pop(index=index)
        else:
            self.list.pop()

        self._decrement_length()


class Item(ItemInterface):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


print("Displaying a simple list")
theList = MyList()
print("list legth: {}".format(theList.length))
theList.add_item(item=5)
print("list legth: {}".format(theList.length))
print("item in index {} is: {}".format(0, theList.get_item(index=0)))
theList.add_item(item=69)
print("list legth: {}".format(theList.length))
print("item in index {} is: {}".format(0, theList.get_item()))
theList.delete_item()
print("list legth: {}".format(theList.length))
print("item in index {} is: {}".format(0, theList.get_item()))

print("\nDisplaying a simple list but now using items class as well")
item = Item(69)
print("Item's value: {}".format(item.value))
itemList = MyList()
print("list legth: {}".format(itemList.length))
itemList.add_item(item=item)
print("New List legth: {}".format(itemList.length))
print("item in index {} is: {}".format(0, itemList.get_item(index=0).value))
