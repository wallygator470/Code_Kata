import unittest

def done_or_not(board):
    blockNum = 0
    for row in range(9):
        if verify(board[row][0:]) == False:
            print(board[row][0:])
            print("Row: " + str(row))
            return "Try again!"
        else:
            print(board[row])
            print("Row: " + str(row))
        for col in range(9):
            if row == 0 and verify(getColumn(board, row, col)) == False:
                print(getColumn(board, 0, col))
                print("Col: " + str(col))
                return "Try again!"
            elif row == 0:
                print(getColumn(board, row, col))
                print("Col: " + str(col))
            
            if row in (0, 3, 6) and col in (0, 3, 6):
                if verify(getBlock(board, row, col)) == False:
                    print(getBlock(board, row, col))
                    print("Row: " + str(row) + ", Col: " + str(col) + ", Block: " + str(blockNum))
                    return "Try again!"
                else:
                    print(getBlock(board, row, col))
                    print("Row: " + str(row) + ", Col: " + str(col) + ", Block: " + str(blockNum))
                blockNum += 1
    return "Finished!"

def getColumn(board, rowNum, colNum):
    column = []
    for row in range(9):
        column.append(board[row + rowNum][colNum])
    return column

def getBlock(board, rowNum, colNum):
    block = []
    for row in range(3):
        for col in range(3):
            block.append(board[row + rowNum][col + colNum])
    return block

def verify(record):
    if len(set(record)) != 9:
        return False
    return True

board = [[1, 2, 3, 4, 5, 6, 7, 8, 9]
        ,[2, 3, 4, 5, 6, 7, 8, 9, 1]
        ,[3, 4, 5, 6, 7, 8, 9, 1, 2]
        ,[4, 5, 6, 7, 8, 9, 1, 2, 3]
        ,[5, 6, 7, 8, 9, 1, 2, 3, 4]
        ,[6, 7, 8, 9, 1, 2, 3, 4, 5]
        ,[7, 8, 9, 1, 2, 3, 4, 5, 6]
        ,[8, 9, 1, 2, 3, 4, 5, 6, 7]
        ,[9, 1, 2, 3, 4, 5, 6, 7, 8]]
print(done_or_not(board))

board = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]
print(done_or_not(board))

board = [[3, 3, 2, 5, 7, 9, 4, 6, 8]
        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]
print(done_or_not(board))

class Test(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]), 'Finished!')
    
    def test2(self):
        self.assertEqual(done_or_not([[3, 1, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]), 'Try again!')
    
if __name__ == '__main__':
    unittest.main()