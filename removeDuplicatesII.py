"""
Runtime: 40 ms, faster than 99.57% of Python3 online submissions for Remove Duplicates from Sorted Array II.
Memory Usage: 14.2 MB, less than 99.96% of Python3 online submissions for Remove Duplicates from Sorted Array II.
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
O(N) time and O(1) space
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        count = 1
        i=1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                if count < 2:
                    count+=1
                    i+=1
                else:
                    nums.pop(i)
            else:
                count = 1
                i+=1
                