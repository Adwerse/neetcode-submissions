# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None

        queue = deque([root])

        while queue:
            val = queue.popleft()
            if val != None:
                val.left, val.right = val.right, val.left
                queue.append(val.left)
                queue.append(val.right)

        return root