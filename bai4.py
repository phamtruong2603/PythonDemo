n = int(input())
a = [int(i) for i in input().split()]

lenght = len(a)
count = 0
start = 0
end = 0

for i in range(lenght-1, 0 , -1):
    if a[i]*a[i-1] > 0:
        if count == 0:
            start = a[i-1]
            end = a[i]
        count +=1

print(count, end=" ")
if count > 0:
    print(start, end)
