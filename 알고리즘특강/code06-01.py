## 함수


## 전역
SIZE = 5
stack = [ None for _ in range(SIZE)]
top = -1

# 메인
top += 1
stack[top] = '커피'
top += 1
stack[top] = '녹차'
top += 1
stack[top] = '꿀물'
print(stack)

data = stack[top]
stack[top] = None
top -= 1
print('팝 ==>', data)
data = stack[top]
stack[top] = None
top -= 1
print('팝 ==>', data)
data = stack[top]
stack[top] = None
top -= 1
print('팝 ==>', data)

print(stack)