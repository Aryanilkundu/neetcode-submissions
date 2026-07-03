class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        mid = int((l+r)//2)
        val = nums[mid]
        return val

