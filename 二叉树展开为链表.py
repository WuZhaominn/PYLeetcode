class Solution:
    head =None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        self.flatten(root.right)
        self.flatten(root.left)
        root.left = None
        root.right =self.head
        self.head = root
