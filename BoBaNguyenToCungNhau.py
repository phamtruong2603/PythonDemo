def check(a, b) :
    while b :
        r = a % b
        a = b
        b = r
    return (a == 1)

l, r = list(map(int, input().split()))

for i in range(l, r-1):
    for j in range(i+1, r):
        if check(i, j):
            for k in range(j+1, r+1):
                if check(k, j) and check(k, i):
                    print("(", i ,", " , j, ", " , k , ")", sep='')
