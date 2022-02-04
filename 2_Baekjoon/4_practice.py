#백준14600

#입력
num = int(input())
sewer = list(map(int, input().split()))

#배열, 하수구 생성 및 타일 배치
if num == 1:
    box = [[1,1],[1,1]]
    box[sewer[0]-1][sewer[1]-1] = -1
else:
    box = [[1,1,3,3],[1,1,3,3],[2,2,4,4],[2,2,4,4]]
    box[sewer[0]-1][sewer[1]-1] = -1
    if sewer[0]>=1 and sewer[0]<=2 and sewer[1]>=1 and sewer[1]<=2:#3사분면
        box[1][2], box[2][1],box[2][2]= 5,5,5
    
    if sewer[0]>=3 and sewer[0]<=4 and sewer[1]>=1 and sewer[1]<=2:#4사분면
        box[1][1], box[1][2],box[2][2]= 5,5,5  
    
    if sewer[0]>=1 and sewer[0]<=2 and sewer[1]>=3 and sewer[1]<=4:#2사분면
        box[1][1], box[2][1],box[2][2]= 5,5,5  
    
    if sewer[0]>=3 and sewer[0]<=4 and sewer[1]>=3 and sewer[1]<=4:#1사분면
        box[1][1], box[1][2],box[2][1]= 5,5,5  
        
#결과출력
for i in range(2**num,0,-1):
    for j in range(2**num):
        print(box[j][i-1], end= " ") # 반시계 방향으로 90도 정도 배열이 일어난다.
    print()
