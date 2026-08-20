class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHashes = defaultdict(set)
        colHashes = defaultdict(set)
        threeBy3Hashes = defaultdict(set)
        for row in range(0, len(board)):
            for col in range(0, len(board[row])):
                cell = board[row][col]
                if cell == ".": continue
                # row
                if (cell not in rowHashes[row]):
                    rowHashes[row].add(cell)
                else:
                    return False
                # col
                if (cell not in colHashes[col]):
                    colHashes[col].add(cell)
                else:
                    return False
                # do math to decide which 3x3 this cell is in
                ninth = math.floor(row/3) * 3 + math.floor(col/3)
                if (cell not in threeBy3Hashes[ninth]):
                    threeBy3Hashes[ninth].add(cell)
                else:
                    return False
        return True 
