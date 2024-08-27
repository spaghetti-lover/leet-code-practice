# Time complexity: O(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for x in tokens:
            if x == "+":
                num_stack.append(num_stack.pop()+ num_stack.pop())
            elif x == "-":
                tmp1, tmp2 = num_stack.pop(), num_stack.pop()
                num_stack.append(tmp2 - tmp1)
            elif x == "*":
                num_stack.append(num_stack.pop() * num_stack.pop())
            elif x == "/":
                tmp1, tmp2 = num_stack.pop(), num_stack.pop()
                tmp = 0
                num_stack.append(int(tmp2/ tmp1))
            else:
                num_stack.append(int(x))
        return num_stack.pop()
                