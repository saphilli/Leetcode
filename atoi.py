"""
Runtime: 24 ms, faster than 98.55% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 14.2 MB, less than 99.99% of Python3 online submissions for String to Integer (atoi).

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip(" ")
        if len(s) == 0:
            return 0

        i = 0
        if s[0] == "+" or s[0] == "-":
            i+=1
            
        while i < len(s):
            if s[i] <= "9" and s[i] >= "0":
                i+=1
            else:
                break
          
        num = s[:i]
        if len(num) == 0 or num == "+" or num == "-":
            return 0
        num = int(num)
        
        if num<-2**31:
            return -2**31
        elif num > 2**31-1:
            return 2**31-1
        return num 
