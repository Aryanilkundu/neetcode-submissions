class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeros=0
        last_zero_at = -1
        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                zeros+=1
                last_zero_at =i
            else:
                prod*=num
        
        if zeros>1:
            return [0]*len(nums)
        elif zeros == 1:
            ls = [0]*len(nums)
            ls[last_zero_at] = prod
            return ls
        else:
            ls = [0]*len(nums)
            for i in range(len(nums)):
                ls[i] = int(prod/nums[i])
            return ls