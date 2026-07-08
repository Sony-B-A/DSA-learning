# Given a positive number n, print the string "GFG" exactly n times separated by a single space.

n = int(input())

# Code here

def printgfg(n):
    if n== 0:
        return
    print("GFG", end=' ')
    printgfg(n-1)
    
printgfg(n)