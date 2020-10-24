class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palin = s[0]
        for i in range(0,len(s)-1):
            left = right = i
            #if palindrome of same chars, move left and right pointers
            #until different characters are found on either end
            if s[i] == s[left] or s[i] == s[right]:
                while left > -1:
                    if s[i] != s[left]:
                        left+=1
                        break
                    left -=1
                while right <len(s):
                    if s[i] != s[right]:
                        right-=1
                        break
                    right+=1
            if left < 0:
                left = 0
            if right >= len(s):
                right = len(s)-1
            #expand out palinrome until it ends,i.e. left and right are not equal
            while left > -1 and right < len(s) and s[left]==s[right]:
                left-=1
                right+=1    
            if (right-left)-1 > len(max_palin):
                    max_palin = s[left+1:right]
        return max_palin
    