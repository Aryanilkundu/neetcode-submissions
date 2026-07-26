class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        for idx, element in reversed(list(enumerate(temperatures))):
            while stack and element >=stack[-1][1]:
                stack.pop()
            if len(stack)!=0:
                ans[idx] = stack[-1][0] - idx
            stack.append((idx,element))
        return ans