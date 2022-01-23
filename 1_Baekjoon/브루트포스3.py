#백준 1018
#문자열을 이차원배열로 만드는 방법
# array = []
#for _ in range(n):
#    array.append(input())
#print(array[숫자][숫자])
#=> 이렇게 하면 원래 array는 1차원배열이지만 2차원배열을 만듦으로 그 원소를 쪼개서 구할수있다.

n, m = map(int, input().split())
array = []

for _ in range(n):
    array.append(input())

case1 = "BWBWBWBW"
case2 = "WBWBWBWB"
result = [] # 여러 경우의 결과값을 담는 곳
index = 0 
for a in range(n-7):#세로 확장
    for b in range(m-7): #가로 확장
        sum1 = 0
        sum2 = 0
        line = 0
        for i in range(0+a,8+a):
            index = 0
            for j in range(0+b,8+b):
                if (line%2 == 0):
                    if (case1[index] != array[i][j]):
                        sum1+=1
                else:
                    if (case2[index] != array[i][j]):
                        sum1+=1
                if (line%2 == 0):
                    if (case2[index] != array[i][j]):
                        sum2+=1
                else:
                    if (case1[index] != array[i][j]):
                        sum2+=1
                index+=1   
            line+=1
        if (sum1>=sum2):
            result.append(sum2)  
        else:
            result.append(sum1)             
print(min(result))