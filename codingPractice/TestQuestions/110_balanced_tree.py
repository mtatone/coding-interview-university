# Definition for a binary tree root.
class Treenode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def isBalanced(root):
        if root is None:
            return True
        if abs(height(root.left) - height(root.right)) < 2:
            if root.left is None and root.right is None:
                return True
            elif root.left is not None:
                return Solution.isBalanced(root.left)
            elif root.right is not None:
                return Solution.isBalanced(root.right)
            else:
                return Solution.isBalanced(root.left) and Solution.isBalanced(root.right)
        return False


def height(node):
    if node is None:
        return 0
    else:
        left_height = height(node.left)
        right_height = height(node.right)
        return max(left_height + 1, right_height + 1)

root = Treenode(1)
root.left = Treenode(2, left=Treenode(4, left=Treenode(7)), right=Treenode(5))
root.right = Treenode(3, right=Treenode(6, right=Treenode(8)))

result = Solution.isBalanced(root=root)

print(result)
