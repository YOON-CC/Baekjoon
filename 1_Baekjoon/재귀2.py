#하노이탑
#11729번
#하노이 탑의 공식은 (2^n)-1이다. 그러나 재귀를 이용하여 풀어보겠다.
#참고사이트 https://data-jj.tistory.com/34
#이해사이트 https://stujune-to-devjune.tistory.com/35

def hanoi(n, src, dst):
    temp = 6 - src - dst
    if n == 0:
        return
    hanoi(n - 1, src, temp)
    print(src, dst)
    hanoi(n - 1, temp, dst)


n = int(input())
print(pow(2, n) - 1)
hanoi(n, 1, 3)
