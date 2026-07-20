class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None

        #swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(4)

sol = Solution()
inverted = sol.invertTree(root)
print(inverted.left.val)