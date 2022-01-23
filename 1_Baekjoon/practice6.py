a = input() ## 입력의 기본은 문자열이다.
sum = 0
for n in range(0, len(a)): ##범위는 0부터 시작하여 a-1이다.
    if (a[n] == 'A' or a[n] == 'B' or a[n] == 'C'):
        sum+=3
    elif (a[n] == 'D' or a[n] == 'E' or a[n] == 'F'):
        sum+=4
    elif (a[n] == 'G' or a[n] == 'H' or a[n] == 'I'):
        sum+=5        
    elif (a[n] == 'J' or a[n] == 'K' or a[n] == 'L'):
        sum+=6       
    elif (a[n] == 'M' or a[n] == 'N' or a[n] == 'O'):
        sum+=7
    elif (a[n] == 'P' or a[n] == 'Q' or a[n] == 'R' or a[n] == 'S'):
        sum+=8
    elif (a[n] == 'T' or a[n] == 'U' or a[n] == 'V'):
        sum+=9
    elif (a[n] == 'W' or a[n] == 'X' or a[n] == 'Y' or a[n] == 'Z'):
        sum+=10  
print(sum)
