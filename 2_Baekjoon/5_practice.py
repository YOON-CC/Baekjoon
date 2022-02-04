#백준 4256
#참고사이트 https://jm-codingmemo.tistory.com/23

#전위순회 ▶ 중 왼 오
#중위순회 ▶ 왼 중 오
#후위순회 ▶ 왼 오 중

def hello(preorder, inorder):
    if len(preorder) == 0:
        return
    elif len(preorder) == 1:
        print(preorder[0], end=' ')
        return
    elif len(preorder) == 2:
        print(preorder[1], preorder[0], end=' ')
        return
    
    root_idx = inorder.index(preorder[0])
 
    left_in = inorder[0:root_idx]
    left_pre = preorder[1:1+len(left_in)]
    hello(left_pre, left_in)
 
    right_in = inorder[root_idx+1:]
    right_pre = preorder[len(left_pre)+1:]
    hello(right_pre, right_in)

    print(preorder[0], end=' ')
    
num = int(input())

 
for i in range(num):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    
    hello(preorder, inorder)
    print()