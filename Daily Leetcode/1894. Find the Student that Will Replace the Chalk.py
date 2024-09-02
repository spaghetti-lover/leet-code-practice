# Time complexity: O(n)
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalk = sum(chalk)
        k %= total_chalk
        for i, c in enumerate(chalk):
            if k - c < 0:
                return i
            else:
                k -= c
        return 0