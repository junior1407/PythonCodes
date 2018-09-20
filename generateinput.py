import random

for i in range(1000):
    n = random.randint(1,100)
    a = random.randint(1,100)
    print(n," ",a,sep='')
    for i in range(n):
        if (i==n-1):
            print(random.randint(1, 1000))
        else:
            print(random.randint(1,1000)," ",sep='',end='')