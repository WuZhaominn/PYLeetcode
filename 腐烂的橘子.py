class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n =len(grid),len(grid[0])
        #处理特殊情况   没有好橘子
        q=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    q+=1
        if q==0:
            return 0
        #烂橘子存进queue里
        queue = []
        #先找出所有的烂橘子
        for i in range(m):
            for j in range(n):
                if grid[i][j] ==2:
                    queue.append((i,j))
        round =-1
        #一层一层找烂橘子
        while queue:
            current_len = len(queue)
            #队列中所有的烂橘子，每个烂橘子都要在一次的时间内感染四周
            for l in range(current_len):
                i,j = queue.pop(0)
                #一个烂橘子的四周
                for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                    temp_i = i+x
                    temp_j = j+y
                    if temp_i>=0 and temp_i <m and temp_j>=0 and temp_j<n and grid[temp_i][temp_j]==1:
                        grid[temp_i][temp_j]=2
                        queue.append((temp_i,temp_j))
            round+=1            

        for eachm in grid:
            if 1 in eachm:
                return -1
        return round
        
