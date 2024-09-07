# Time complexity: O(n * m) where n is the input number and m is the length of the string
# Space complexity: O(m) where m is the length of the string
class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"

        for i in range(1, n):
            j = 0
            nextSeq = ""

            while j < len(res):
                count = 1

                while j < len(res) - 1 and res[j] == res[j + 1]:
                    count+=1
                    j+=1
                
                nextSeq += str(count) + res[j]
                j+=1
            res = nextSeq

        return res

        