# Intuition: nested => sub problem => recursion + parrantesis => where to stop => stack
# Time complexity: O(n) where n is the length of the string
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "]":
                tmp, num = "", ""

                while stack and stack[-1] != "[":
                    tmp = stack.pop() + tmp
                stack.pop()

























                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * tmp)
            else:
                stack.append(char)
        return "".join(stack)
    