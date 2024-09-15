# Time complexity: O(nlog(sum(weights) - max(weights))) where n is the length of the weights
class Solution:

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l <= r:
            m = (l + r) // 2

            tmp = 0
            cnt_day = 1

            for weight in weights:
                if tmp + weight <= m:
                    tmp += weight
                else:
                    cnt_day += 1
                    tmp = weight

            if cnt_day <= days:
                r = m - 1
            else:
                l = m + 1
        return l
