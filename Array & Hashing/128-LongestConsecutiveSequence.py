#Time Complexity: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


#Time complexity: O(n) but slower than the previous solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if (len(nums) == 0):
            return 0
        hash_set = set()
        hash_set.add(nums[0])
        cnt = 0
        for i in range(1, len(nums)):
            if abs(nums[i] - nums[i - 1]) <= 1:
                hash_set.add(nums[i])
            else:
                cnt = max(len(hash_set), cnt)
                hash_set.clear()
                hash_set.add(nums[i])
            print(len(hash_set), " ", nums[i])
        cnt = max(len(hash_set), cnt)
        return cnt