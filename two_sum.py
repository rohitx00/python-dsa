from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        first = 0
        last = len(nums)-1

        while(first < last):
            if nums[first] + nums[last] == target:
                return [first, last]
            elif nums[first] + nums[last] < target:
                first = first + 1
            else:
                last = last - 1
        return [-1]
        
cl = Solution()
print(cl.twoSum([2,7,11,15],9))