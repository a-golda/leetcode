# class Solution(object):
#     def spiralOrder(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[int]
#         """
#         stage = 0 #0-right, 1-down, 2-left, 3-up
#         shrinking_counter = 0
#         m = len(matrix)
#         n = len(matrix[0])
#         res = []
#
#         while m>0 and n>=0:
#             if stage==0:
#                 for i in range(shrinking_counter,m):
#                     res.append(matrix[shrinking_counter][i])
#                 stage+=1
#             elif stage == 1:
#                 for i in range(shrinking_counter+1,n-1):
#                     res.append(matrix[i][n-1])
#                 stage += 1
#             elif stage == 2:
#                 for i in range(m-1,shrinking_counter,-1):
#                     res.append(matrix[m-1][i])
#                 stage += 1
#             elif stage == 3:
#                 for i in range(m-1, shrinking_counter, -1):
#                     res.append(matrix[i][shrinking_counter])
#                 n -= 1
#                 m -= 1
#                 stage += 1
#             else:
#                 pass
#
#             if stage > 3:
#                 stage = 0
#                 shrinking_counter += 1
#             else:
#                 pass
#
#         return res


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []

        while any(matrix):
            #top
            top = matrix.pop(0)
            for el in top:
                res.append(el)

            #right
            for row in matrix:
                res.append(row.pop())

            if not any(matrix):
                break
            else:
                pass

            # down
            down = reversed(matrix.pop(-1))
            for el in down:
                res.append(el)

            #left
            for row in matrix[::-1]:
                res.append(row.pop(0))

            if not any(matrix):
                break
            else:
                pass

        return res


matrix = [
    [ 1,  2,  3,  4,  5,  6,  7,  8,  9],
    [10, 11, 12, 13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24, 25, 26, 27],
    [28, 29, 30, 31, 32, 33, 34, 35, 36],
    [37, 38, 39, 40, 41, 42, 43, 44, 45],
    [46, 47, 48, 49, 50, 51, 52, 53, 54],
    [55, 56, 57, 58, 59, 60, 61, 62, 63],
    [64, 65, 66, 67, 68, 69, 70, 71, 72],
    [73, 74, 75, 76, 77, 78, 79, 80, 81]
]

# matrix = [[1,2,3],[4,5,6],[7,8,9]]

# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print(Solution().spiralOrder(matrix))