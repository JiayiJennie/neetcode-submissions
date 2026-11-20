class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowCount = [set() for _ in range(9)]
        colCount = [set() for _ in range(9)]
        squareCount = [set() for _ in range(9)]

        for x in range(9):
            for y in range(9):
                n = board[x][y]
                if n != ".":

                    if n in rowCount[x]:
                        return False
                    else:
                        rowCount[x].add(n)
                    
                    if n in colCount[y]:
                        return False
                    else: 
                        colCount[y].add(n)

                    square_id = int(x/3)*3 + int(y/3)
                    if n in squareCount[square_id]:
                        return False
                    else:
                        squareCount[square_id].add(n)

        return True
        