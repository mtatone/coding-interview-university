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

    # @abstractmethod
    # def pre_order_traversal(self):
    #     pass
    #
    # @abstractmethod
    # def post_order_traversal(self):
    #     pass
    #
    # @abstractmethod
    # def in_order_traversal(self):
    #     pass

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

    @classmethod
    def height(cls, node):
        if node is None:
            return 0
        else:
            left_height = MyBinaryTree.height(node.left)
            right_height = MyBinaryTree.height(node.right)
            return max(left_height + 1, right_height + 1)

    @classmethod
    def width(cls, node):
        if node is None:
            return 0
        left_height = MyBinaryTree.height(node.left)
        right_height = MyBinaryTree.height(node.right)
        left_width = MyBinaryTree.width(node.left)
        right_width = MyBinaryTree.width(node.right)

        return max((left_height + right_height + 1), left_width, right_width)

    #TODO:
    @classmethod
    def is_full_tree(cls, node):
        #every parent node/internal node has either 2 children or none
        # basically if any parent doesnt have 2 children then its not a full_tree
        if node is None:
            return
        if node.left is None and node.right is None:
            return True
        elif node.left is None or node.right is None:
            return False
        else:
            return MyBinaryTree.is_full_tree(node.left) and MyBinaryTree.is_full_tree(node.left)


    #TODO:
    @classmethod
    def is_perfect_tree(cls, node):
        # if a node has height greater than 0 (h > 0), and if both subtrees are of height h-1 then its a perfect tree
        if node is None:
            return
        node_height = MyBinaryTree.height(node)
        if node_height > 0:
            if MyBinaryTree.height(node.left) == (node_height - 1) and MyBinaryTree.height(node.right) == (node_height - 1):
                if node.left is None and node.right is None:
                    return True
                else:
                    return MyBinaryTree.is_perfect_tree(node.left) and MyBinaryTree.is_perfect_tree(node.right)
            else:
                return False
        else:
            return True

    #TODO:
    @classmethod
    def is_balanced_tree(cls, node):
        #the heigh of the left subtree and the right subtree of any node differ by 1 or less
        if node is None:
            return
        if MyBinaryTree.height(node.left) - MyBinaryTree.height(node.right) < 2:
            if node.left is None and node.right is None:
                return True
            elif node.left is not None:
                return MyBinaryTree.is_balanced_tree(node.left)
            elif node.right is not None:
                return MyBinaryTree.is_balanced_tree(node.right)
            else:
                return MyBinaryTree.is_balanced_tree(node.left) and MyBinaryTree.is_balanced_tree(node.right)
        else:
            return False


    #TODO:
    @classmethod
    def is_complete_tree(cls, node):
        #essentially a full tree with the exception of the last leaft element might not have a right sibling
        # leafs might not have a right sibling
        if node is None:
            return
        if node.left is None and node.right is None:
            return True
        elif node.left is not None and node.right is None:
            return MyBinaryTree.is_complete_tree(node.left)
        else:
            return MyBinaryTree.is_complete_tree(node.left) and MyBinaryTree.is_complete_tree(node.left)


class MyNode(NodeInterface):
    def __init__(self, value, left=None, right=None):
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

    def print_pre_order(self):
        self.print()
        if self.left:
            self.left.print_pre_order()
        if self.right:
            self.right.print_pre_order()

    def print_in_order(self):
        if self.left:
            self.left.print_in_order()
        self.print()
        if self.right:
            self.right.print_in_order()

    def print_post_order(self):
        if self.left:
            self.left.print_post_order()
        if self.right:
            self.right.print_post_order()
        self.print()

    def print(self):
        print(self.value, end=' ')

    def print_level_order(self):
        q = [self]
        while len(q) != 0:
            node = q.pop(0)
            node.print()
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

    def level_order_insert(self, node):
        q = [self]
        while len(q) != 0:
            curr_node = q.pop(0)
            if curr_node.left is not None:
                q.append(curr_node.left)
            else:
                curr_node.left = node
                return
            if curr_node.right is not None:
                q.append(curr_node.right)
            else:
                curr_node.right = node
                return


head = MyNode(12)
head.left = MyNode(24)
head.left.right = MyNode(69)
head.left.left = MyNode(420)
head.left.left.left = MyNode(21)
#            12
#         24
#    420     69
# Pre Order: 12, 24, 420, 69
# In Oder: 420, 24, 69,12
# Post Order: 420, 69, 24, 12

print("PreOrder")
head.print_pre_order()
print("\nInOrder")
head.print_in_order()
print("\nPostOrder")
head.print_post_order()
print("\nWidth: {}".format(MyBinaryTree.width(head)))
print("Height: {}".format(MyBinaryTree.height(head)))

print("Level Insert")
head2 = MyNode(1)
head2.level_order_insert(MyNode(2))
head2.level_order_insert(MyNode(3))
head2.level_order_insert(MyNode(4))
head2.level_order_insert(MyNode(5))
head2.level_order_insert(MyNode(6))
head2.level_order_insert(MyNode(7))
head2.print_level_order()
print("\nWidth: {}".format(MyBinaryTree.width(head2)))
print("Height: {}".format(MyBinaryTree.height(head2)))

root = MyNode(1)
root.left = MyNode(2)
root.right = MyNode(3)
root.left.left = MyNode(4)
root.right.left = MyNode(5)
root.right.right = MyNode(6)
root.right.left.left = MyNode(7)
root.right.left.right = MyNode(8)
print("\nPreOrder")
root.print_pre_order()
print("\nInOrder")
root.print_in_order()
print("\nPostOrder")
root.print_post_order()
print(MyBinaryTree.is_full_tree(head2))
head3 = MyNode(1)
head3.level_order_insert(MyNode(2))
head3.level_order_insert(MyNode(3))
head3.level_order_insert(MyNode(4))
print(MyBinaryTree.is_balanced_tree(head3))
# print(MyBinaryTree.is_full_tree(root))
