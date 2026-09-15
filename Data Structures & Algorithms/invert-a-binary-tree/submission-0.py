# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:          # база: пустое поддерево — нечего разворачивать
            return None

        root.left, root.right = root.right, root.left   # меняем детей местами на ЭТОМ узле

        self.invertTree(root.left)    # рекурсивно разворачиваем то, что стало left
        self.invertTree(root.right)   # рекурсивно разворачиваем то, что стало right

        return root