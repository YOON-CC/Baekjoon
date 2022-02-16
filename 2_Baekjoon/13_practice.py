#백준 14939

import sys
input = sys.stdin.readline
 
n = int(input())
table = []
for i in range(n):
    temp = list(map(int, input().split()))
    table.append(temp)
 
dx = [-1, 1, 0, 0, 0]
dy = [0, 0, 0, -1, 1]
ans = 1234
for f in range(1<<n):
    a=[]
    for i in range(n):
        a.append(table[i][:])
    cnt = 0
 
    for i in range(n):
        if f & (1<<i):
            cnt += 1
            for k in range(5):
                nx = i + dx[k]
                ny = 0 + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    a[ny][nx] = not a[ny][nx]
 
    for i in range(1, n):
        for j in range(n):
            if a[i-1][j]:
                for k in range(5):
                    nx = j + dx[k]
                    ny = i + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        a[ny][nx] = not a[ny][nx]
                cnt += 1
 
 
    can = True
    for i in range(n):
        if a[-1][i] == True:
            can = False
            break
 
    if can:
        ans = min(cnt, ans)
 
print(ans if ans != 1234 else -1)