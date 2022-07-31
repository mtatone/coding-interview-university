from codingPractice.Trees.MyBinarySearchTree import delete, insert
from codingPractice.Trees.MyBinaryTree import height
import sys


class MyTreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.height = 1


class MyAVLTree(object):
    def insert_node(self, root, key):
        if root is None:
            return MyTreeNode(key)
        if root.value > key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balance_factor = self.get_balance(root)

        if balance_factor > 1:
            if key < root.left.value:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
        elif balance_factor < -1:
            if key > root.right.value:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rotate_left(self, root):
        if root is None:
            return root

        y = root.right
        T2 = root.right.left

        y.left = root
        root.right = T2

        # TODO: Update heights of nodes
        root.height = 1 + max(self.getHeight(root.left),
                           self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(root.left),
                           self.getHeight(root.right))
        return y

    def rotate_right(self, root):
        if root is None:
            return root

        y = root.left
        T3 = root.left.right

        y.right = root
        root.left = T3

        # TODO: Update heights of nodes
        root.height = 1 + max(self.getHeight(root.left),
                           self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    def delete_node(self, root, node):
        root = delete(root, node)
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balance_factor = self.get_balance(root)

        if balance_factor > 1:
            if self.get_balance(root.left) >= 0:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
        elif balance_factor < -1:
            if self.get_balance(root.right) <= 0:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)
        return root

    def preOrder(self, root):
        if not root:
            return
        print(root.value, end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)


def main():
    avlTree = MyAVLTree()
    root = None
    nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
    for num in nums:
        root = avlTree.insert_node(root, num)
    print("PreOrder Traversal After Creation")
    avlTree.preOrder(root)
    root = avlTree.delete_node(root, 10)
    print("\nPreOrder Traversal After Deletion")
    avlTree.preOrder(root)


if __name__ == "__main__":
    main()

