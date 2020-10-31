"""
Runtime: 32 ms, faster than 64.24% of Python3 online submissions for Reverse Integer.
Memory Usage: 14.1 MB, less than 99.99% of Python3 online submissions for Reverse Integer.
Given a 32-bit signed integer, reverse digits of an integer.
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
""""


class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31-1 
        MIN_INT = -2**31 
        #since python ints are long,we account for this by detecting overflow manually
        if x>MAX_INT or x<MIN_INT:
            return 0
        remainder = abs(x)
        rev = 0
        while remainder != 0:
            lsd = remainder%10
            remainder //= 10
            rev = rev*10 + lsd
            if rev > MAX_INT//10 and remainder != 0:
                return 0
            if (rev == MAX_INT//10 and x>0 and remainder>7):
                return 0 
            if (rev == MAX_INT//10 and x<0 and remainder>8):
                return 0
        if x<0:
            rev*=-1
        return rev