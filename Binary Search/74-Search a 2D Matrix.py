# Time complexity: O(logn + logm)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up_row = 0
        down_row = len(matrix) - 1
        mid_row = 0
        while(up_row <= down_row):
            mid_row = up_row + (down_row - up_row) // 2
            if matrix[mid_row][-1] < target:
                up_row += 1
            elif matrix[mid_row][0] > target:
                down_row -= 1
            else:
                break
        l, r = 0, len(matrix[mid_row]) - 1
        while(l <= r):
            mid = l + (r - l) // 2
            if matrix[mid_row][mid] < target:
                l += 1
            elif matrix[mid_row][mid] > target:
                r -= 1
            else:
                return True
        return False