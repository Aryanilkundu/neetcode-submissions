class Solution:
    def isValid(self, s: str) -> bool:
        left = ["[","{","("]
        right = ["]","}",")"]
        stack = []
        for i in range(len(s)):
            if s[i] in left:
                stack.append(s[i])
            elif s[i] == ']':
                if (stack and stack[-1] != '[') or len(stack)==0:
                    return False
                else:
                    stack.pop()
            elif s[i] == '}':
                if (stack and stack[-1] != '{') or len(stack)==0:
                    return False
                else:
                    stack.pop()
            else:
                if (stack and stack[-1] != '(') or len(stack)==0:
                    return False
                else:
                    stack.pop()
        if len(stack)==0:
            return True
        else:
            return False


