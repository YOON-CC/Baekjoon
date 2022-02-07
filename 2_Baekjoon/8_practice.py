import sys

sys.setrecursionlimit(10000) 
input = sys.stdin.readline

a,b = map(int, input().split())

box = []
for _ in range(a):
    box.append(list(map(int, input().split())))
    
def maze(l,value,i,j): # 배열, 현재 주체 값, 
       global cnt
       global a,b
       if value == l[a-1][b-1]:
              cnt+=1
              #print("끝")
              #return 
       
       if i!=0:
              if l[i][j] > l[i-1][j]: # 위쪽
                     #print("위", l[i-1][j])
                     maze(l, l[i-1][j],i-1,j)
       
       if i!=a-1:
              if l[i][j] > l[i+1][j]: # 아래쪽
                     #print("아래쪽", l[i+1][j])
                     maze(l, l[i+1][j],i+1,j)   
                        
       if j!=0:
              if l[i][j] > l[i][j-1]:# 왼쪽
                     #print("왼쪽", l[i][j-1])
                     maze(l, l[i][j-1],i,j-1)
             
       if j!=b-1:
              if l[i][j] > l[i][j+1]:# 오른쪽
                     #print("오른쪽", l[i][j+1])
                     maze(l,l[i][j+1],i,j+1)       
          
cnt = 0
maze(box,box[0][0],0,0)
print(cnt)