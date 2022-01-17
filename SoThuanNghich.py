def Inverse(s):
    str1 = str(s)
    str2 = str1[::-1]
    if str1 == str2:
        return True
    return False

# Chuyển đổi hệ cơ số
def ConvertNumber(n, b):
    if (n < 0 or b < 2 or b > 16):
        return False
 
    sb = ""
    m = 0
    remainder = n
 
    while (remainder > 0):
        if (b > 10):
            m = remainder % b
            if (m >= 10):
                sb = sb + str(chr(55 + m))
            else:
                sb = sb + str(m)
        else:
            sb = sb + str(remainder % b)
        remainder = int(remainder / b)
    return "".join(reversed(sb))

count = 0

a, b, M = list(map(int, input().split()))

for i in range(a, b+1):
    for k in range(2, M+1):
        if Inverse(ConvertNumber(i, k)):
            count += 1
        
print(count)
