'''front,back,tall = map(int,input().split())
now_1 = 0
day_count = 0
while True:
    day_count += 1
    now_1 += front
    if now_1 >= tall:
        break
    now_1 -= back
print(day_count)'''
import sys
import math

a,b,v = map(int,sys.stdin.readline().split())
day = (v - b) / (a - b)   #(v-b) - 마지막 날 떨어지는 걸 제외 (a-b) - 하루에 오를 수 있는 높이
print(math.ceil(day))  #ceil 함수는 실수를 입력하면 올림 하여 정수를 반환하는 함수이다.
