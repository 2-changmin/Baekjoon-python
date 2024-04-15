a = list(map(int,input().split()))
max_a = max(a)
index_max = a.index(max_a)
a.remove(a[index_max])
b = 0
while True:
    if max_a < sum(a):
        b = sum(a)
        break
    else:
        max_a -= 1
print(max_a+b)