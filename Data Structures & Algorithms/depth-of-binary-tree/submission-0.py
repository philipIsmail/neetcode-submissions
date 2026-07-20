# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        leftdepth = self.maxDepth(root.left)
        rightdepth = self.maxDepth(root.right)

        return 1 + max(leftdepth, rightdepth)


example = TreeNode(1)
example.left = TreeNode(2)
example.right = TreeNode(3)
example.right.left = TreeNode(4)
example.right.left.left = TreeNode(5)
example.right.left.left.left = TreeNode(6)
example.right.left.left.left.left = TreeNode(7)

sol = Solution()

print(sol.maxDepth(example))