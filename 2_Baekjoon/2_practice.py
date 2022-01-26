#문자열을 뒤집을 수 있는 것이 있다.
#슬라이스라는 것으로 문자열[::-1] 이렇게 사용하면 문자열이 뒤집힌다.
# ex) hello => olleh
a = int(input())
for _ in range(a):
    n = list(input().split())
    for i in range(int(len(n))):
        if int(len(n[i]))>=2:
            print(n[i][::-1], end=" ")
        else:
            print(n[i],end=" ")
    print()  
        
        