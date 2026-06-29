class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_s = set(s)
        chars_t = set(t)
        if chars_s == chars_t and len(s) == len(t):
            for char in chars_s:
                if s.count(char) != t.count(char):
                    return False
            return True
        else:
            return False
        