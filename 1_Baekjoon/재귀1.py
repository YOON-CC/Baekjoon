def hole(a, box):
    if (a/3<1): # 최소 잡아주기
        return
    
    hole(a/3,box) # 재귀
    
    step1 = 0
    step2 = 0
    
    many = len(box)/a # 얼마나 반복해야 할지, 이차원배열의 길이는 첫줄의 가로 길이이다. 따라서 고정 길이는 잡는다.
    
    for m in range(int(many)): #첫번재 반복은 제일마지막 즉, 높이, 두번재 반복은 가로 따라서 가로를 먼저하고 세로를 잡아준다.
        for n in range(int(many)):
            for i in range(int(a/3)+int(step2),int(a/3)+int(a/3)+int(step2)):
                for j in range(int(a/3)+int(step1),int(a/3)+int(a/3)+int(step1)):
                    box[i][j] = " "
            step1+=a
        step1=0
        step2+=a
               
a = int(input())
box = [["*" for _ in range(a)] for _ in range(a)] #첫번째는 일자의 길이, 두번째는 높이의 길이, 그리고 앞에 문자는 채우려는 것

hole(a, box)

for i in range(a):
    for j in range(a):
        print(box[i][j],end="")
    print()