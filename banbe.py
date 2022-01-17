t = int(input())

while t > 0:
    count = 0
    a, b = [int(x) for x in input().split()]
    max = b+2
    f = [1]*max
    for i in range(2, max//2):
        for j in range(i*2, max, i):
            f[j]+=i
    for i in range(a, b):
        if f[i] <= b and f[f[i]]==i and f[i]!=i:
            count+=1
    print(count//2)
    t-=1
