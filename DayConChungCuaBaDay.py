def findCommon(ar1, ar2, ar3, n1, n2, n3):
    i, j, k = 0, 0, 0

    res = []
    while (i < n1 and j < n2 and k < n3):
        if (ar1[i] == ar2[j] and ar2[j] == ar3[k]):
            res.append(ar1[i])
            i += 1
            j += 1
            k += 1
        elif ar1[i] < ar2[j]:
            i += 1
        elif ar2[j] < ar3[k]:
            j += 1
        else:
            k += 1
    if len(res) == 0:
        print("NO")
    else:
        for i in res:
            print(i, end=" ")

t = int(input())
while t > 0:
    t -= 1
    length = input()
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    findCommon(a, b, c, len(a), len(b), len(c))
    print()