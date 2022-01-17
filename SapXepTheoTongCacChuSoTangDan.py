t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = [int(i) for i in input().split()]

    b = {}
    for i in a:
        if i not in b:
            b[i] = sum(map(int, str(i)))

    c = sorted(b.items(), key = lambda x: [x[1], x[0]])
    for i in range(len(c)):
        print(c[i][0], end=" ")
