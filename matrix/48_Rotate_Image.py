# class Solution(object):
#     def rotate(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: None Do not return anything, modify matrix in-place instead.
#         """
#         matrix_2 = [[0 for _ in row] for row in matrix]
#         n = len(matrix)
#
#         for i in range(n):
#             for j in range(n):
#                 matrix_2[j][n-1-i] = matrix[i][j]
#
#         return matrix_2


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()

        return matrix

matrix = [[5,1,9,11],
          [2,4,8,10],
          [13,3,6,7],
          [15,14,12,16]]
print(Solution().rotate(matrix))


# (0, 0) -> (0, n)
# (0, 1) -> (1, n)
# (0, 2) -> (2, n)
# ...
# (1,0)->(0,n-1)
# (1,1) -> (1,n-1)
# ...
#
# (2,0) ->
#
# (0, n) -> (n, n)
