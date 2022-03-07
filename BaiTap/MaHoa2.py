P = [
    'A','B','C','D','E','F','G','H','I','J',
    'K','L','M','N','O','P','Q','R','S','T',
    'U','V','W','X','Y','Z','_','.'
    ]

while True:
    str = [i for i in input().split()]
    k = int(str[0])
    if k == 0:
        break
    s = list(str[1])
    for i in range(len(s)):
        j = P.index(s[i])
        s[i] = P[(j+k)%28]
    print("".join(s)[::-1])
