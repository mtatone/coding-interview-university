from abc import ABC, abstractmethod


class NodeInterface(ABC):
    @property
    @abstractmethod
    def value(self):
        pass
    @value.setter
    def value(self):
        pass

    @property
    @abstractmethod
    def right(self):
        pass

    @right.setter
    def right(self):
        pass

    @property
    @abstractmethod
    def left(self):
        pass

    @left.setter
    def left(self):
        pass

    @abstractmethod
    def pre_order_traversal(self, head):
        pass

    @abstractmethod
    def post_order_traversal(self, head):
        pass

    @abstractmethod
    def in_order_traversal(self):
        pass

    @abstractmethod
    def print(self):
        pass


class BinaryTreeInterface(ABC):
    @property
    @abstractmethod
    def head(self):
        pass

    @head.setter
    def head(self):
        pass

    def print(self):
        pass


class MyBinaryTree(BinaryTreeInterface):
    def __init__(self, head):
        self.head = head
    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        self._head = value

    def print(self):
        self.head.print()


class MyNode(NodeInterface):
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left

    def pre_order_traversal(self):
        self.print()
        if self.left != None:
            self.left.pre_order_traversal()
            return
        elif self.right() != None:
            self.right.pre_order_traversal()
            return
        return

    def in_order_traversal(self):
        pass

    def post_order_traversal(self):
        pass

    def print(self):
        print(self.value)


head = MyNode(12)
head.left = MyNode(24)
head.left.right = MyNode(69)
head.left.left = MyNode(420)
#            12
#         24
#    420     69
#Pre Order: 12, 24, 420, 69
#In Oder: 420, 24, 69,12
#Post Order: 420, 69, 24, 12
head.pre_order_traversal()
head.print()