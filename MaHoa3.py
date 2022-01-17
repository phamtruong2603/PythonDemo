def Rotate(a ,b):
    if type(b) is str:
        b = ord(b) - 65
    return chr((ord(a) + b - 65)%26 + 65)

t = int(input())
while t>0:
    t-=1

    s = input()

    str1 = list(s[:int(len(s)/2)])
    str2 = list(s[int(len(s)/2):])

    sumLeft = 0
    sumRight = 0
    for i in range(int(len(s)/2)):
        sumLeft += ord(str1[i]) - 65
        sumRight += ord(str2[i]) - 65

    for i in range(int(len(s)/2)):
        str1[i] = Rotate(str1[i], sumLeft)
        str2[i] = Rotate(str2[i], sumRight)

    for i in range(int(len(s)/2)):
        str1[i] = Rotate(str1[i], str2[i])

    print(''.join(str1))