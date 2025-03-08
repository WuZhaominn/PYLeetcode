#不是原地算法
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return 
        zero = []
        m,n=len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero.append((i,j))
        

        while len(zero) > 0:
            x,y =zero.pop()
            for i in range (m):
                for j in range(n):
                    if i==x or j ==y:
                        matrix[i][j] =0
        return 
#原地算法
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return 
        m,n=len(matrix),len(matrix[0])
        first_col_has_zero =False
        first_row_has_zero =False

        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero =True
                break

        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero =True
                break
                    
        

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] ==0:
                    matrix[i][0]=0
                    matrix[0][j]=0

        for i in range(1,m):
            if matrix[i][0] ==0:
                for j in range(1,n):
                    matrix[i][j] =0

        for j in range(1,n):
            if matrix[0][j] ==0:
                for i in range(1,m):
                    matrix[i][j] =0


        if  first_row_has_zero:
            for j in range(n):
                matrix[0][j]=0

        if first_col_has_zero:
            for i in range(m):
                matrix[i][0]=0

