class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_nums = defaultdict(list)
        for s in strs:
            tmp = ''.join(sorted(s))
            dict_nums[tmp].append(s)
        return list(dict_nums.values())
        