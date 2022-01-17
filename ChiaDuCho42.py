a = []
while True:
    b = input().split()
    b = list(map(int, b))
    a = a + b
    if(len(a) == 10): break
for i in range(10):
    a[i] = a[i] % 42
print(len(set(a)))