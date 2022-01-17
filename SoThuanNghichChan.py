t=int(input())
while t > 0:
    t-=1
    n=int(input())
    for i in range(0, 9, 2):
        for j in range(0, 9, 2):
            for k in range(0, 9, 2):
                a = i*100001+j*10010+k*1100
                if a==0: 
                    continue
                while(a % 10 == 0):
                    a //= 10
                if a >= n:
                    break
                print(a, end=" ")
    print()