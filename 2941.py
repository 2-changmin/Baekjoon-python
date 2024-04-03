word = input()
count = 0
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in croatia:
    if i in word:
        count += word.count(i)
        word = word.replace(i, ' ') # i 라는 내용을 공백으로 치환

print(count + len(word.replace(' ', '')))