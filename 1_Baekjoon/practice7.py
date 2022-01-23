a = input()
num = len(a)

for i in range(1, len(a)):
    string = a[i-1]+a[i]
    if (string == "c=" or string == "c-" or string == "d-" or string == "lj" or string == "nj"
        or string == "s=" or string == "z="):
        num-=1
for i in range(2, len(a)):
    string = a[i-2]+a[i-1]+a[i]
    if (string == "dz="):
        num-=1
print(num)