# Time complexity: O(nlogn)
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        res = r
        while (l <= r):
            k = l + (r - l) // 2
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / k)
            if totalTime > h:
                l = k + 1
            else:
                res = min(res, k)
                r = k - 1
        return res
                    
        
                    
        