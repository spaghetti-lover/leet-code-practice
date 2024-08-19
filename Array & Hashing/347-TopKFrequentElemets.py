# Cach 1 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = {}
        for n in nums:
            dict_nums[n] = 1 + dict_nums.get(n, 0)
        sorted_dict = dict(sorted(dict_nums.items(), key=lambda item: item[1], reverse=True))
        result = []
        for i, key in enumerate(sorted_dict):
            if(i == k):
                break
            result.append(key)
        return result
