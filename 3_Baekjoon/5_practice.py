#17299
#Counter('hello world') # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
#위처럼 이렇게 딕셔너리 형태로 빈도수를 나타내기 때문에 시간 복잡도 문제를 해결할 수 있다.
from collections import Counter
import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
A_num = Counter(A)
answer = [-1] * n 
stack = []


stack.append(0)
for i in range(1, n):
    while stack and A_num[A[stack[-1]]] < A_num[A[i]]: 
        answer[stack.pop()] = A[i] 
    stack.append(i)


print(*answer)