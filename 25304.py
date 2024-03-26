x=int(input())
n=int(input())
hap=0
for i in range(n):
    a,b=input().split()
    a,b=int(a),int(b)
    hap+=a*b
if x==hap:
    print("Yes")
else:
    print("No")