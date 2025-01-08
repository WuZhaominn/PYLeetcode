class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #深度优先搜索，搜索到的1就会变为0，这样不会被重复搜索
        def dfs(grid,i,j):
            grid[i][j]='0'
            m,n = len(grid),len(grid[0])

            for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if x>=0 and x<m and y>=0 and y<n and grid[x][y]=='1':
                    dfs(grid,x,y)
                


        if not grid:
            return 0
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    ans+=1
                    dfs(grid,i,j)
        return ans           
        
