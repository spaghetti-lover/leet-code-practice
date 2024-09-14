# Time complexity: O(n)
# Space complexity: O(n)
# Explanation: We iterate through the string and append each character to the corresponding row. We keep track of the current row and whether we are going down or up. If we are at the top or bottom row, we change the direction. Finally, we join the rows and return the result.
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [''] * numRows
        current_row, going_down = 0, False

        for char in s:
            rows[current_row] += char
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1
        return ''.join(rows)
