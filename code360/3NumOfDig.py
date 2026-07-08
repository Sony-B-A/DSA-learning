# Problem statement
# Ninja want to add coding to his skill set so he started learning it. On the first day,
# he stuck to a problem in which he has given a long integer ‘X’ and had to count the number of digits in it.
# Ninja called you for help as you are his only friend. Help him to solve the problem.

# EXAMPLE:
# Input: 'X' = 2
# Output: 
# As only one digit is ‘2’ present in ‘X’ so answer is ‘1’.


def countDigit(n: int) -> int:
   # Write your code here.
   count = 0
   while n > 0:
      count += 1
      n = n // 10
   return count

res = countDigit(33)
print(res)