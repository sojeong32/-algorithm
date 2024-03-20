# 트리순회

def preorder(x):
    print(parent[x], end='')
    if left[x] != '.':
        preorder(parent.index(left[x]))
    if right[x] != '.':
        preorder(parent.index(right[x]))

def inorder(x):
    if left[x] != '.':
        inorder(parent.index(left[x]))
    print(parent[x], end='')
    if right[x] != '.':
        inorder(parent.index(right[x]))

def postorder(x):
    if left[x] != '.':
        postorder(parent.index(left[x]))
    if right[x] != '.':
        postorder(parent.index(right[x]))
    print(parent[x], end='')


N = int(input())
parent = [0]*N
left = [0]*N
right = [0]*N
for i in range(N):
    parent[i] , left[i], right[i] = input().split()

preorder(0)
print()
inorder(0)
print()
postorder(0)