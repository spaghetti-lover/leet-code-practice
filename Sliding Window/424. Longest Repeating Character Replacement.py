# Time complexity: O(n)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        diff, l = 0, 0
        freq = {}
        maxf = 0
        for r in range(0, len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxf = max(maxf, freq[s[r]])
            if r - l + 1 - maxf > k:
                freq[s[l]] -= 1
                l += 1
        return r - l + 1
