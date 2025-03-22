class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g= []
        for _ in range(numCourses):
            g.append([])
        # 将依赖关系 [a, b]（表示 b 是 a 的先修课）加入邻接表。g[b] 包含所有依赖课程 b 的后续课程 a
        for a,b in prerequisites:
            g[b].append(a)
        colors = [0] *numCourses
        def dfs(x):
            colors[x] =1   #正在访问中
            for y in g[x]:
                if colors[y] ==1 or colors[y] ==0 and dfs(y):
                    return True  #找到了环
            colors[x] =2  #完全访问完毕
            return False  #没有找到环
        for i,c in enumerate(colors):
            if c==0 and dfs(i):
                return False   #有环
        return True  #没有环
