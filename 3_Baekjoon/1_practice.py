#14888
import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input()) ##입력의 수
number = list(map(int, input().split())) ## 조합할 숫자

oper = list(map(int, input().split())) ## 연산자의 수

plus = oper[0] # 더하기
minus = oper[1] # 빼기
mul = oper[2] # 곱하기
div = oper[3] # 나누기

box = [] # 연산자를 넣는 배열

for i in range(plus):
    box.append(0)
    
for i in range(minus):
    box.append(1)

for i in range(mul):
    box.append(2)

for i in range(div):
    box.append(3)

n = plus+minus+mul+div

order = list(permutations(box, n)) # 중복을 포함하며 조합을 생각한다. , combinations의 경우는 중복을 허용하지 않는다.

result = [] # 연산 결과를 모아둔 배열

for i in range(len(order)):
    value = 0 # 연산의 값 초기화
    value = number[0] # 시작 숫자
    for j in range(n):
        if(order[i][j] == 0):
            #더하기
            value = value+number[j+1]
        if(order[i][j] == 1):
            #빼기
            value = value-number[j+1]
        if(order[i][j] == 2):
            #곱하기
            value = value*number[j+1]
        if(order[i][j] == 3):
            #나누기
            if(value < 0): # 한쪽이 음수
                value = -(abs(value)//number[j+1])
            else: # 나머지 경우
                value = value//number[j+1]
    result.append(value)
print(max(result))
print(min(result))