"""
Runtime: 32 ms, faster than 67.18% of Python3 online submissions for Decode Ways.
Memory Usage: 14.1 MB, less than 5.26% of Python3 online submissions for Decode Ways.
message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        if N == 0 or not s:
            return 0
        dp = [0] * N
        dp[0] = 0 if s[0] == "0" else 1
        
        for i in range(1,N):
            current = s[i]
            prev_current = int(s[i-1:i+1])
            if current >= "1":
                dp[i] = dp[i-1]
                
            if prev_current >=10 and prev_current <= 26:
                dp[i] += dp[i-2] if i>=2 else 1
                
            
        return dp[N-1]
