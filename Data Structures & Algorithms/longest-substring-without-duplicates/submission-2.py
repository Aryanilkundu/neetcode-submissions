class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        l = 0
        r=0
        ans = 0
        n = len(s)
        # while l<n:
        while r<n:
            if s[r] not in dic:
                dic[s[r]] = r
                if r == n-1:
                    ans = max(ans,r-l+1)
            else:
                ans = max(ans,r-l)
                l = max(dic[s[r]]+1,l)
                dic[s[r]] = r 
            r+=1
            print(l,r)

        if ans == 0:
            ans = len(s)
        return ans
        
                



