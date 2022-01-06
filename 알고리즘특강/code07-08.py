## 함수
def isQueueFull() :
    global SIZE, queue, front, rear
    if (rear != SIZE-1) :
        return False
    elif (rear == SIZE-1) and (front == -1) :
        return True
    else :
        for i in range(front+1, SIZE) :
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print('큐 꽉!')
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
        print('큐 텅~')
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅~')
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
print('입장 손님 : ', deQueue())
print('입장 손님 : ', deQueue())
print('출구<--', queue, '<--입구')
enQueue('재남')
print('출구<--', queue, '<--입구')
enQueue('BTS')
print('출구<--', queue, '<--입구')
enQueue('울랄라')
print('출구<--', queue, '<--입구')