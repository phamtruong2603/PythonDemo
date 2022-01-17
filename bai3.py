n = int(input())
s = [input().lower() for i in range(n)]

s = list(set(s))
s.sort()

for i in s:
    print(i)
    