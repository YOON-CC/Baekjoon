#백준 13904
import sys
import heapq

n = int(sys.stdin.readline().rstrip("\n")) ##후행 줄바꿈 제거

nums = []

sums = [0]*(1000+1)

for i in range(n):
    day, value = map(int, sys.stdin.readline().rstrip("\n").split())
    nums.append([-value,day,value]) # 최소힙으로 변환을 하기 위한 -value의 역할
    
heapq.heapify(nums) ## 최소 힙으로 변환

while nums:
    temp = heapq.heappop(nums)
    for i in range(temp[1],0,-1): # 시작, 끝, step  => 끝은 포함하지 않는다.
        if(sums[i]==0):
            sums[i]=temp[2]
            break

print(sum(sums))