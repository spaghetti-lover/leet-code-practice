# Time complexity: O(n log log n)
mport math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        prime = [True] * n
        prime[0], prime[1] = False, False
        
        for i in range(2, int(math.sqrt(n)) + 1):
            if prime[i]:
                for j in range(i * i, n, i):
                    prime[j] = False
        return sum(prime)
