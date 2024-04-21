n = int(input())
kg_5 = int(n/5)
kg_3 = int(n/3)
c = 0
d = []

if n % 5 == 0:
    d.append(int(n/5))
elif n % 3 == 0:
    d.append(int(n/3))
for i in range(kg_5,0,-1):
    c = n
    c -= 5 * i
    if c % 3 == 0:
        b = int(c/3)
        d.append(b+i)
if len(d) != 0:
    print(min(d))
else:
    print(-1)