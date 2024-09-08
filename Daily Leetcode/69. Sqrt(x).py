# Time Complexity: O(log n)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        l, r = 2, x // 2
        while l <= r:
            mid = (l + r) // 2
            num = mid * mid

            if num == x:
                return mid
            elif num > x:
                r = mid - 1
            else:
                l = mid + 1
        return r