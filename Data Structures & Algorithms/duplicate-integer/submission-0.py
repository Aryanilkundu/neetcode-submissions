class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques = set()
        ans = 0
        for element in nums:
            if element in uniques:
                ans = 1
                break
            else:
                uniques.add(element)
        if ans == 0:
            return False
        else:
            return True 


