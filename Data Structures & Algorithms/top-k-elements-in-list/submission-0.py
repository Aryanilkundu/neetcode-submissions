class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)
        for i in range(len(nums)):
            cnt[nums[i]]+=1
        ls=[]
        cnt_d = dict(sorted(cnt.items(), key=lambda item: item[1], reverse=True))
        l = list(cnt_d.keys())
        for i in range(k) :
            ls.append(l[i])
        return ls
