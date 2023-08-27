import sys
n = int(input())
stack = []
for _ in range(n):
    word = sys.stdin.readline().split()  #띄어쓰기 구분해 입력받기
    if word[0] =='push':
        stack.append(word[1])
    elif word[0] =='pop':
        if len(stack)>0:
            print(stack.pop())
        else:
            print(-1)
    elif word[0] =='size':
        print(len(stack))
    elif word[0] =='top':
        if len(stack)>0:
           length = len(stack)-1
           print(stack[length])
        else:
            print(-1)