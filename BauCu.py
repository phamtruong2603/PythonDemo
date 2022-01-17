m, n = list(map(int,input().split()))
a = [int(i) for i in input().split()]
b = []

for i in a:
    b = b + [a.count(i)]

b = sorted(b)

max1 = b[len(b) - 1]
max2 = -1
b = b + [-1]

for i in b:
    if i < max1 and i > max2:
        max2 = i
        
if max2 == -1 or max2 == 0:
    print("NONE")
else:
    for i in a:
        if a.count(i) == max2:
            print(i)
            break