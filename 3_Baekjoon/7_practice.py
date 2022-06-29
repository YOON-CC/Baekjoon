#A*(B+C)
#ABC+*

#A+B*C-D/E
#ABC*+DE/-

# 피연산자라면 출력
# ( 라면 스택에 저장
# ) 라면 ( 나올때까지 연산자 출력
# 연산자라면 스택에 있는 연산자들중 우선순위가 낮은 것들 출력
# 나머지 남아있는 연산자 출력

import sys
input = sys.stdin.readline

prior = {"/":2, "*":2, "+":1, "-":1, "(":0}
stack = []
_str = input().rstrip()

for s in _str:
    if s.isalpha(): # 문자는 그대로 출력
        print(s, end="")
    elif s == "(": # 일단 넣어
        stack.append(s)
    elif s == ")": # (만날때 까지 다 출력해 그리고 )는 출력 ㄴ, 버리고 끝
        while True:
            temp = stack.pop()
            if temp == "(":
                break
            print(temp, end="")
    else:
        while stack and prior[stack[-1]]>=prior[s]: # 내보다 낮은놈 빼고 나온나~~
            print(stack.pop(), end="")
        stack.append(s)
while stack:
    print(stack.pop(),end="")