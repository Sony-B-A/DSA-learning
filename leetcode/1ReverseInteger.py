# 7. Reverse Integer
# Level: Medium

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = abs(x)
        rev = 0
        while n > 0:
            rev = (rev * 10) + n % 10
            n = n // 10
        if(x < 0):
            rev = -(rev)
        if(rev >= -2 ** 31 and (rev <= 2 ** 31 -1)):
            return rev
        else:
            return 0  