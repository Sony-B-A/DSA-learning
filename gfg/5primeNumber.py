# Given a number n, determine whether it is a prime number or not.
# Note: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

class Solution:
    def isPrime(self, n):
        # code here
        from math import sqrt
        if(n < 2):
            return False
        else:
            if(n % 2 == 0 and n != 2):
                return False
            else:
                for i in range(3, int(sqrt(n)) + 1, 2):
                    if(n % i == 0):
                        return False
        return True