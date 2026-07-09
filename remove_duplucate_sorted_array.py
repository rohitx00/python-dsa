from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 1
        count = 1
        while (j < n):
            if nums[j] == nums[i]:
                j = j + 1
                continue
            else:
                nums[i+1] = nums[j]
                i = i + 1
                j = j + 1
                count = count + 1
        return count
    
cl = Solution()
print(cl.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))