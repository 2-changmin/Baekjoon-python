n,m = input().split()
n,m = int(n),int(m)
a = [0]*n
for _ in range(m):
    i,j,k = input().split()
    i,j,k = int(i),int(j),int(k)
    for x in range(i-1,j):
        a[x] = k
for i in a:
    print(i,end=' ')