class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if self.k == 0:
                return #直接从这里退出当前的递归调用
            self.k -=1
            if self.k==0:
                self.res = root.val
            dfs(root.right)
        self.k = k
        dfs(root)
        return self.res
