class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        board_2 = [[board[i][j] for j in range(len(board[0]))] for i in range(len(board))]

        counter_0 = 0
        counter_1 = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                index_list = self.get_index(i, j, len(board), len(board[0]))
                for l in index_list:
                    if l[0]==i and l[1]==j:
                        pass
                    elif board[l[0]][l[1]] == 0:
                        counter_0+=1
                    else:
                        counter_1 += 1

                if board_2[i][j]==1 and (counter_1<2 or counter_1>3):
                    board_2[i][j] = 0
                elif board_2[i][j]==1 and (counter_1==2 or counter_1==3):
                    board_2[i][j] = 1
                elif board_2[i][j]==0 and counter_1==3:
                    board_2[i][j] = 1
                else:
                    pass
                counter_0 = 0
                counter_1 = 0

        return board_2

    @staticmethod
    def get_index(i, j, len_raw, len_col):
        index_list = [[i - 1, j - 1], [i - 1, j], [i - 1, j + 1],
                      [i, j - 1], [i, j], [i, j + 1],
                      [i + 1, j - 1], [i + 1, j], [i + 1, j + 1]]

        l = 0
        while l < len(index_list):
            if (index_list[l][0] < 0) or (index_list[l][0] >= len_raw) or (index_list[l][1] < 0) or (index_list[l][1] >= len_col):
                index_list.pop(l)
            else:
                l += 1
        return index_list


print(Solution().gameOfLife([[1,1],[1,0]]))


