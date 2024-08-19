# https://neetcode.io/problems/is-anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        
        if len(s) != len(t):
            return False
        else:
            for x in s:
                dict_s[x] = 1 + dict_s.get(x, 0)
            for x in t:
                dict_t[x] = 1 + dict_t.get(x, 0)
            return dict_s == dict_t