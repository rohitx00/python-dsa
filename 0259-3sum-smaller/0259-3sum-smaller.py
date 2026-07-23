class Solution():
    def sum_smaller(self, nums, target):
        result = 0
        nums.sort()
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total >= target:
                    right -= 1
                else:
                    result = result + (right-left)
                    left += 1

        return result





