n = int(input())
div = 2
while n != 1:
    if n%div != 0:
        div += 1
    else:
        print(div)
        n /= div

'''
n = int(input())
div = 2
square = int(n ** 0.5)
while div <= square:    #모든 합성수는 그 수의 제곱근보다 작거나 같은 약수를 갖는다!!
    if n % div != 0:
        div += 1
    else:
        print(div)
        n //= div
if n>1:
    print(n)
'''