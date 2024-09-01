class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        while(l <= r):
            mid = l + ((r - l) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l += 1
            else:
                r -= 1   
        return -1
        