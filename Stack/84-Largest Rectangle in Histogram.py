# Time complexity: O(n) 
# Solved using stack: https://www.youtube.com/watch?v=lktr76SxB2w
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_res = 0

        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_res = max(max_res, height * width)
            stack.append(i)
        return max_res
