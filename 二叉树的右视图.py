class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node,depth):
            if not node:
                return
            if depth ==len(ans):
                ans.append(node.val)
            dfs(node.right,depth+1)
            dfs(node.left,depth+1)
        dfs(root,0)
        return ans
