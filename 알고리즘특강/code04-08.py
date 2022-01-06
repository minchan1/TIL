## 함수
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData) :
    global memory, head, current, pre
    if head.data == findData : # 첫 노드 앞에
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    # 중간노드 앞에 삽입
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data == findData :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
    # 마지막에 추가
    node = Node()
    node.data = insertData
    current.link = node
    return

def deleteNode(deleteData) :
    global memory, head, current, pre
    if head.data == deleteData : # 첫노드 삭제
        current = head
        head = head.link
        del(current)
        return
    # 첫노드 외의 삭제
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data == deleteData :
            pre.link = current.link
            del(current)
            return

def findNode(findData) :
    global memory, head, current, pre
    current = head
    if current.data == findData :
        return current
    while current.link != None :
        current = current.link
        if current.data == findData:
            return current
    return Node()

## 전역
memory=[]
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

## 메인
node = Node()  # 첫 노드
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:] :  # ['정연', '쯔위', '사나', '지효']
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)
printNodes(head)

insertNode('다현', '화사')
printNodes(head)
insertNode('사나', '솔라')
printNodes(head)
insertNode('재남', '문별')
printNodes(head)

deleteNode('화사')
printNodes(head)
deleteNode('쯔위')
printNodes(head)
deleteNode('원빈')
printNodes(head)

fNode = findNode('지효')
print(fNode.data)

fNode = findNode('재남')
print(fNode.data)