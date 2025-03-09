class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # i = m - 1（最后一行的索引）。
        # j = 0（第一列的索引）。
        #从左下角 (m-1, 0) 位置开始搜索
        i,j =len(matrix)-1,0
        while i>=0 and j <len(matrix[0]):
            if matrix[i][j] >target:
                i -=1
            elif matrix[i][j] <target:
                j+=1
            else:
                return True
                
