#여러줄에 입력을 하는 방법은 아래와 같다.
#a,b,c = map(int, input().split())

#또한 리스트로 원하는 만큼 넣는 방법은 다음과 같다.
#box = list(map(int, input().split()))

#배열에서 최솟값을 찾는 방법은 다음과 같다.
#min(배열이름)

#시간을 아끼며 소수를 구하는 방법은 다음과 같다.
#https://sso-feeling.tistory.com/387

#배열의 항목 개수는 다음과 같다.
#배열.count(항목)

#반지름을 가지고 원의 넓이를 구하는 것은 다음과 같다.
#import math
#반지름 * 반지름 * math.pi

x, y = map(int, input().split())

for i in range(x, y+1):
    if i == 1: 
        continue
    for j in range(2, int(i** 0.5)+1): #+1이 뒤에 붙은 이유는 가운데까지 반복하기 위함, 3이나 7같은 경우는 그냥 가운데 왼쪽
        if i%j==0:
            break #break가 없다면 반복이 끝나고 else로 가지만 break를 다는순간 해당 반복문은 그냥 탈출이니 else로 안간다.
    else: #반복이 조건보다 먼저이다. 따라서 반복이 모두 끝나고 나서 조건인 else에 들어올수 있다.
        print(i)