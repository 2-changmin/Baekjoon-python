x = input('')
y = input('')
x = int(x)
y = int(y)
if x>0:
    if y>0:
        print('1')
    elif y<0:
        print('4')
if x<0:
    if y>0:
        print('2')
    elif y<0:
        print('3')
        