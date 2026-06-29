class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        order = sorted(range(len(nums)), key=lambda i: nums[i], reverse=False)
        print(order)
        for i in range(len(sorted_nums)):
            element = sorted_nums[i]
            needed = target - element
            for j in range(len(sorted_nums)-1,i,-1):
                if needed == sorted_nums[j]:
                    i1 =  min(order[i],order[j])
                    i2 = max(order[i],order[j])
                    return [i1,i2]
            
