class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #push first to stack
        #i = 0
        #now compare first with second. if second greater then while second greater: stack.pop()
        #i += 1, in the index = i
        #else: stack.append(val)
        stack = []
        ans = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return ans
                    
