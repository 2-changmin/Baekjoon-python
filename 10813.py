import sys
input = sys.stdin.readline
n,m = sys.stdin.readline().split()
n,m = int(n),int(m)
a = [0]*n
for i in range(1,n+1):
    a[i-1] = i
for i in range(m):
    i,j = map(int,input().split())
    a[i-1],a[j-1] = a[j-1],a[i-1]
for i in range(n):
    print(a[i],end=' ')