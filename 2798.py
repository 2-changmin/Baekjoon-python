n,m = map(int,input().split())
a = list(map(int,input().split()))
max_a = 0
c = 0
for i in range(n):
    for k in range(n):
        if i == k:
            continue
        for j in range(n):
            if k == j or i == j:
                continue
            c = a[i] + a[k] + a[j]
            if c >= max_a and c <= m:
                max_a = c
print(max_a)
                