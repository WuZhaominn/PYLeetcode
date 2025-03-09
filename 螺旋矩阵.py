class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix),len(matrix[0])
        DIRS = (0,1),(1,0),(0,-1),(-1,0)    #右下左上
        ans = []
        i = j = di = 0  #i,j表示当前位置，di表示当前方向
        for q in range(m*n):
            ans.append(matrix[i][j])
            matrix[i][j] =None
            x,y = i +DIRS[di][0],j+DIRS[di][1]   #计算下一步位置
            #判断是否需要改变方向
            if x<0  or x>=m  or y<0 or y>=n or matrix[x][y]==None:
                di=(di+1)%4
            i +=DIRS[di][0]
            j +=DIRS[di][1]
        return ans
