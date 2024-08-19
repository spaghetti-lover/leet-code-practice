# Time complexity: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join([char for char in s if char.isalnum()])
        l = 0
        r = len(s) - 1
        while (l <= r):
            if (s[l] != s[r]):
                return False
            l += 1
            r -= 1
        return True

# Time complexity: O(n) but faster than the previous solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s.lower()))
        return s == s[::-1]

# Time complexity: O(n) but more memory efficient than the previous solution
class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        new=""
        for i in s:
            if i.isalnum():
                new+=i
        return new[::-1] == new 
        