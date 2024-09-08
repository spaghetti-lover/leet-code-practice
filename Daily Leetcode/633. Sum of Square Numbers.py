# Time complexity: O(sqrt(c))
# Space complexity: O(1)
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(math.sqrt(c)) + 1):
            a = c - i*i
            if math.isqrt(a) ** 2 == a:
                return True
        return False
