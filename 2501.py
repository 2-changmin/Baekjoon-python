import sys
n,k = map(int,sys.stdin.readline().split())
yak_list = []
for i in range(1,n+1):
    if n%i==0:
        yak_list.append(i)
if len(yak_list) < k:
    print('0')
else:
    print(yak_list[k-1])

'''
a,b = map(int,input().split())
c = []
for i in range(1, a//2+1):
    if a % i == 0:
        c.append(i)
c.append(a)
if len(c) >= b:
    print(c[b-1])
else:
    print(0)
'''