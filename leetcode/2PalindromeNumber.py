# 9. Palindrome Number
# Level: Easy
# Given an integer x, return true if x is a palindrome, and false otherwise.


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0:
            n = x
            res = 0

            while n > 0:
                ld = n % 10
                res = (res * 10) + ld
                n = n // 10
            
            return res == x

        else:
            return False


obj = Solution()
res = obj.isPalindrome(10)