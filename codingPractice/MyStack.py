from abc import ABC, abstractmethod


class MyStackInterface(ABC):
    @property
    @abstractmethod
    def is_empty(self):
        pass

    @is_empty.setter
    def is_empty(self, value):
        pass

    @property
    @abstractmethod
    def length(self):
        pass

    @property
    @length.setter
    def length(self, value):
        pass

    @property
    def head(self):
        pass

    @head.setter
    def head(self, value):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def push(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def clear(self):
        pass


class StackItemInterface(ABC):
    @property
    @abstractmethod
    def value(self):
        pass

    @value.setter
    def value(self, value):
        pass

    @property
    @abstractmethod
    def next(self):
        pass

    @next.setter
    def next(self, value):
        pass


class StackItem(StackItemInterface):
    def __init__(self, value):
        self.value = value
        self.next = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value


class MyStack(MyStackInterface):
    def __init__(self):
        self.is_empty = True
        self.length = 0
        self.head = None

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        self._head = value

    @property
    def is_empty(self):
        return self._is_empty

    @is_empty.setter
    def is_empty(self, value):
        self._is_empty = value

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    def pop(self):
        if self.is_empty:
            print("Stack Is Empty Dumb Dumb, I should raise an error")
            exit()
        elif self.head.next == None:
            item = self.head
            self.head = None
            self.length -= 1
            self.is_empty = True
            return item
        else:
            item = self.head
            while item.next != None:
                if item.next.next != None:
                    item = item.next
                else:
                    last_item = item.next.next
                    item.next = None
                    self.length -= 1
                    return last_item
            print("Unable to Pop From Stack")

    def push(self, item):
        if self.is_empty:
            self.head = item
        elif self.head.next == None:
            self.head.next = item
        else:
            itr_item = self.head
            is_end = False
            while not is_end:
                if itr_item.next == None:
                    itr_item.next = item
                    break
                else:
                    itr_item = itr_item.next
        self.length += 1
        self.is_empty = False

    def peek(self):
        if self.is_empty:
            print("Stack Is Empty Dumb Dumb, I should raise an error")
            exit()
        elif self.head.next == None:
            return self.head
        else:
            itr_item = self.head
            is_end = False
            while not is_end:
                if itr_item.next == None:
                    return itr_item
                else:
                    itr_item = itr_item.next

    @classmethod
    def clear_stack(cls, item):
        if item.next == None:
            return
        elif item.next != None:
            MyStack.clear_stack(item.next)
        item.next = None

    def clear(self):
        if self.is_empty:
            print("Stack Is Already Cleared")
            return
        elif self.head.next == None:
            self.head = None
            self.is_empty = True
            self.length = 0
        else:
            MyStack.clear_stack(self.head)
            self.is_empty = True
            self.length = 0
            self.head = None




the_stack = MyStack()
print(the_stack.is_empty)
the_stack.push(StackItem(12))
the_stack.push(StackItem(21))
print(the_stack.length)
print(the_stack.is_empty)
print(the_stack.peek().value)
the_stack.pop()
print(the_stack.length)
print(the_stack.is_empty)
the_stack.clear()
print(the_stack.is_empty)
