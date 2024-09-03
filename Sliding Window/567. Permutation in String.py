# Time complexity: O(n * m)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        k = len(s1)
        l = 0
        for r in range(k - 1, len(s2)):
            tmp = {}
            for i in range(l, r + 1):
                tmp[s2[i]] = 1 + tmp.get(s2[i], 0)
            cnt = 0
            for c in s1:
                if c in tmp:
                    if tmp[c] == 0:
                        break
                    tmp[c] -= 1
                    cnt += 1
            if r - l + 1 == cnt:
                return True
            l += 1
        return False
        
# Time complexity: O(n)
# Check len(s1) and len(s2) => Initialize s1Count and s2Count => Check matches in the first len(s1) element => Iterate through s2 => Check matches => Return matches
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1
        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
        