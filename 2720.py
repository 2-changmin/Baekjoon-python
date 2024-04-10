t = int(input())
size = [25,10,5,1]
'''for i in range(t):
    c = int(input()) / 100
    for k in size:
        print(int(c//k),end=' ')
        if c < k:
            continue
        c -= k * (c//k)
    print()'''
for _ in range(t):
    c = int(input())
    for k in size:
        print(c//k, end=' ')
        c %= k
    print()