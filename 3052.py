import sys
input = sys.stdin.readline
a = []
b = 0
for i in range(10):
    c = int(input())
    a.append(c%42)
for i in range(42):
    if a.count(i) >= 1:
        b += 1
print(b)
    