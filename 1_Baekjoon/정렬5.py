#백준 11651
#이차원 배열을 정렬하게 되면 제일 앞의 원소들의 정렬이 가장 우선이고
#만약 앞의 원소들이 같다면 뒤의 원소들이 그 다음 우선순위가 된다.
#배열의 원소의 순서를 바꾸는 방법 => 배열.reverse()

# a = int(input())
# array = []
# for _ in range(a):
#     mix = []
#     a,b = map(int, input().split())
#     mix.append(b)
#     mix.append(a)
#     array.append(mix)

# for b,a in sorted(array):
#     print(a,b)
##########################################################
##########################################################
#이차원배열 종결 ▶ 방법 1
print("------------------------------")
array = []
for _ in range(3):
    mix = []
    a,b = map(int, input().split())
    mix.append(a)
    mix.append(b)
    array.append(mix)
print(array)
print("------------------------------")

#이차원배열 종결 ▶ 방법 2
array = []
for _ in range(3):
    array.append(list(map(int, input().split())))
print(array)
print("------------------------------")

#이차원배열 종결 ▶ 방법 3
box = []
a, b = map(str, input().split())
a = int(a)
box.append([a, b])
print(box)
print("------------------------------")