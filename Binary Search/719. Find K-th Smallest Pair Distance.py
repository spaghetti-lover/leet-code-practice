# Time complextiy: O(nlogn) where n is the length of the nums
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, max(nums)
        while l < r:
            m = l + (r - l) // 2

            left = 0
            cnt = 0
            # dung two pointer de tao mang diff
            for right in range(0, len(nums)):
                while nums[right] - nums[left] > m:
                    left += 1
                cnt += right - left

            if cnt >= k:
                r = m
            else:
                l = m + 1
        return r
