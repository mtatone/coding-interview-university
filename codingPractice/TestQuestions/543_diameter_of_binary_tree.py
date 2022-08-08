# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            Solution.max_diameter = 0
            height(root)
        return Solution.max_diameter


def height(node):
    if node is None:
        return 0
    else:
        left_height = height(node.left)
        right_height = height(node.right)
        temp_dia = left_height + right_height
        if temp_dia > Solution.max_diameter:
            Solution.max_diameter = temp_dia
        return max(left_height + 1, right_height + 1)