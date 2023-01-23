#### still working on this problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(input())

n = int(input())

counter = 1

areAllStrictSuperSets = False

while counter <= n:
    isStrictSuperSet = False
    N = set(input())
    for i in A:
        if i not in N:
            isStrictSuperSet = True
        else:
            isStrictSuperSet = False
            break
    if isStrictSuperSet == True:
        areAllStrictSuperSets = True
    else:
        areAllStrictSuperSets = False
        break

    counter += 1

print(areAllStrictSuperSets)

###
###
###

# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(input())

n = int(input())

counter = 1

areAllStrictSupersets = False

while counter <= n:
    N = set(input())
    isStrictSuperset = False
    if N.issuperset(A) and len(A) == len(N):
        isStrictSuperset = True
    else:
        isStrictSuperset = False
        areAllStrictSupersets = False
        break
    if isStrictSuperSet == True:
        areAllStrictSuperSets = True
    else:
        areAllStrictSuperSets = False
        break

    counter += 1

print(areAllStrictSupersets)
