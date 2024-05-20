# https://leetcode.com/problems/transpose-matrix/description/
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []
        for j in range(len(matrix[0])):
            column = []
            for i in range(len(matrix)):
                column.append(matrix[i][j])
            
            transpose.append(column)
        return(transpose)

            
