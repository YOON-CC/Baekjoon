#리스트 정렬은 for문으로 만들어도 가능하지만 sorted(리스트이름)또한 가능하다.
#자바 처럼 파이썬에서는 sys를 import하여 입력, 출력을 다음과 같이 표현할 수 있다.
#sys.stdin.readline()
#sys.stdout.write()
#그리고 for문을 sort로 표현하여 배열의 정렬되지 않은것을 오름차순으로 정렬하여 반복한다.
#정렬이 된 원소대로 차래로 i에 입력이 되는 것이다.

import sys
n = int(input())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
for i in sorted(l):
    sys.stdout.write(str(i)+'\n')