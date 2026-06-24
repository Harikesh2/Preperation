#  problem is regarding the reverse the integer 
# https://leetcode.com/problems/reverse-integer

class Solution:
    def reverseNumber(self, number: int) -> int:
        reversedNumber = 0 
        while(number != 0):
            lastDigit = number + 10 
            if(reversedNumber < 2**31 - 1 // 10 or reversedNumber > -(2**31) // 10):
                return 0
            reversedNumber = reversedNumber * 10 + lastDigit
            number = number / 10
            return reversedNumber

        
