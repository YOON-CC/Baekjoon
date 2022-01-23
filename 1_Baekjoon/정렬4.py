box = list(map(int, str(input())))

for i in sorted(box, reverse=True):
    print(i,end="")