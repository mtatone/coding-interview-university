
from codingPractice.MySinglyLinkedList import LinkedItem
from codingPractice.MySinglyLinkedList import MyLinkedList


class DoublyLinkedItem(LinkedItem):
    def __init__(self, value):
        super(DoublyLinkedItem, self).__init__(value)
        self._previous_item = None
    @property
    def previous_item(self):
        return self._previous_item

    @previous_item.setter
    def previous_item(self, value):
        self._previous_item = value


class MyDoublyLinkedList(MyLinkedList):
    def add_to_front(self, item):
        super(MyDoublyLinkedList, self).__init__(item)
        item.previous_item = self.head

    def add_item(self, item):
        if self.head == None:
            self.head = item
            item.previous_item = None
        else:
            last_item = self.head
            while last_item.next_item != None:
                last_item = last_item.next_item

            last_item.next_item = item
            item.previous_item = last_item
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
                    item.previous_item = last_item
                    self._increment_length()
                    return
                last_item = last_item.next_item
            if last_item.value == ref:
                item.next_item = last_item.next_item
                last_item.next_item = item
                item.previous_item = last_item
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
                self.head.previous_item = item
                self.head = item
                return
            last_item = self.head
            while last_item.next_item != None:
                if last_item.next_item.value == ref:
                    item.next_item = last_item.next_item
                    last_item.next_item.previous_item = item
                    last_item.next_item = item
                    item.previous_item = last_item
                    self._increment_length()
                    return
                last_item = last_item.next_item
            print("unable to insert item")
            exit()

    def delete_item(self, ref=False):
        if self.head == None:
            print("The list is empty dumb dumb")
        if ref:
            if self.head.value == ref:
                self.head = self.head.next_item
                self.head.previous_item = None
                return
            last_item = self.head
            while last_item.next_item != None:
                if last_item.value == ref:
                    if last_item.next_item == None:
                        last_item.previous_item.next_item = None
                    else:
                        last_item.next_item.previous_item = last_item.previous_item
                        last_item.previous_item.next_item = last_item.next_item
                    return
                last_item = last_item.next_item
            print("Unable to delete item")
            exit()
        else:
            last_item = self.head
            while last_item.next_item != None:
                if last_item.next_item.next_item == None:
                    last_item.next_item = None
                    return
                last_item = last_item.next_item
            print("Unable to delete item")
            exit()

    def delete_before(self, ref):
        if self.head.value == ref:
            self.head = self.head.next_item
            self.head.previous_item = None
        else:
            last_item = self.head
            while last_item.next_item != None:
                if last_item.next_item.value == ref:
                    last_item.next_item.previous_item = last_item.previous_item
                    last_item.previous_item.next_item = last_item.next_item
                    return
                last_item = last_item.next_item
            print("Unable to delete item")
            exit()

    def delete_after(self, ref):
        if self.head.value == ref:
            self.head.next_item = self.head.next_item.next_item
            self.head.next_item.next_item.previous_item = self.head
        else:
            last_item = self.head
            while last_item.next_item != None:
                if last_item.next_item.value == ref:
                    if last_item.next_item.next_item == None:
                        self.delete_item()
                        return
                    if last_item.next_item.next_item.next_item == None:
                        last_item.next_item.next_item = None
                    else:
                        last_item.next_item.next_item.next_item.previous_item = last_item.next_item
                        last_item.next_item.next_item = last_item.next_item.next_item.next_item
                        last_item.next_item.previous_item = last_item.previous_item
                        last_item.previous_item.next_item = last_item.next_item
                    return
                last_item = last_item.next_item
            print("Unable to delete item")
            exit()



    @classmethod
    def print(cls, itm):
        if itm.previous_item != None:
            previous_item_value = itm.previous_item.value
        else:
            previous_item_value = "None"
        if itm.next_item != None:
            next_item_value = itm.next_item.value
        else:
            next_item_value = "None"
        print("Item Value: {}, Prev_Item_value: {}, Next_Item_value: {}".format(itm.value, previous_item_value, next_item_value))
        if itm.next_item != None:
            MyDoublyLinkedList.print(itm.next_item)

print("\nDisplaying a doubly linked list:")
linked_list = MyDoublyLinkedList()
linked_list.add_item(DoublyLinkedItem(69))
print("list legth: {}".format(linked_list.length))
linked_list.add_item(DoublyLinkedItem(23))
print("list legth: {}".format(linked_list.length))
print("Printing out linked list")
MyDoublyLinkedList.print(linked_list.head)
linked_list.insert_before(item=DoublyLinkedItem(26), ref=23)
print("Printing out linked list after insertion")
MyDoublyLinkedList.print(linked_list.head)
linked_list.delete_item()
print("Printing out linked list after deletion")
MyDoublyLinkedList.print(linked_list.head)
linked_list.insert_before(item=DoublyLinkedItem(420), ref=26)
print("Printing out linked list after inserting before")
MyDoublyLinkedList.print(linked_list.head)
linked_list.delete_item(420)
print("Printing out linked list after deletion")
MyDoublyLinkedList.print(linked_list.head)
linked_list.insert_after(item=DoublyLinkedItem(420), ref=69)
linked_list.insert_before(item=DoublyLinkedItem(69420), ref=26)
linked_list.insert_after(item=DoublyLinkedItem(6969), ref=26)
print("Printing out linked list after insertions")
MyDoublyLinkedList.print(linked_list.head)
linked_list.delete_after(ref=26)
linked_list.delete_before(ref=26)
linked_list.delete_before(ref=69)
linked_list.delete_after(ref=26)
print("Printing out linked list after deletions")
MyDoublyLinkedList.print(linked_list.head)
