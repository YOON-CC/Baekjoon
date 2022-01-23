#문제 참고사이트
#https://eunhee-programming.tistory.com/99
#해당 문제는 수학문제로 규칙을 찾는 것이다.
#이러한 문제를 풀경우는 숫자를 처음부터 대입해서 표를 만들고 규칙을 찾아 풀어야한다.


num = int(input())
for n in range(num):
    a,b = map(int, input().split())
    distance = b-a
    n = 1
    sum = 0
    while True:
        sum += 2*n
        if (distance >(sum-2*n)and distance <=sum):
            break
        n+=1
    Max = sum
    Min = (sum - 2*n)+1
    Avg = (Max+Min)/2
    if (distance <Avg):
        print(Max-Min)
    else:
        print(Max-Min+1)



    
    
        
    
    

    
