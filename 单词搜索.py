class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n= len(board[0])
        for i in range(m):
            for j in range(n):
                if self.backtracking(board,word,i,j,0):
                    return True
        return False
    
    def backtracking(self,board,word,i,j,k):
        #说明当前路径无效
        if board[i][j] !=word[k]:
            return False
        #说明找到了正确路径
        if k == (len(word) - 1):
            return True
        #标记当前字符已经被访问
        board[i][j] = ''
        #向四个方向递归搜索
        for x,y in (i,j-1),(i-1,j),(i,j+1),(i+1,j):
            if 0<= x<len(board) and 0<=y <len(board[0]) and self.backtracking(board,word,x,y,k+1):
                return True
        
        board[i][j] = word[k]
        return False
