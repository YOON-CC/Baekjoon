#2504

bracket = list(input())

stack = []
answer = 0
tmp = 1

# [ [] [] ]
#(3+3)*3 = (3*3)+(3*3) = 27
for i in range(len(bracket)):

    if bracket[i] == "(":
        stack.append(bracket[i])
        tmp *= 2

    elif bracket[i] == "[":
        stack.append(bracket[i])
        tmp *= 3

    elif bracket[i] == ")":
        if not stack or stack[-1] == "[": ## 올바르지 않은 입력 not stack의 경우 바로 위의 elif 에 맞느 것이 없으니 잘못됨
            answer = 0
            break
        if bracket[i-1] == "(": ## 이전이 맞는 입력
            answer += tmp
        stack.pop()
        tmp //= 2 

    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if bracket[i-1] == "[":
            answer += tmp

        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)