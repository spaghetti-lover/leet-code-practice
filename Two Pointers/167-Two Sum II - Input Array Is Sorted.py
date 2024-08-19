# Time complexity: O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while (l <= r):
            tmp = numbers[l] + numbers[r] 
            if tmp == target:
                return [l + 1, r + 1]
            elif tmp < target:
                l += 1
            else:
                r -= 1
        return [l + 1, r + 1]