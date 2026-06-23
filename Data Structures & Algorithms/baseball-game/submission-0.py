class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for char in operations:
            if char == "+":
                sum_val = stack[-1] + stack[-2]
                stack.append(sum_val)
            elif char == "C":
                stack.pop()
            elif char == "D":
                stack.append(stack[-1]*2)
            else:
                char = int(char)
                stack.append(char)
        return sum(stack)