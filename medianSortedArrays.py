#Runtime: 80 ms, faster than 98.32% of Python3 online submissions for Median of Two Sorted Arrays.
#Memory Usage: 14.4 MB, less than 9.29% of Python3 online submissions for Median of Two Sorted Arrays.
#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

class Solution:            
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2) #N+MlogM+N  
        N = len(merged)
        #if length is odd
        if N%2 == 1:
            return merged[N//2]   
        #if length is even
        return (merged[N//2-1]+merged[N//2])/2   
     
