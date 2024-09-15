class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        l, r = min(bloomDay), max(bloomDay)
        res = -1

        while l <= r:
            mid = (l + r) // 2
            bouquets = 0
            cnt = 0

            for i in range(len(bloomDay)):
                if bloomDay[i] <= mid:
                    cnt += 1
                    if cnt == k:
                        bouquets += 1
                        cnt = 0
                    continue
                cnt = 0
            if bouquets < m:
                l = mid + 1
                continue
            res = mid
            r = mid - 1

        return res
