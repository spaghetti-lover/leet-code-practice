# Time complexity: O(logn)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = 9999
        while (l <= r):
            mid = (l + r) // 2
            res = min(res, nums[mid])
            # Check xem thuoc day tang dan ben phai hay ben trai
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return res
    