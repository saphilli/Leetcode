#Runtime: 28 ms, faster than 99.00% of Python3 online submissions for Running Sum of 1d Array.
#Memory Usage: 14.4 MB, less than 99.99% of Python3 online submissions for Running Sum of 1d Array.

#Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#Return the running sum of nums.
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums