# 1. What are the two mandatory parts of recursion?
'''>base case and recursive case
'''
# 2. What happens if a recursive function has NO base case?
'''> infinite recursion and program crashes'''

# Predict the Output
def fun(n):
    if n == 0:
        return
    print(n)
    fun(n-1)

fun(3)
''' the output for this is 3, 2, 1 
I traced it'''

def fun(n):
    if n == 0:
        return
    fun(n-1)
    print(n)

fun(3)
''' output for this is 1, 2, 3
compare: print(n) is written before and after for both the fxns respectively'''

print()
def test(n):
    if n == 1:
        return 1
    return n + test(n-1)

print(test(4))
'''output = 10
'''

# Write a recursive function to print numbers from 5 to 1
print()
def fxn(n):
    if(n == 6):
        return
    fxn(n + 1)
    print(n)

fxn(1)

# “Statements written after a recursive call execute while going down.”
'''false, the statements written after recursive call will execute while going back up'''

# “A return statement ends all recursive calls at once.”
'''False, a return statement ends only the base case function and
all other functions will stay in the hold state until base case's function finishes'''

# Anything written after a recursive call executes while _____________.
'''going back up'''