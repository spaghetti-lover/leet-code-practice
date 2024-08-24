# Time complexity: O(n)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = min(heights[l], heights[r]) * (r - l)
        
        while (l < r):
            min_height = 0
            if heights[l] > heights[r]:
                r -= 1
                tmp = min(heights[l], heights[r]) * (r - l)
                if tmp > res:
                    res = tmp
            else:
                l += 1
                tmp = min(heights[l], heights[r]) * (r - l)
                if tmp > res:
                    res = tmp
        return res
# Time complexity: O(n)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        
        while (l < r):
            res = max(res, min(heights[l], heights[r]) * (r - l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res
        
        