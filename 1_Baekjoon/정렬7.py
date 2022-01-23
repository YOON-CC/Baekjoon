#백준 18870
#시간을 아끼기 위해 다음을 사용#
#sys와 딕셔너리
#참고사이트 https://eunhee-programming.tistory.com/116

import sys
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr2 = [] 
#arr에는 처음 입력한 수가 들어있다.
#arr2는 빈 배열이다. 여기서는 중복을지우고(하나는 남겨둠) 오름차순으로 정렬한 수를 넣을 것이다.

arr2 = list(sorted(set(arr)))
#중복된것을 하나로 만들고 오름차순으로 정렬하였으니 해당 숫자 인덱스는 해당값이 일치하게 된다.

dic = {arr2[i]:i for i in range(len(arr2))} 
#따라서 축소한 인덱스가 차례로 들어가는 i를 arr2의 처음으로 넣는다.
# 즉 dic = {arr2[0]의값 : 0, arr2[1]의 값 : ...}이 된다.

for i in arr: # 최초 입력 리스트에서 원소가 차례대로 i에 들어온다.
    print(dic[i], end=' ')#딕셔너리(key값)을 통하여 바로 찾을 수 있다.