##############################################################################################################
print("|\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\\__|")

#따옴표나 역슬래쉬를 출력하려면 역슬래쉬를 앞에 붙인다.
##############################################################################################################
a,b = input().split()
print(int(a)-int(b))

#split()은 공백으로 한다는 말, 즉 입력을 공백으로 구분한다라는 말이다.
##############################################################################################################
a = int(input())
b = str(input())
print(a*int(b[2]))
print(a*int(b[1]))
print(a*int(b[0]))
print(a*int(b))

#문자열은 항상 배열(리스트) 형태로 저장이 된다.
##############################################################################################################