import math
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        max_diff = math.inf
        result_sum = 0

        for i in range (len(nums)-2):
            
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                diff = abs(total-target)

                if diff < max_diff:
                    max_diff = diff
                    result_sum = total
                
                if total == target:
                    left +=1
                    right -=1
                elif total < target:
                    left +=1
                else:
                    right -=1
            
        return result_sum