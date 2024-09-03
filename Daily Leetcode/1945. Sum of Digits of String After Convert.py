class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_str = ''.join(str(ord(char) - ord('a') + 1) for char in s)
        num = int(num_str)
        
        for i in range(0, k):
            curr_sum = 0
            while num > 0:
                curr_sum += num % 10
                num = num // 10
            num = curr_sum
        return curr_sum