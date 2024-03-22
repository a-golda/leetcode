class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        raw_list = []
        col_list = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    raw_list.append(i)
                    col_list.append(j)

        raw_list = set(raw_list)
        col_list = set(col_list)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i in raw_list) or (j in col_list):
                    matrix[i][j] = 0

        return matrix

print(Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]]))