t = int(input())

while t>0:
    n = int(input())
    di = {}
    for x in range(n):
        i = int(input())
        if i not in di:
            di[i] = 1
        else:
            di[i] += 1

    a = sorted(di.items(), key = lambda x: (-x[1], x[0]))
    print(a[0][0])
    t-=1
    