from collections import defaultdict

# preorder, inorder, postorder
tree = defaultdict(list)
N = int(input())
for i in range(N):
    root, left, right = map(str,input().split())
    tree[root].append(left)
    tree[root].append(right)

def preorder(root):
    if root != ".":
        print(root,end="")#루트
        preorder(tree[root][0])#왼쪽 자식
        preorder(tree[root][1])#오른쪽 자식

def inorder(root):
    if root != ".":
        inorder(tree[root][0])
        print(root,end="")
        inorder(tree[root][1])

def postorder(root):
    if root != ".":
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root,end="")



preorder("A")    
print()
inorder("A")
print()
postorder("A")
    