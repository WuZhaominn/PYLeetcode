class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        #ans：用于记录满足条件的路径数量
        #cnt：是一个字典，用于存储前缀和及其出现的次数。初始化时，cnt[0] = 1，表示前缀和为 0 的路径已经出现了一次（空路径）
        ans =0
        cnt = defaultdict(int)
        cnt[0] =1
        # s：从根节点到当前节点的路径和（前缀和）
        def dfs(node,s):
            if not node:
                return
            nonlocal ans
            #将当前节点的值累加到前缀和 s 中
            s +=node.val
            #如果存在一个前缀和 s - targetSum，则说明从某个节点到当前节点的路径和等于 targetSum
            ans +=cnt[s-targetSum]
            cnt[s] +=1
            dfs(node.left,s)
            dfs(node.right,s)
            cnt[s] -=1
        dfs(root,0)
        return ans
