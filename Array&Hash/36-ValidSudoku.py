# Time complexity: O(1)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Kiểm tra các hàng
        for i in range(0, len(board)):
            hash_set = set()
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    if board[i][j] in hash_set:
                        return False
                    hash_set.add(board[i][j])

        # Kiểm tra các cột
        for i in range(0, len(board)):
            hash_set = set()
            for j in range(len(board[i])):
                if board[j][i] != '.':
                    if board[j][i] in hash_set:
                        return False
                    hash_set.add(board[j][i])

        # Kiểm tra các ô 3x3
        for block_i in range(0, len(board), 3):
            for block_j in range(0, len(board[0]), 3):
                hash_set = set()
                for i in range(3):
                    for j in range(3):
                        current_val = board[block_i + i][block_j + j]
                        if current_val != '.':
                            if current_val in hash_set:
                                return False
                            hash_set.add(current_val)

        return True

# Time complexity: O(1)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True