n = int(input())

a=[]

def check(s):
    thuong = hoa = so = db = 0
    for i in s:
        if i >= 'a' and i <= 'z':
            thuong = 1
        if i >= 'A' and i <= 'Z':
            hoa = 1
        if i =='#' or i =='$' or i=='@':
            db = 1
        if i >= '0' and i <= '9':
            so = 1

    return (thuong == 1 and hoa == 1 and so == 1 and db == 1)

def checkLen(s):
    return (len(s) >= 6 and len(s) <= 12)

for i in range(n):
    a.append(input().split(','))

for i in a:
    dau = 0
    for x in i:
        if checkLen(x) and check(x):
            if dau == 0:
                print(x)
            else:
                print(','+x)
    print()
