class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(tree):
            if not tree:
                return 0
            ld = dfs(tree.left)
            rd = dfs(tree.right)
            nonlocal ans
            ans = max(ans, ld + rd)
            return max(ld, rd) + 1
        dfs(root)
        return ans
