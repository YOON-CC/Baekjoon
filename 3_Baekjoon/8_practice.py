#(1) 전체 수 만큼 True의 리스트를 생성해준다.
#(2) 2부터 +1씩 해주면서 그 배수에 해당하는 값들을 False로 바꿔준다.
r= 1000000

check = [True for _ in range(r)]

for i in range(2,int(r**0.6)):
    if check[i]==True:
        for j in range(i*2, r, i): # 마지막 i 즉, 튜플은 그 다음이 i만큼 증가해서 나타낸다는 것이다.
            if check[j] == True :
                check[j] = False  
                
                
import sys
input = sys.stdin.readline

while(True):                 
    n = int(input()) 

    if n==0 : break
    for i in range(3,r):
        if check[i] == True:
            if check[n-i] == True :    #여러 가지라면, b-a가 가장 큰 것을 출력을 해야하기 때문에 이렇게 한것이다.
                print("%d = %d + %d"%(n , i , n-i))
                break
