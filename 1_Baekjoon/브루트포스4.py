#백준 1436
#입력한 정수형 숫자를 리스트로 분리하는 방법
#box = list(map(int, str(n)))

a = int(input())
n = 1
index = 0
result = []
while True:
    box = list(map(int, str(n)))
    speed = 0
    for i in range(int(len(box))):
        if (box[i] == 6):
            speed+=1
        else:
            speed=0
        if (speed == 3):
            break
    if(speed == 3):
        index +=1
        result.append(n)
    n+=1
    if (a == index):
        break     
print(result[a-1])

