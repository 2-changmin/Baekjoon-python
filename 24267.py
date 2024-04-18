def m(n):
    a = 0
    for i in range(1,n-1):
        a += i
    b = a
    for i in range(n-2,0,-1):
        b -= i
        a += b
    return a
n = int(input())
print(m(n))
print(3)