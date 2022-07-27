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


class MyLinkedList(FormalListInterface):
    def __init__(self):
        self.length = 0
        self.head = None

    @property
    def length(self) -> int:
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    def _increment_length(self):
        self.length += 1

    def _decrement_length(self):
        self.length -= 1

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        self._head = value

    def add_to_front(self, item):
        if self.head == None:
            self.head = item
        else:
            item.next_item = self.head
            self.head = item

    def add_item(self, item):
        if self.head == None:
            self.head = item
        else:
            last_item = self.head
            while last_item.next_item != None:
                last_item = last_item.next_item

            last_item.next_item = item
        self._increment_length()
        item.next_item = None

    def insert_after(self, item, ref):
        if self.head == None:
            self.head = item
        else:
            last_item = self.head
            while last_item.next_item != None:
                if last_item.value == ref:
                    item.next_item = last_item.next_item
                    last_item.next_item = item
                    self._increment_length()
                    return
                last_item = last_item.next_item
            if last_item.value == ref:
                item.next_item = last_item.next_item
                last_item.next_item = item
                self._increment_length()
                return
            else:
                print("unable to insert item")
                exit()

    def insert_before(self, item, ref):
        if self.head == None:
            self.head = item
        else:
            if self.head.value == ref:
                item.next_item = self.head
                self.head = item
                return
            last_item = self.head
            while last_item.next_item != None:
                if last_item.next_item.value == ref:
                    item.next_item = last_item.next_item
                    last_item.next_item = item
                    self._increment_length()
                    return
                last_item = last_item.next_item
            print("unable to insert item")
            exit()

    def delete_item(self, ref=False):
        if self.head == None:
            print("List is empty dumb dumb")
            exit()
        if ref:
            if self.head.value == ref:
                self.head = self.head.next_item
                return
            last_item = self.head
            while last_item.next_item != None:
                if last_item.next_item.value == ref:
                    last_item.next_item = last_item.next_item.next_item
                    self._decrement_length()
                    return

                last_item = last_item.next_item
        else:
            if self.head.next_item == None:
                self.head = None
                return
            last_item = self.head
            while last_item.next_item != None:
                if last_item.next_item.next_item == None:
                    last_item.next_item = None
                    self._decrement_length()
                    return
                last_item = last_item.next_item
        print("unable to delete item")
        exit()

    def delete_before(self, ref):
        if self.head == None:
            print("List is empty dumb dumb")
            exit()
        else:
            if self.head.value == ref:
                self.head = self.head.next_item
                return
            last_item = self.head
            while last_item.next_item != None:
                if last_item.next_item.next_item.value == ref:
                    last_item.next_item = last_item.next_item.next_item
                    self._decrement_length()
                    return
                last_item = last_item.next_item
            print("unable to delete item")
            exit()

    def delete_after(self, ref):
        if self.head == None:
            print("List is empty dumb dumb")
            exit()
        else:
            if self.head.value == ref:
                self.head = self.head.next_item
                return
            last_item = self.head
            while last_item.next_item != None:
                if last_item.value == ref:
                    last_item.next_item = last_item.next_item.next_item
                    self._decrement_length()
                    return
                if last_item.next_item.next_item.value == ref:
                    last_item.next_item = last_item.next_item.next_item
                    self._decrement_length()
                    return
                last_item = last_item.next_item
            print("unable to delete item")
            exit()

    @classmethod
    def print(cls, itm):
        print("Item Value: {}".format(itm.value))
        if itm.next_item != None:
            MyLinkedList.print(itm.next_item)


class Item(ItemInterface):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class LinkedItem(Item):
    def __init__(self, value, next_item=None):
        super(LinkedItem, self).__init__(value)
        self._next_item = next_item

    @property
    def next_item(self):
        return self._next_item

    @next_item.setter
    def next_item(self, next_item):
        self._next_item = next_item


print("\nDisplaying a linked list:")
linked_list = MyLinkedList()
linked_list.add_item(LinkedItem(69))
print("list legth: {}".format(linked_list.length))
linked_list.add_item(LinkedItem(23))
print("list legth: {}".format(linked_list.length))
print("Printing out linked list")
MyLinkedList.print(linked_list.head)
linked_list.insert_before(item=LinkedItem(26), ref=23)
print("Printing out linked list after insertion")
MyLinkedList.print(linked_list.head)
linked_list.delete_item()
print("Printing out linked list after deletion")
MyLinkedList.print(linked_list.head)
linked_list.insert_before(item=LinkedItem(420), ref=26)
linked_list.delete_item(420)
print("Printing out linked list after deletion")
MyLinkedList.print(linked_list.head)
linked_list.insert_after(item=LinkedItem(420), ref=69)
linked_list.insert_before(item=LinkedItem(69420), ref=26)
linked_list.insert_after(item=LinkedItem(6969), ref=26)
print("Printing out linked list after insertions")
MyLinkedList.print(linked_list.head)
linked_list.delete_after(ref=26)
linked_list.delete_before(ref=26)
linked_list.delete_before(ref=69)
linked_list.delete_after(ref=26)
print("Printing out linked list after deletions")
MyLinkedList.print(linked_list.head)
