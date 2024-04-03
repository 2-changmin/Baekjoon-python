'''word = input()
a = int(len(word))
b = 0
for i in range(a):
    if word[i] == word[a-1-i]:
        b += 1
    else:
        continue
if b == a:
    print('1')
else:
    print('0')'''

word = input()
if word[::1] == word[::-1]:
    print('1')
else:
    print('0')