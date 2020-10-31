"""
Runtime: 32 ms, faster than 56.61% of Python3 online submissions for Unique Paths.
Memory Usage: 14.1 MB, less than 99.99% of Python3 online submissions for Unique Paths.

Function to calculate the number of unique paths from the top left corner to the bottom right corner of a
n by m grid
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 0 or n <= 0:
            return 0
        memo = {}
        return self.findPaths(m,n,memo)
    
        
    #Top Down approach
    def findPaths(self,m,n,memo):
        if m<=1 or n<= 1:
            return 1
        if m == 2:
            return n
        if n==2:
            return m 
        #sort tuple everytime so we save space in memo since
        #paths for grid of m*n == n*m 
        key = (m,n) if m<n else (n,m)
        if not memo.get(key):
            memo[key] = self.findPaths(m-1,n,memo) + self.findPaths(m,n-1,memo)
        return memo[key]