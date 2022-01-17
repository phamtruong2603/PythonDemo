from operator import le


s = input()
a = list(s)
lenght = len(a)

for i in range(0, lenght):
    if(a[i] >= 'a' and a[i] <= 'z'):
        a[i] = a[i].upper()
    else:
        a[i] = a[i].lower()

print(''.join(a))
