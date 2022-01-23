num = int(input())
weight = []
height = []
order = []
for i in range(num):
    a,b = map(int, input().split())
    weight.append(a)
    height.append(b)

for i in range(num):
    o = 1
    for j in range(num):
        if (weight[i] < weight[j] and height[i] < height[j] ):
            o+=1
    order.append(o)

for i in range(num):
    print(order[i], end=" ")