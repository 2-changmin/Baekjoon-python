a = int(input())
b = int(input())
c = int(input())
if a==b==c==60:
    print('Equilateral')
elif a+b+c==180 and (a==b or a==c or b==c):
    print('Isosceles')
elif a+b+c==180 and (a!=b!=c):
    print('Scalene')
else:
    print('Error')

'''
a = int(input())
b = int(input())
c = int(input())
if sum([a,b,c]) != 180:
    print('Error')
elif a==b==c:
    print('Equ~')
elif a==b or a==c or b==c: 
    print('Iso~')
else:
    print('Sca~')
'''
