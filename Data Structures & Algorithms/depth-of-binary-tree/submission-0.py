# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        a,b = 0,0
        if not root:
            return 0
        if root.left:
            a = self.maxDepth(root.left)
        if root.right:
            b = self.maxDepth(root.right)
        return max(a,b)+1