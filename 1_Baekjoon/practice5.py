#매번 num = 123의 각자리 를 더해라 이런문제가 많은데 이때는 str로 바꾸고
#num[0]+num[1]+num[2] 이렇게 한다.
########################################################################################################
a = input()
print(ord(a))
b = int(input())
print(chr(b))
#문자 -> 아스키코드 : chr()
#아스키코드 -> 문자 : ord()
########################################################################################################
a = input().upper()
b = list(set(a))
lol = [a.count(i) for i in b] # ex) 제일처음 프로그램에서 fdff를 입력 -> [3,1,3,3]
if lol.count(max(lol))>1:
    print("?")
else:
    print(b[lol.index(max(lol))])

#for문안에 count를 쓰게되면 알고리즘 시간이 존나 기니 count안에 for문을 넣는다. 초반에 중복을 제거하여 for문의 i
#를 빠르게 볼 수 있도록 만든다.
########################################################################################################