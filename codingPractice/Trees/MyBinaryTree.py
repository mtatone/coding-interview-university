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
    def print(self):
        pass


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


def height(node):
    if node is None:
        return 0
    else:
        left_height = height(node.left)
        right_height = height(node.right)
        return max(left_height + 1, right_height + 1)


def width(node):
    if node is None:
        return 0
    left_height = height(node.left)
    right_height = height(node.right)
    left_width = width(node.left)
    right_width = width(node.right)

    return max((left_height + right_height + 1), left_width, right_width)


def is_full_tree(node):
    # every parent node/internal node has either 2 children or none
    # basically if any parent doesnt have 2 children then its not a full_tree
    if node is None:
        return
    if node.left is None and node.right is None:
        return True
    elif node.left is None or node.right is None:
        return False
    else:
        return is_full_tree(node.left) and is_full_tree(node.left)


def is_perfect_tree(node):
    # if a node has height greater than 0 (h > 0), and if both subtrees are of height h-1 then its a perfect tree
    if node is None:
        return
    node_height = height(node)
    if node_height > 0:
        if height(node.left) == (node_height - 1) and height(node.right) == (node_height - 1):
            if node.left is None and node.right is None:
                return True
            else:
                return is_perfect_tree(node.left) and is_perfect_tree(node.right)
        else:
            return False
    else:
        return True


def is_balanced_tree(node):
    # the heigh of the left subtree and the right subtree of any node differ by 1 or less
    if node is None:
        return
    if MyBinaryTree.height(node.left) - MyBinaryTree.height(node.right) < 2:
        if node.left is None and node.right is None:
            return True
        elif node.left is not None:
            return is_balanced_tree(node.left)
        elif node.right is not None:
            return is_balanced_tree(node.right)
        else:
            return is_balanced_tree(node.left) and is_balanced_tree(node.right)
    else:
        return False


def is_complete_tree(node):
    # essentially a full tree with the exception of the last leaft element might not have a right sibling
    # leafs might not have a right sibling
    if node is None:
        return
    if node.left is None and node.right is None:
        return True
    elif node.left is not None and node.right is None:
        return is_complete_tree(node.left)
    else:
        return is_complete_tree(node.left) and is_complete_tree(node.left)


def delete(root, node_to_delete):
    if root is None:
        return
    if root.left is None and root.right is None:
        if root.value == node_to_delete:
            return None
        else:
            return root

    q = [root]
    delete_me = None
    while len(q) != 0:
        node = q.pop(0)
        node.print()
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)

    # find the delete me node
    delete_me = head
    # while delete_me
    # find the deepest right node
    # set depest right node left and right to that of the deleteme
    # set the deleteme parents refrence to the deepest right node
    # set the deepest right node's parent regerence to the delte me
    # delete the delete me



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
print("\nWidth: {}".format(width(head)))
print("Height: {}".format(height(head)))

print("Level Insert")
head2 = MyNode(1)
head2.level_order_insert(MyNode(2))
head2.level_order_insert(MyNode(3))
head2.level_order_insert(MyNode(4))
head2.level_order_insert(MyNode(5))
head2.level_order_insert(MyNode(6))
# head2.level_order_insert(MyNode(7))
head2.print_level_order()
print("\nWidth: {}".format(width(head2)))
print("Height: {}".format(height(head2)))

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
print(is_full_tree(head2))
head3 = MyNode(1)
head3.level_order_insert(MyNode(2))
head3.level_order_insert(MyNode(3))
head3.level_order_insert(MyNode(4))
print(is_balanced_tree(head3))
# print(is_full_tree(root))
