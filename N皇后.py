class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 结果集
        ans = []
        
        # 初始化皇后位置、列占用、对角线占用
        queens = [0] * n  # 皇后放在 (r, queens[r])
        col = [False] * n  # 记录每列是否被占用
        diag1 = [False] * (n * 2 - 1)  # 记录主对角线是否被占用
        diag2 = [False] * (n * 2 - 1)  # 记录副对角线是否被占用
        
        # 开始回溯
        self.dfs(n, 0, queens, col, diag1, diag2, ans)
        return ans
    
    def dfs(self, n, r, queens, col, diag1, diag2, ans):
        # 返回条件：所有行都放置了皇后
        if r == n:
            ans.append(['.' * c + 'Q' + '.' * (n - 1 - c) for c in queens])
            return
        
        # 尝试在当前行的每一列放置皇后
        for c, ok in enumerate(col):
            # 检查是否冲突
            if not ok and not diag1[r + c] and not diag2[r - c]:
                # 放置皇后
                queens[r] = c
                col[c] = diag1[r + c] = diag2[r - c] = True
                
                # 递归处理下一行
                self.dfs(n, r + 1, queens, col, diag1, diag2, ans)
                
                # 撤销选择
                col[c] = diag1[r + c] = diag2[r - c] = False
