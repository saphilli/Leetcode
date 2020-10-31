"""
Runtime: 76 ms, faster than 91.50% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.8 MB, less than 89.25% of Python3 online submissions for Remove Duplicates from Sorted Array.
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if(nums[i] == nums[j]):
                continue
            else:
                i += 1
                nums[i] = nums[j]
        return i + 1
    
    