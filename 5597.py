n = []
for i in range(1,31):
    n.append(i)
for i in range(28):
    a = int(input())
    n.remove(a)
b = min(n)
print(b)
c = max(n)
print(c)