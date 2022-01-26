# import sys

# n = sys.stdin.readline().split()
# sys.stdout.write(str(n))
#이렇게 시간을 아낄수있다. readline은 하나를 입력하면 배열이 아니지만 위에처럼 split()
#을 통하여 두개 이상부터는 배열의 형태로 출력이 되며 write()를 사용하여 출력을한다.
#write는 print와 달리 자동 줄바꿈이 없다. 따라서 그 다음 줄로 넘어가지 않는다.
import sys
n = int(sys.stdin.readline())

stack=[]
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0]=='push':
        stack.append(command[1])
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])