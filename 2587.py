a = []
for i in range(5):
    a.append(int(input()))
a = sorted(a)
print(int(sum(a)/len(a)))
print(a[2])