# Time complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x == "(" or x == "[" or x == "{":
                stack.append(x)
            elif x == ")":
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif x == "}":
                if len(stack) > 0 and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif x == "]":
                if len(stack) > 0 and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        if(len(stack) == 0):
            return True
        return False
        