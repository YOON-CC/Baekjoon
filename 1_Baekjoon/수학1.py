#백준 2775

num = int(input())

for many in range(num):
    k = int(input())
    n = int(input())
    zero_step = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

    if (k == 0): #0층처리
        print(n)
    else:
        for i in range(k):# k번 반복, 즉, 층높이만큼 반복
            for j in range(n-1):
                zero_step[j+1] = zero_step[j]+zero_step[j+1]
        print(zero_step[n-1])    
