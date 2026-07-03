class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict 
        u = defaultdict(list)
        
        for s in strs:
            # N = '000'*26
            chars = list(s)
            chars.sort()
            # print(chars)
            chars_str = ''.join(chars)
            u[chars_str].append(s)
        dic = dict(u)
        values_ls = list(dic.values())

        return values_ls
            

        
