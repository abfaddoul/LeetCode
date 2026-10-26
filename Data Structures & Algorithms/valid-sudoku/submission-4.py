class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            seen = set()
            for n in row:
                if n == '.':
                    continue
                if n in seen:
                    return False
                seen.add(n)

        for j in range(len(board[0])):
            seen = set()
            for i in range(len(board)):
                if board[i][j] == '.':
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        boxes = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in boxes[(i//3, j//3)] :
                    return False
                boxes[(i//3, j//3)].add(board[i][j])
        return True