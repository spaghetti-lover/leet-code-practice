# Time complexity: O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_left = height[l]
        max_right = height[r]
        res = 0
        while(l < r):
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                res += max_left - height[l]
            elif max_left >= max_right:
                r -= 1
                max_right = max(max_right, height[r])
                res += max_right - height[r]
        return res
        