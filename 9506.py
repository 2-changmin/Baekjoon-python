while True:
    sum_a = 0
    a = []
    b = 0
    n = int(input())
    if n == -1:
        break
    for i in range(1,n//2+1):
        if n%i==0:
            a.append(i)
            sum_a += i
    b = len(a)
    if sum_a == n:
        print(n,'=',end=' ')
        for x in range(b-1):
            print(a[x],'+ ',end='')
        print(a[b-1])
    else:
        print(n,'is NOT perfect.')