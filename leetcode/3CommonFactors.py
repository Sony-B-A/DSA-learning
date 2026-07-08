# 2427. Number of Common Factors
# Level: Easy
# Given two positive integers a and b, return the number of common factors of a and b.
# An integer x is a common factor of a and b if x divides both a and b.

class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        from math import sqrt
        n = a
        m = b

        af = []
        bf = []
        cmn = set()

        for i in range(1, int(sqrt(n)) + 1):
            if(n % i == 0):
                af.append(i)
                if(n // i != i):
                    af.append(n // i)
        # af.append(n)

        for i in range(1, int(sqrt(m)) + 1):
            if(m % i == 0):
                bf.append(i)
                if(m // i != i):
                    bf.append(m // i)
        # bf.append(m)

        cmn = (set(af) & set(bf))

        return len(cmn)