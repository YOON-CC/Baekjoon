#백준7424
import sys
input = sys.stdin.readline

n = int(input())
num = int('9'*(len(str(n))-1))
result = []
cnt = 0

def hello(n):
    global cnt
    for i in range(num):
        x = list(map(int, str(n - i)))    
        
        for j in range(len(x)):
            x.remove(x[j])
            x = ''.join(map(str, x))
            
            if  x == str(i) or x == '0'+str(i):
                result.append(int(x))
                cnt+=1          
            x = list(map(int, str(n - i)))
                        
hello(n)

if 0 in result:
    print(cnt-result.count(0))
else:
    print(cnt)

for i in range(cnt-1,-1, -1):
    if 1 <= result[i] < 10 and (('0'+str(result[i])) in str(n-result[i])):
        print(n-result[i],' + 0', result[i], ' = ', n, sep='') 
    elif result[i] != 0:
        print(n-result[i],'+', result[i], '=', n)