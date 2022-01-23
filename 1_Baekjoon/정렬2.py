# 10989번
#매모리를 아끼며 효율적으로 사용하는 방법

import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001 # 이러면 배열의 길이가 10001이 된다.

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1 # 입력한 인덱스에 1이 들어간다.(+=)로 중복처리

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]): # 결국 든것은 1이니 한번 반복이다. 중복은 그만큼 수 
            print(i)

