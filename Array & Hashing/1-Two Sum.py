class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        for i,n in enumerate(nums):
            complement = target - n
            if complement in dict_nums:
                return [dict_nums[complement], i]
            dict_nums[n] = i
                
            
