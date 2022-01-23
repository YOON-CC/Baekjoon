#정렬을 할때는 key를 줄수 있는데 key는 정렬을 목적으로 하는 함수를 값으로 넣는것이다.
#람다식을 통하여 lambda a,b: a+b ▶a,b를 변수로 받고 a+b를 최종값으로 한다라는 말이다.

#result = sorted(box, key=lambda x: x[0])
#box가 이차원배열이라 하면 각 방마다 제일 앞을 기준으로만 정렬을 한다는 말이다.

#또한 정렬을 할때는 sort,sorted가 있는데 전자는 배열이 정렬된후 유지, 후자는 일회용 정렬
#또한 전자는 배열.sort() 이렇게 사용하고 후자는 저장할배열 = sorted(정렬할 배열) 이다.

a = int(input())
box = []
result = []
for i in range(a):
    a, b = map(str, input().split())
    a = int(a)
    box.append([a, b])
    
result = sorted(box, key=lambda x: x[0])
for a,b in result:
    print(a,b)