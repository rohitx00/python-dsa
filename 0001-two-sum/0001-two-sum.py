class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            left = i
            right = i + 1
            while right < len(nums):
                total = nums[left] + nums[right]
                if total == target:
                    return [left, right]
                right +=1

