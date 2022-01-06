import random
## 함수
def seqSearch(ary, fData) :
    pos = -1
    for i in range(len(ary)) :
        if ary[i] == fData :
            pos = i
            break
    return pos

## 전역
dataAry = [ random.randint(10, 99) for _ in range(20)]
findData = dataAry[random.randint(0,19)]

## 메인
print('배열 -->', dataAry)
position = seqSearch(dataAry, findData)
if position == -1 :
    print(findData, ' 없어요ㅠㅠ')
else :
    print(findData, '는', position, '위치에 있어요')