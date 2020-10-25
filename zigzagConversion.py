#Runtime: 76 ms, faster than 31.53% of Python3 online submissions for ZigZag Conversion.
#Memory Usage: 14.2 MB, less than 6.88% of Python3 online submissions for ZigZag Conversion.
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) < 2 or numRows <2:
            return s
        zigzag = ""
        outer_row_inc = numRows+(numRows-2)
        #record two alternating increments for the inner rows
        increments = [outer_row_inc-2,2]
        #first row
        zigzag=s[::outer_row_inc]
        i =1
        start = 1
        while i < numRows-1 and len(s) > len(zigzag):
            #
            if i > (numRows)//2 -1 and i<numRows/2:
                increments[0],increments[1] = increments[1],increments[0]  
            j = start 
            inc = increments[0]
            while j < len(s):
                zigzag+=(s[j])
                j+=inc
                if inc == increments[0]:
                    inc = increments[1]
                else:
                    inc = increments[0]
                
            increments[0]-=2
            increments[1]+=2
            i+=1  
            start+=1
        #last row
        zigzag+=s[start::outer_row_inc]
        return zigzag