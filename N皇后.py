class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        # 记录每行皇后的列位置。queens[r] 表示第 r 行的皇后放在第 queens[r] 列。
        queens = [0] * n
        #记录每列是否被占用。
        col = [False] * n
        #记录主对角线是否被占用
        diag1 = [False] *(n*2-1)
        #记录副对角线是否被占用
        diag2 = [False] *(n*2-1)
        self.backtracking(n,0,queens,col,diag1,diag2,res)
        return res

    def backtracking(self,n,row,queens,col,diag1,diag2,res):
        if row == n:
            res.append(['.' * c + 'Q' +'.'*(n-1-c)  for c in queens])
            return
        #尝试在当前行的每一列放置皇后
        for c,ok in enumerate(col):
            #检查是否冲突
            if not ok and not diag1[row+c] and not diag2[row-c]:
                #放置皇后
                queens[row] =c
                col[c] = diag1[row+c] = diag2[row-c] = True
                self.backtracking(n,row+1,queens,col,diag1,diag2,res)
                col[c] = diag1[row+c] =diag2[row-c] =False
