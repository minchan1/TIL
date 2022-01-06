## 함수
def isQueueFull() :
    global SIZE, queue, front, rear
    if (rear == SIZE-1) :
        return True
    else :
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print('큐가 꽉 찼습니다')
        return
    rear += 1
    queue[rear] = data

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐가 비었습니다')
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐가 비었습니다')
        return None
    return queue[front+1]

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front=rear=-1

## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print('출구<--', queue, '<--입구')
enQueue('재남')
print('출구<--', queue, '<--입구')
print(deQueue())
print(deQueue())
print('다음 대기 손님 : ', peek())
print(deQueue())
print(deQueue())
print(deQueue())
print('출구<--', queue, '<--입구')
print(deQueue())
print('출구<--', queue, '<--입구')