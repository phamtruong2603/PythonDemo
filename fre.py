n = int(input())

a = []
di={}
for i in range(n):
    a = a + input().split()

for i in a:
    if i not in di:
        di[i] = 1
    else:
        di[i] += 1

a = []

for key, value in di.items():
    a.append((value, key))

a = sorted(a, reverse=True)

max = a[0][0]
min = 0
for i in a:
    if i[0] < max:
        min = i[0]
        break

c = []
for i in a:
    if i[0] == min:
        c.append(i[1])

c.sort()

for i in c:
    print(i, end = ' ')