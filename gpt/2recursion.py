# 1. Write a recursive function to print numbers from N to 1.
def rec(n):
    if(n == 1):
        print(n)
        return
    print(n)
    rec(n - 1)
rec(4)

# 2. Write a recursive function to print numbers from 1 to N.
print()
def upward(n):
    if(n == 1):
        print(1)
        return
    upward(n - 1)
    print(n)
upward(5)

# 3. Write a recursive function to return the sum of first N natural numbers.
print()
def sum_n(n):
    if(n == 1):
        return 1
    return n + sum_n(n - 1)
print(sum_n(5))


