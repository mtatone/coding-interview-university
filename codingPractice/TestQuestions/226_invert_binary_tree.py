# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


nodes = []


class Solution:
    @staticmethod
    def invertTree(root):
        in_order_get(root)
        print(nodes)
        in_order_set(root)
        return root


def in_order_get(node):
    if node is None:
        return
    if node.right is not None and node.left is None:
        nodes.append(None)
    if node.left is not None:
        in_order_get(node.left)
    nodes.append(node.val)
    if node.left is not None and node.right is None:
        nodes.append(None)
    if node.right is not None:
        in_order_get(node.right)


def in_order_set(node):
    if node is None:
        return
    if node.right is not None and node.left is None:
        node.right = TreeNode(nodes.pop(-1))
    if node.left is not None:
        in_order_set(node.left)
    popped_value = nodes.pop(-1)
    if popped_value is None:
        node.val = "null"
    else:
        node.val = popped_value
    if node.left is not None and node.right is None:
        node.left = TreeNode(nodes.pop(-1))
    if node.right is not None:
        in_order_set(node.right)

#    if node is None:
#        return
#    if node.left is not None:
#        in_order_set(node.left)
#    node.val = nodes.pop(-1)
#    if node.right is not None:
#        in_order_set(node.right)
root = TreeNode(val=1, left=TreeNode(2))
Solution.invertTree(root=root)
print("cunt")
