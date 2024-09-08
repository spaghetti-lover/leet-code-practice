# Time complexity: O(n * m) where n is the number of strings and m is the length of the shortest string
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        res = strs[0]
        for i in range(1, len(strs)):
            for j in range(0, len(strs[i])):
                if j >= len(res) or strs[i][j] != res[j]:
                    res = strs[i][:j]
                    break
        return res
# Time complexity: O(n * m) where n is the number of strings and m is the length of the shortest string
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        shortest = strs[0]

        for i in range(n):
            if len(strs[i]) < len(shortest):
                shortest = strs[i]
            
        left = 0
        right = len(shortest)
        
        while left < right:
            prefix = shortest[:right]
            if all(s.startswith(prefix) for s in strs):
                return prefix
            else:
                right -= 1
        return ""