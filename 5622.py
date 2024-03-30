word = input()
time = 0
a = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
for i in range(len(word)):
    for j in a:
        if word[i] in j:
            time += a.index(j)+3

print(time)