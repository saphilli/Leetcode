#Runtime: 88 ms, faster than 86.40% of Python3 online submissions for Median of Two Sorted Arrays.
#Memory Usage: 14.5 MB, less than 9.29% of Python3 online submissions for Median of Two Sorted Arrays.
#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

class Solution:
    #Worst Case: O(NlogN) due to sorting N items (len(nums1)+len(nums2))         
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2) #NlogN  
        N = len(merged)
        #if length is odd
        if N%2 == 1:
            return merged[N//2]   
        #if length is even
        return (merged[N//2-1]+merged[N//2])/2   

#Runtime: 84 ms, faster than 94.65% of Python3 online submissions for Median of Two Sorted Arrays.
#Memory Usage: 14.3 MB, less than 9.29% of Python3 online submissions for Median of Two Sorted Arrays.    
#faster solution since only merging half of the sorted arrays: O(N) where N = len(nums1)+len(nums2)
class Solution2:            
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = merge(nums1,nums2)
        N = len(nums1) + len(nums2)
        #if length of a+b is odd
        if N%2 == 1:
            return merged[-1]
        return (merged[-2] +merged[-1])/2    
    
        
def merge(a, b):
    i = j = k = 0
    N = len(a) +len(b)
    limit = N//2+1
    if N%2 == 1:
        limit = N//2+1
    merged = []
    while k < limit:
        if j >= len(b) or (i < len(a) and a[i]<=b[j]):
            merged.append(a[i])
            i+=1
        else:
            merged.append(b[j])
            j+=1
        k+=1
    return merged
