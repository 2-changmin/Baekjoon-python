a,b = input().split()
c = input()
a,b,c = int(a),int(b),int(c)

a += c // 60
b += c % 60

if b>=60:
    a += 1
    b -= 60 
if a>=24:
    a -= 24

print(a,b)