import sys
n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]

a = sorted(set(a))
for i in a:
    print(i)