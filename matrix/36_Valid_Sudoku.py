class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        res = True

        #check each number individually
        for number in range(1,10):
            number = str(number)

            # check rows
            counter = 0
            for row in board:
                for symbol in row:
                    if symbol==number:
                        counter+=1
                    else:
                        pass
                if counter>1:
                    return False
                else:
                    pass
                counter = 0

            # check columns
            counter = 0
            for i in range(9):
                for j in range(9):
                    if number==board[j][i]:
                        counter+=1
                    else:
                        pass
                if counter>1:
                    return False
                else:
                    pass
                counter = 0

            # check squares
            counter = 0
            for r in range(3):
                square_rows = board[3*r:3*(r+1)]
                for c in range(3):
                    square = [sq_r[3*c:3*(c+1)] for sq_r in square_rows]
                    for row in square:
                        for el in row:
                            if number==el:
                                counter+=1
                            else:
                                pass
                    if counter > 1:
                        return False
                    else:
                        pass
                    counter = 0

        return res


board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
print(Solution().isValidSudoku(board))