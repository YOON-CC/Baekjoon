how_many = int(input())
result = 0

for n in range(how_many):
    a = input() #새로운 문자를 받아들일 준비
    num = 0 #새로운 문자를 받아들일 준비
    box = 0 #새로운 문자를 받아들일 준비
    for i in range(1, len(a)): #문자의 하나당 돌리기
        num+=1
        if (a[i-1] != a[i]): # 앞뒤가 다를 경우
            if (a.count(a[i-1]) == num):#그리고 하나로 나열된 경우
                box+=num #box에 담기
                num = 0 #하나의 문자에대해 다시 다른 알파벳의 시작
            if (a.count(a[i-1]) != num): # 하나로 나열된 경우가 아닌경우
                num = 0 #num을 0으로 주어 바로 밑의 조건문이 무조건 수치적으로 틀리게 한다.
    if (len(a) == (box+num+1)): #result
        result +=1

print(result)