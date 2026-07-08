# 2180. Count Integers With Even Digit Sum
# Easy
# Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.
# The digit sum of a positive integer is the sum of all its digits.

class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0

        for i in range(1, num + 1):
            sum = 0
            n = i
            while n > 0:
                sum += n % 10
                n = n // 10

            if(sum % 2 == 0):
                count += 1
            

        return count