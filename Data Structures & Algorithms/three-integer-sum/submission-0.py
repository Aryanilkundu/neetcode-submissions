class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l =0
        r=len(numbers)-1
        ans = []
        while l<r:
            s = numbers[l] + numbers[r]
            if s == target:
                ans.append([l,r])
                l+=1
                r-=1
            elif s<target:
                l+=1
            else:
                r-=1
        return ans
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            p = self.twoSum(nums,-nums[i])
            if  p != []:
                for pair in p:
                    if i not in pair:
                        ls = [nums[i],nums[pair[0]],nums[pair[1]]]
                        ans.add(tuple(sorted(ls)))
        t =[]
        for ls in ans:
            t.append(list(ls))
        return t


        