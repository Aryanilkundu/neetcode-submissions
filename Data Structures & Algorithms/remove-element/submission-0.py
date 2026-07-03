class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i] != val:
                k+=1
            else:
                nums[i] = 51
        nums.sort()
        return k